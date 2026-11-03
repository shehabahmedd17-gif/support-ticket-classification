from .model  import get_model_device
from .decoding import (
    apply_top_k,
    apply_temperature,
    apply_top_p,
    select_next_token
)

from .tokenize import tokenize
import torch


@torch.no_grad()
def generate_text(
    tokenizer,
    model,
    prompt,
    max_new_token = 50,
    temperature = 1.0,
    top_k = None,
    top_p = None
) :


    device = get_model_device(model)

    input = tokenize(tokenizer, prompt, device)

    input_ids = input['input_ids']  # is equal token_ids but different in name bec input_ids i take the shape of tensor 
                                        #token_ids=[5], input_ids=[[5]]
    attention_mask = input['attention_mask']

    prompt_lenght= input_ids.shape[1]

    past_key_values = None   #the past calculated key and value

    for _ in range(max_new_token) :

        if past_key_values is None : 
            outputs = model(
                input_ids = input_ids,
                attention_mask = attention_mask,
                use_cache = True
            )

        else :
            outputs = model(
                input_ids = input_ids[:,-1:],  #take the last token 
                attention_mask = attention_mask,
                use_cache = True,
                past_key_values = past_key_values
            )

        next_token_logit = outputs.logits[:, -1, :]

        past_key_values = outputs.past_key_values

        next_token_logit = apply_temperature(next_token_logit, temperature)

        next_token_logit = apply_top_k(next_token_logit, top_k)

        next_token_logit = apply_top_p(next_token_logit, top_p)

        next_token_id = select_next_token(next_token_logit, temperature)

        if (tokenizer.eos_token_id is not None  
            and  next_token_id.item() == tokenizer.eos_token_id) :
            break

        input_ids = torch.cat(
            [input_ids, next_token_id],
            dim =-1
        )

        attention_mask = torch.cat(
            [
                attention_mask,
                torch.ones(
                    (attention_mask.shape[0], 1), #attention_mask.shape = [2,5]
                                                    #إحنا عايزين نضيف token واحد لكل batch-----> (2, 1)---------->(1,1)
                                                                                                                #(1,1)        

                    device=device,
                    dtype=attention_mask.dtype,
                ),
            ],
            dim=-1,
        )
    generate_ids=input_ids[:,prompt_lenght:] # ده عشان بدل ما يرد السؤال بتاعي كل مره بالاجابه كدا هيرد الاجابه بس

    return tokenizer.decode(generate_ids[0], skip_special_tokens = True)
#                why input_ids[0] , only [batch size] this mean it convert the result into one dim so even [[55,2,5]] this it was this  [5,2]
#       
# 
#          input_ids = tensor(                   [batch_size, sequence_length]
   #           [ [10, 25, 80, 40]] ------------->                                  -------->  [10,25,80,40]                 
 #              )                                       ↓             ↓
 #                                                      1             4

#               
