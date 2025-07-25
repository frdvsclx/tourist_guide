'''
webde calisan chatbot ekrani 
streamlit framework ile olusturulacak

'''

import streamlit as st 
from langchain.chat_models import ChatOllama 
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory


st.set_page_config(page_title="Tourist Guide", page_icon=" <3")
st.title("Tourist Guide")
st.markdown("You can ask whatever you want about travelling human")

#session state (kullanici gecmisini tutmak icin)
if "memory" not in st.session_state:
    st.session_state.memory =  ConversationBufferMemory(return_messages=True)
    
lama = ChatOllama(model = "llama3.2:3b")


user_input = st.chat_input("place,food.. you can ask whatever you wanna know :)")

if user_input:
    st.session_state.memory.chat_memory.add_user_message(user_input)
    
    messages =[SystemMessage(content="you are a tourist guide..""You can talk about history,food ..")
        ] + st.session_state.memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]

    response = lama(messages)
    
    st.session_state.memory.chat_memory.add_ai_message(response.content)
    

#sohbet gecmisini arayüze gösterme
for msg in st.session_state.memory.chat_memory.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("lama"):
            st.markdown(msg.content)
            
