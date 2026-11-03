import torch

def apply_temperature(logits, temperature) : 
    """
    scale logits using temperature.

    temperature < 1 --> sharper dist
    temperature > 1 --> flatter dist
    temperature = 1 --> unchanged 
    """
    if temperature <=0 : 
        return logits
    return logits / temperature


def apply_top_k(logits, top_k) : 

    if top_k is None or top_k <= 0 : 
        return logits

    top_k = min(top_k, logits.size(-1))

    values, _ = torch.topk(logits, top_k)

    thershold = values[:, -1].unsqueeze(-1)


    logits = logits.masked_fill(
        logits < thershold,
        float('-inf')
    )

    return logits

def apply_top_p(logits, top_p) : 

    if top_p is None or top_p >= 1.0 : 
        return logits

    if not 0.0 < top_p <=1.0 : 
        raise ValueError("top_p must be between 0 and 1.")

# [batch_size, seq_len ,voca_size]

    sorted_logits, sorted_indices = torch.sort(
        logits,
        descending= True,
        dim=-1
    )

    sorted_probs = torch.softmax(sorted_logits, dim=-1)

    cumulative_prob = torch.cumsum(sorted_probs, dim=-1)

    sorted_indices_to_remove = cumulative_prob > top_p

    # top_p = .9 
    # [.1 ,   .5,  .8 , .91 , .98]
    # [true  true true true False  ]

    sorted_indices_to_remove[...,1:] = (sorted_indices_to_remove[...,:-1].clone()) #Shift the mask one position to the right.

    sorted_indices_to_remove[...,0] = False #Never remove the highest-probability token.

    indices_to_remove = torch.zeros_like(
        logits,
        dtype=torch.bool
    )

    indices_to_remove.scatter_(
        dim=-1,
        index=sorted_indices,
        src = sorted_indices_to_remove     #فغيّرنا ترتيب الـ logits.

# وبالتالي الـ mask اللي عملناها أصبحت مرتبطة بالترتيب الجديد:
    )

    logits  = logits.masked_fill(
        indices_to_remove,
        float('-inf')
    )

    return logits


def select_next_token(logits, temperature) : 
    if temperature == 0 :

        return torch.argmax(logits, dim=-1, keepdim=True)
    
    logits = logits / temperature

    probabilities = torch.softmax(logits, dim =-1)


    return torch.multinomial(probabilities, num_samples=1)#multinomial choose by defulte even if was a hight prop may not choosen in the next time

