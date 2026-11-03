from dataclasses import dataclass
from enum import Enum



class Messagesrole(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT  = "assistant"




@dataclass(frozen=True)
class Massages:
    
    role :Messagesrole

    content : str 


@dataclass(frozen=True)
class GenerationRequest:

    prompt:list [Massages]
    temprature :float = 1.0
    top_p : float | None=None
    top_k : int | None = None
    max_tokens : int =100   