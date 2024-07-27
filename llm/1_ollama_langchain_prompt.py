from pprint import pprint

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
)

chain = prompt | llm
response = chain.invoke(
    {
        "input_language": "Korean",
        "output_language": "German",
        "input": "좋은 아침",
    }
)

print(type(response))  # langchain_core.messages.ai.AIMessage
res = response.to_json()
print(type(res)) # dict
pprint(res)
# pprint(response.dict())
