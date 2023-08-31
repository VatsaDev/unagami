# Unagami
![image](https://user-images.githubusercontent.com/71975550/264119150-aa059609-6535-4d78-878f-3efbc17f582a.png)

The next AI model after NanoChatGPT, this model is meant for more informational capabilities, closer to a mainstream LLM

all updates at [updates.md](https://github.com/VatsaDev/unagami/blob/main/updates.md)   
**Add Colab link**      

## Features
 - speaks several, proper informative sentences. 


## how does it work?

Format inspired by `oasst-pythia-12b` 
```
<system> ... <endOfText>
<human> ... <endOfText>
<Bot> ... <endOfText>
<human> ... <endOfText>
<Bot> ... <endOfText>
<human> ... <endOfText>
<Bot> ... <endOfText>
```

## Problems / TODOs
   - more data
     - need more data
   
## whats in the data
 - oasst/oasst-1
 - eluthierAI/arithmetic
 - camel-ai/math
 - garage-bAInd/Open-Platypus

#### Limitations 

I did not make the data dumps/corpuses that make up this data, and can't account for any biases, as the dataset it self is based off the conversations of real people who may or may not have had biases. The model is meant for academic research purposes, and isn't meant for any important or high risk scenarios. Do not follow its advice

#### citations
```
@article{brown2020language,
    title={Language Models are Few-Shot Learners},
    author={Tom B. Brown and Benjamin Mann and Nick Ryder and Melanie Subbiah and Jared Kaplan and Prafulla Dhariwal and Arvind Neelakantan and Pranav Shyam and Girish Sastry and Amanda Askell and Sandhini Agarwal and Ariel Herbert-Voss and Gretchen Krueger and Tom Henighan and Rewon Child and Aditya Ramesh and Daniel M. Ziegler and Jeffrey Wu and Clemens Winter and Christopher Hesse and Mark Chen and Eric Sigler and Mateusz Litwin and Scott Gray and Benjamin Chess and Jack Clark and Christopher Berner and Sam McCandlish and Alec Radford and Ilya Sutskever and Dario Amodei},
    year={2020},
    eprint={2005.14165},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

@misc{li2023camel,
      title={CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society}, 
      author={Guohao Li and Hasan Abed Al Kader Hammoud and Hani Itani and Dmitrii Khizbullin and Bernard Ghanem},
      year={2023},
      eprint={2303.17760},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}

@article{platypus2023,
    title={Platypus: Quick, Cheap, and Powerful Refinement of LLMs}, 
    author={Ariel N. Lee and Cole J. Hunter and Nataniel Ruiz},
    booktitle={arXiv preprint arxiv:2308.07317},
    year={2023}
}
```
