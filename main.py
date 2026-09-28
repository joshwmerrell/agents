# Get info from the following sources for this: https://byuidatascience.github.io/agentic_ai_course/lessons/lesson1_4.html , ./ai-conversations/'How do I add a system prompt with this_.docx', and ./ai-conversations/'The last hint in this page_guide has me create a....docx'


# *** CODE FOR USING GOOGLE'S TOOLS INSTEAD OF LANGCHAIN'S ***
# from rich.console import Console
# from rich.markdown import Markdown
# console = Console()
# from dotenv import load_dotenv
# load_dotenv()
# from google import genai
# from google.genai import types


# SYSTEM_PROMPT = """

# You are a humble and honest assistant.

# """


# client = genai.Client()


# chat = client.chats.create(
#     model="gemini-flash-lite-latest",
#     config=types.GenerateContentConfig(
#         system_instruction=SYSTEM_PROMPT,
#         tools=[]
#     )
# )

# def get_response(prompt: str) -> str:
#     response = chat.send_message(prompt)
#     return response.text

# def main():
#     while True:
#         try:
#             prompt = input("Input: ")
#             if prompt == "exit": break
#             response = get_response(prompt)
#         except EOFError:
#             break
#         console.print(Markdown(response))

# if __name__ == "__main__":
#     main()
# *** CODE FOR USING GOOGLE'S TOOLS INSTEAD OF LANGCHAIN'S ***


import os
import uuid
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool


from rich.markdown import Markdown
from rich.console import Console
console = Console()
from langchain.agents import create_agent


load_dotenv()



# Define the tools available to the agent
tools = []

# Initialize LangChain LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    temperature=0
)

# Initialize memory checkpointer
memory = MemorySaver()

# System prompt
SYSTEM_PROMPT = """

    You are a humble and concise assistant.

"""

# Create agent
agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    system_prompt=SYSTEM_PROMPT
)


thread_config = {"configurable": {"thread_id": str(uuid.uuid4())}}




def get_response(prompt: str) -> str:
    input = {"messages": [prompt]}
    response = agent.invoke(input, config=thread_config)
    return response["messages"][-1].text

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