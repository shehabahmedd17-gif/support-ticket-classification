from .structered_model import create_structered_model

class StructuredGeneration : 

    def __init__(self, model, tokenizer):
        self.model = create_structered_model(model, tokenizer)

    def generate(self, prompt, schema) :

        return self.model( prompt,  schema , max_new_tokens=200 )



##                     ===========




    ##structured_model = create_structured_model(model, tokenizer)
   
    # result = structured_model(prompt, schema)