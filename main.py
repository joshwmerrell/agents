from rich.console import Console
from rich.markdown import Markdown
console = Console()
from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import types


SYSTEM_PROMPT = """

You are a humble and honest assistant.

"""


client = genai.Client()


chat = client.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[]
    )
)

def get_response(prompt: str) -> str:
    response = chat.send_message(prompt)
    return response.text

def main():
    while True:
        try:
            prompt = input("Input: ")
            if prompt == "exit": break
            response = get_response(prompt)
        except EOFError:
            break
        console.print(Markdown(response))

if __name__ == "__main__":
    main()

# **CODE FOR OTHER AGENTS OTHER THAN GEMINI**
# from langchain.agents import create_agent


# SYSTEM_PROMPT = "You are a passive aggressive assistant."


# agent = create_agent(
#     model="google_genai:gemini-flash-lite-latest",
#     tools=[],
#     system_prompt=SYSTEM_PROMPT
# )


# def get_response(prompt: str) -> str:
#     response = agent.invoke({"messages": [prompt]})
#     print(response["messages"][-1].text)

# def main():
#     while True:
#         try:
#             prompt = input("Input: ")
#             if prompt == "exit": break
#             response = get_response(prompt)
#         except EOFError:
#             break
#         # console.print(Markdown(response))
#         print(response)

# if __name__ == "__main__":
#     main()