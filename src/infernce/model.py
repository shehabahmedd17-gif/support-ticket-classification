from transformers import AutoTokenizer, AutoModelForCausalLM
from .config import (MODEL_NAME, DEVICE_MAP, TORCH_DTYPE)


def load_model() :
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model     = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, device_map=DEVICE_MAP,torch_dtype=TORCH_DTYPE)
    return tokenizer, model


def get_model_device(model) :

    return model.get_input_embeddings().weight.device

