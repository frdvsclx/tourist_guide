'''
problem tanimi:
-kullanicilar Sri Lanka özelinde turist 

model: LLAMA 3.2 3B (Meta AI)
    -acik kaynakli
    -verimli
    -modüler
    -localde calisabilir

plan/prgramlama:
-ollama indir ve lama kur


importing libraries:
-langchain
-langchain_community
-ollama
-streamlit

pip install langchain langchain_community ollama streamlit

'''

from langchain.chat_models import ChatOllama
from langchain.schema import SystemMessage,HumanMessage 
from langchain.memory import ConversationBufferMemory

happy_lama = ChatOllama(model="llama3.2:3b")

memory = ConversationBufferMemory(return_messages=True) #mesajlar formatlı döner

print("selam ben turizm rehberi ;) ...")

while True:
    user_input = input("siz:")
    
    if user_input.lower() =="quit"
        print("lama is sad, by")
        break
    
    



