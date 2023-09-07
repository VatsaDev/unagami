# Unagami!
![Component 1 (2)](https://github.com/VatsaDev/unagami/assets/71975550/4f1fdab4-216a-4717-bf16-4ef542928408)
The next AI model after NanoChatGPT, this model is meant for more informational capabilities, closer to a mainstream LLM

all updates at [updates.md](https://github.com/VatsaDev/unagami/blob/main/updates.md)   
[Colab run and finetune](https://colab.research.google.com/drive/1iJkZDlV1U9l5LR9ariqY-EhV0kaSwygS?usp=sharing)  

## Features
 - speaks several, proper informative sentences on multiple topics.
 - Trained on 5.5 billion tokens
 - 20GB dataset
 - System prompt
 - Sounds Self aware, may often call itself Unagami or call me its developer


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

## whats in the data
 - oasst/oasst-1
 - eluthierAI/arithmetic
 - camel-ai/math
 - garage-bAInd/Open-Platypus
 - openorca/openorca
 - fnlp/moss-002-sft-data
 - nomic-ai/gpt-4-all-prompt-gen
 - databricks/dolly-15k
 - codeparrot/codeparrot-self-instruct
 - TheoremQA
 - zhiqings/dromedary-65b
 - ArtifactAI/arxiv-math-instruct
 - xiyuez/im-feeling-curious
 - Dahoas/synthetic-instruct-gptj-pairwise
 - Muennighoff/flan
 - swype/instruct
 - teven/code_contests
 - samsum
 - multi_news
 - nampdn-ai/tiny-codes
 - MBZUAI/LaMini-instruction
 - izardLM/WizardLM_evol_instruct_70k

#### Limitations 

I did not make the data dumps/corpuses that make up this data, and can't account for any biases. The model is meant for academic research purposes, and isn't meant for any important or high risk scenarios. Do not follow its advice

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

@misc{OpenOrca,
  title = {OpenOrca: An Open Dataset of GPT Augmented FLAN Reasoning Traces},
  author = {Wing Lian and Bleys Goodson and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/Open-Orca/OpenOrca},
}
```
