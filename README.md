
# 🍌 Banana Serverless

This repo gives a framework to serve ML models in production using simple HTTP servers.

Information taken from: https://huggingface.co/Writer/palmyra-base

# Model Description
Palmyra Base was primarily pre-trained with English text. Note that there is still a trace amount of non-English data present within the training corpus that was accessed through CommonCrawl. A causal language modeling (CLM) objective was utilized during the process of the model's pretraining. Similar to GPT-3, Palmyra Base is a member of the same family of models that only contain a decoder. As a result, it was pre-trained utilizing the objective of self-supervised causal language modeling. Palmyra Base uses the prompts and general experimental setup from GPT-3 in order to conduct its evaluation per GPT-3.

# Use case
Palmyra Base is extremely powerful while being extremely fast. This model excels at many nuanced tasks such as sentiment classification and summarization.

# Training data
Palmyra Base (5b) was trained on Writer’s custom dataset.

# Citation

```bibtex
@misc{Palmyra,
  author = {Writer Engineering team},
  title = {{Palmyra-base Parameter Autoregressive Language Model}},
  howpublished = {\url{https://dev.writer.com}},
  year = 2023,
  month = January 
}
```

<br>

# Helpful Links
Understand the 🍌 [Serverless framework](https://docs.banana.dev/banana-docs/core-concepts/inference-server/serverless-framework) and functionality of each file within it.

Generalize this framework to [deploy anything on Banana](https://docs.banana.dev/banana-docs/resources/how-to-serve-anything-on-banana).

<br>

## Use Banana for scale.
