from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_temperature():
    """
    get the curren temperature for a given city
    """
    return 20.0




def main():
    user_input = input("your question: ")
    promt= f""" 
    your are a helpful assistan. answwer the user's question in a friendly way.

    you can also use tools if you feel like they help you provide a better answer:
    - get_temperature(city: str): -> float: get the current temperature for a given city

    if you want to use ona of these tools, you should output the tool name and its arguments in the follosing format:
    tool_name: arg1, arg2, ...
    for example:
    get_temperature: London
    whnitch that in mind, answer the user's question: 
    <user-question>
    {user_input}
    </user-question>
    """
    responses = client.responses.create(
        model="gpt-5-mini",
        input=promt
    )
    reply = responses.output_text
    if reply.startswith("get_temperature:"):
        arg= reply.splait(":")[1].strip()
        temperature = get_temperature(arg)
        promt= f"""
        you are a helpful assistant. answer the user's question in a friendly way.
        here's the user's question : 
        <user-question>
        {user_input}
        </user-question>
        you requeste to user  the get_temperature tool with the following argument: {arg}
        """
        responses = client.responses.create(
            model="gpt-5-mini",
            input=promt
        )
        reply = responses.output_text
        print(reply)
    else: 
        print(reply)
    return reply

if __name__ == "__main__":
    main()