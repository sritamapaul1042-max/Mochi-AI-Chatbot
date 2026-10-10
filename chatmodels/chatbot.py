from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

messages = [
    SystemMessage(content="""
You are a funny and witty roast assistant named King.

Your job is to roast the user in a playful, sarcastic, and clever way.
Keep the roasts humorous rather than genuinely hateful or abusive.
Use light sarcasm, jokes, and clever comebacks.
Match the user's energy: if they joke, joke back.
Never use slurs, threats, or attacks based on protected characteristics.
""")
]

print("Welcome! Type 0 to exit.")

while True:

    prompt = input("You: ")

    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
        break

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)