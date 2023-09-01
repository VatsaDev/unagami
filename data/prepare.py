import os
import requests
import tiktoken
import numpy as np

train_ids=[]
val_ids=[]
enc = tiktoken.get_encoding("gpt2")

def download_file(url):
  response = requests.get(url)
  if response.status_code == 200:
    with open('dataset.txt', 'wb') as f:
      f.write(response.content)
      print("downloaded dataset, tokenizing")
  else:
    print('Error downloading file:', response.status_code)

download_file('https://huggingface.co/VatsaDev/ChatGpt-nano/resolve/main/Dataset.txt')


def split_file(filename, output_dir, chunk_size):
  if not os.path.exists(output_dir):
    os.mkdir(output_dir)

  with open(filename, 'r') as f:
    lines = f.readlines()

  n_chunks = len(lines) // chunk_size
  for i in range(n_chunks):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, len(lines))

    chunk_lines = lines[start:end]

    output_filename = os.path.join(output_dir, f'{i+10}-dataset.txt')
    with open(output_filename, 'w') as f:
      f.writelines(chunk_lines)

split_file('dataset.txt', 'output', 10000)

def is_numbers(string):
  two_chars = string[:2]

  try:
    int(two_chars)
    return True
  except ValueError:
    return False
    
def get_num_txt_files(output_dir):
  num_txt_files = 0
  for filename in os.listdir(output_dir):
    if filename.endswith('.txt'):
      num_txt_files += 1
    print(f"there are {num_txt_files} text files")
  return num_txt_files

num_files = get_num_txt_files("output")

for filename in os.listdir('output'):
  if filename.endswith('.txt'):
    if is_numbers(filename) == True:
      if int(filename[:2]) < num_files*0.9:
        with open(f'output/{filename}', 'r') as f:
          data = f.read()
        train_ids = train_ids+enc.encode_ordinary(data)
      if int(filename[:2]) > num_files*0.9:
        with open(f'output/{filename}', 'r') as f:
          data = f.read()
        val_ids = val_ids+enc.encode_ordinary(data)

print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
