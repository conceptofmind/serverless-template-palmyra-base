from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    global tokenizer
    
    model = AutoModelForCausalLM.from_pretrained("Writer/palmyra-base", torch_dtype=torch.float16).cuda()

    # the fast tokenizer currently does not work correctly
    tokenizer = AutoTokenizer.from_pretrained("Writer/palmyra-base", use_fast=False)

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model
    global tokenizer

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    input_ids = tokenizer.encode(prompt, return_tensors='pt').cuda()
    output = model.generate(
        input_ids, 
        max_length=100, 
        do_sample=True, 
        top_k=50, 
        top_p=0.95, 
        num_return_sequences=1, 
        temperature=0.9, 
        early_stopping=True, 
        no_repeat_ngram_size=3, 
        num_beams=5, 
        length_penalty=1.5, 
        repetition_penalty=1.5, 
        bad_words_ids=[[tokenizer.encode(' ', add_prefix_space=True)[0]]]
        )

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    # Return the results as a dictionary
    result = {'output': result}
    return result


if __name__ == "__main__":
    init()
    print(inference({'prompt': 'The sun is shining'}))