import os 
import sys
sys.path.append(os.path.abspath('..'))
from src.infernce.model import load_model
from src.structered.schema import Tickets
from src.structered.generator import StructuredGeneration
from prompt.classifier_prompt import classifer_prompt

def main():

    tokenizer,model  =load_model()

    user_query='I received my order early and everything looks great'

    prompt=classifer_prompt(user_query)

    generator=StructuredGeneration(model,tokenizer)

    output=generator.generate(prompt,Tickets)

    print(output)

if __name__== '___main__':


    main() 
   



