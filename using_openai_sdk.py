
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),

)


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
    response = client.responses.create(
        model="gpt-5-mini",
        input=promt
    )
    return response.output_text


def main():
    # user input => AI (LLM) to generate a X post
    
    user_input= input("what should the post be about?")
    x_post=generate_x_post(user_input)
    print(x_post)
    

if __name__ == "__main__":
    main()
