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

print("hi im lama, here to help ;) ...")

while True:
    user_input = input("siz:")
    
    if user_input.lower() == "quit":
        print("lama is sad, by")
        break 
    
    memory.chat_memory.add_user_message(user_input)
    
    messages = [SystemMessage(content="you are a tourist guide..")] + memory.load_memory_variables({})["history"] 
    + [HumanMessage(content=user_input)]

    response = happy_lama(messages) #modelden yanit alma
    memory.chat_memory.add_ai_message(response.content)
    print(f"guide: {response.content}")

