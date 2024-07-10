from groq import Groq
from langchain.schema import SystemMessage,AIMessage,HumanMessage
import json
import sys
import re

class Process:
    def __init__(self):    
        self.helper_client =  Groq(
            api_key="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",
        )

    def chatBot(self, user_prompt):
        user_prompt = user_prompt
        # read the list of converstation and add user prompt to it the send to  the llm
        with open("conversation.txt","r") as f:
            base_conversation = f.read()
            # base_conversation = [n.strip().replace("'","") for n in base_conversation]
        ai_response = self.llm(str(base_conversation),"llama3-8b-8192")

        with open("conversation.txt", "w") as f:
            base_conversation += "\n"+ai_response
            f.writelines(base_conversation)
        
        return ai_response
        
    
    def llm(self, prompt, model):
        response = self.helper_client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": """You are an AI chatbot designed to interact with an SQL Server containing ERP system data. 
            Your purpose is to assist users in querying and managing this data efficiently and accurately."""
            },
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=4096,
        top_p=0.8,
        model = model,

        )
        return response.choices[0].message.content.replace('```','').replace('json','')