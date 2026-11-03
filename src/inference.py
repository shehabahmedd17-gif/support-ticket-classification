


#   ticket ---> llm ----> category, summary, urgency, sentiment (Structured Output)
# 1- using prompt 
#    --- structured prompt 
#    --- few-shot   prompt 

# category  [technical, account, delivery, billing, subscription]
# sentiment [positive, negative, neutral]
# urgency  [high, meduim, low]
# summary  " ticket summary"



 # prompt_template = """
    #         you are ticket classifer.
    #         your task is to classify customer ticket and generate this structured output
    #         category 
    #         sentiment
    #         urgency  
    #         summary  
    #         i need it as valid json
    #         customer ticket :
    #         {message}
    #         """
    # user_message = 'My laptop screen is broken and I need urgent help to fix it before my presentation tomorrow.'
    # prompt = prompt_template.format(message=user_message)









