
import os 

import requests
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_KEY= os.getenv("OPENAI_API_KEY")

def generate_x_post(usr_inpt: str) -> str:
    # call ai /llm 
    promt= f"""
    you are a expert social media manager, and you excel at crafting viral and highly engaging post for X(formerly twitter).
    you task is a post that is consice, engaging, and has a high potential for virality.
    avoid using hashtags, and lots of emojis(a few emojis are okay, but not too many).
    keep the post sort and focused, structure it in a clean, redeable way, using line breaks and empty lines to enhace redability.
    here is the topic privded by the user for which you need to generate a post:
    <topic>
    {usr_inpt}
    </topic>
    """
    payload= {
        "model": "gpt-5-mini",
        "input": promt
    }
    response = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload, 
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPEN_AI_KEY}"
        })
    
    response_text=response.json().get("output",[{}])[1].get("content",[{}])[0].get("text","")
    return response_text


def main():
    # user input => AI (LLM) to generate a X post
    
    user_input= input("what should the post be about?")
    x_post=generate_x_post(user_input)
    print(x_post)
    

if __name__ == "__main__":
    main()
