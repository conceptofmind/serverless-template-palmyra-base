from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

from transformers import pipeline

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    AutoModelForCausalLM.from_pretrained("Writer/palmyra-base", torch_dtype=torch.float16)

    # the fast tokenizer currently does not work correctly
    AutoTokenizer.from_pretrained("Writer/palmyra-base", use_fast=False)

if __name__ == "__main__":
    download_model()