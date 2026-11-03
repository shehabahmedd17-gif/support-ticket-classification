# import os 
# from dotenv import load_dotenv
# load_dotenv()


# Api_key=os.getenv('Api_key')

# it_s mean go to file .env and take the api only, if api is none it contain until you know the error 
# this why basesetting come for it make validation to the parameter you put in
# --------------------------------------------------------
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class LLMSettings(BaseSettings):
    api_key:str=Field(...,min_length=1,validation_alias='LLM_api_key')

    base_url:str=Field('https://api.groq.com/openai/v1',min_length=1,validation_alias='LLM_base_url')

    max_attempts: int =Field(3,ge=1,validation_alias='LLM_max_attempts')

    model:str =Field(...,min_length=1,validation_alias='LLM_model')

    base_delay:int = Field(2,ge=0,validation_alias='LMM_base_delay')            #  Attempt 1 → fail → wait 1 sec
                                                                                #  Attempt 2 → fail → wait 2 sec
                                                                                #  Attempt 3 → fail → wait 4 sec

    timeout: int = Field(30 , ge=0,validation_alias='LLM_timeout')

    model_config=SettingsConfigDict(env_file='.env' , env_file_encoding='utf-8',extra='ignore')