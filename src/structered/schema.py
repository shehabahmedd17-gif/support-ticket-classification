# validation 
from pydantic import BaseModel 
from typing import Literal
class TicketOutput(BaseModel):
    category : Literal["technical", "account", "delivery", "billing", "subscription"] 
    sentiment: Literal['positive','neative','neutral'] 
    urgency : Literal['low','high','meduim']
    summary : str
    