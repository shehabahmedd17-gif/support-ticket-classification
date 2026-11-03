from dotenv import load_dotenv
import os
load_dotenv()


MODEL_NAME = os.getenv("MODEL_NAME")

DEVICE_MAP = os.getenv("DEVICE_MAP", 'auto')

TORCH_DTYPE = os.getenv("TORCH_DTYPE", 'auto')



if MODEL_NAME is None : 
    raise ValueError("Please select Model")



