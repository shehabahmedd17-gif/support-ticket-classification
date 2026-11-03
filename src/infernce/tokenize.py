import torch

def tokenize(tokenizer, text, device):

    inputs = tokenizer(text, return_tensors='pt')

    # {"inputs_ids":[23,23,23,23], "attention_mask":[1111]}
    return{key: value.to(device) for key, value in inputs.items()}
    