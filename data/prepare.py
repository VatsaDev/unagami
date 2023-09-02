import os
import random
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

download_file('https://huggingface.co/VatsaDev/unagami/resolve/main/data.txt')


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

    output_filename = os.path.join(output_dir, f'{i}-dataset.txt')
    with open(output_filename, 'w') as f:
      f.writelines(chunk_lines)

split_file('dataset.txt', 'output', 50000)

train_len = 0
val_len = 0

for filename in os.listdir('output'): #blocks are chosen randomly from the text, more of a seamless train val split
  if filename.endswith('.txt'):
    train_or_val = random.randint(0, 9)
    if train_or_val <= 8:
      with open(f'output/{filename}', 'r') as f:
        data = f.read()
      train_ids = enc.encode_ordinary(data)
      train_len = train_len+len(train_ids):
      train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
      print(f"train has {train_len} tokens")
      train_ids = []
    if train_or_val > 8:
      with open(f'output/{filename}', 'r') as f:
        data = f.read()
      val_ids = enc.encode_ordinary(data)
      val_len = val_len+len(val_ids):
      val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
      print(f"val has {val_len} tokens")
      val_ids = []
