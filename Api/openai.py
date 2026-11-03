from .base import  LMM
from openai import OpenAI
from .config import LLMSettings
from .model import GenerationRequest

class OpenAICombatable(LMM):
    def __init__(self,setting: LLMSettings):
        self.client= OpenAI(api_key=setting.api_key,base_url=setting.base_url)
        self.model=setting.model

    def generate(self, request:GenerationRequest):
        messages=[
            {
                'role' : message.role.value ,
                'content': message.content
            }
        
            for message in request.messages
        ]

        res=self.client.chat.completions.create(model=self.model , messages=messages)

        return res.choices[0].message.content