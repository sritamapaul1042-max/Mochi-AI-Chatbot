from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(page_title="Mochi - Roast Bot", page_icon="🎀")

SYSTEM_PROMPT = """
You are a funny and witty roast assistant named Mochi.

Your job is to roast the user in a playful, sarcastic, and clever way.
Keep the roasts humorous rather than genuinely hateful or abusive.
Use light sarcasm, jokes, and clever comebacks.
Match the user's energy: if they joke, joke back.
Never use slurs, threats, or attacks based on protected characteristics.
"""


@st.cache_resource
def get_model():
    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )


model = get_model()

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]

if "ended" not in st.session_state:
    st.session_state.ended = False

# ---------- Header ----------
st.title("🎀 Mochi")
st.caption("Your witty roast assistant. Type 0 to exit.")

# ---------- Chat history ----------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🎀"):
            st.markdown(msg.content)

# ---------- Input ----------
if st.session_state.ended:
    st.info("Chat ended. Refresh the page to start again.")
else:
    prompt = st.chat_input("You: ")

    if prompt:
        if prompt.strip() == "0":
            st.session_state.ended = True
            st.rerun()

        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🎀"):
            with st.spinner("Mochi is cooking up a roast..."):
                response = model.invoke(st.session_state.messages)
            st.markdown(response.content)

        st.session_state.messages.append(AIMessage(content=response.content))