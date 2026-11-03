import json 
from pydantic import ValidationError
from .schema import TicketOutput

def parsing_validation(raw_output:str):


    try:
         data=json.loads(raw_output)

         ticket=TicketOutput.model_validate(data)

         return TicketOutput
    except json.JSONDecodeError:
         raise ValueError (' MODEL output does not valid json')

    except ValidationError:
         raise ValueError (' MODEL output does not match ticket ')
         




