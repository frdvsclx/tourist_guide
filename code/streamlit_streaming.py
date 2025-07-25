import streamlit as st

from langchain.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory

#streaming callbacks
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler #streamlit ile calısmak icin handler basei
from typing import Any

#özel streaming callback tanimi
class StreamHandler(BaseCallbackHandler):
    def __init__(self,placeholder):
        self.placeholder = placeholder #streamlitteki mesaj kusus
        self.final_text=  "" #
        
    def on_llm_new_token(self, token:str, chunk = None, **kwargs: Any) -> None:    
        self.final_text +=token #token birlestirme
        self.placeholder.markdown(self.final_text + "") 
    
    
#baslik, aciklama    
st.set_page_config(page_title="Tourist Guide", page_icon="🦙")
st.title("Tourist Guide LLama ✨")
st.markdown("I am here for the chat about travelling and stuff")

#session state (kullanici gecmisini tutmak icin)
if "memory" not in st.session_state:
    st.session_state.memory =  ConversationBufferMemory(return_messages=True)

#kullaninicinin mesajı yazicagi kutu
user_input = st.chat_input("Happy Lama,Sad Lama,Mentally Disturbed Lama,Super Lama,Drama Lama,Big Fat Mama Lama!")

#sohbet gecmisini arayüze gösterme
for msg in st.session_state.memory.chat_memory.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    else:
        with st.chat_message("lama"):
            st.markdown(msg.content)

if user_input:
    st.session_state.memory.chat_memory.add_user_message(user_input)
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("lama"):
        response_placeholder = st.empty() #gecici mesaj kutusu
        stream_handler =StreamHandler(response_placeholder)    
        lama = ChatOllama(model = "llama3.2:3b",streming = True,callbacks=[stream_handler])

        messages =[SystemMessage(content="You are a tourist guide..""You can talk about history,food ..")
            ] + st.session_state.memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]

        response = lama(messages)
        
        st.session_state.memory.chat_memory.add_ai_message(response.content)
    