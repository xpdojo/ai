from pprint import pprint

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "너는 중고차 판매를 도와주는 어시스턴트야." +
            "human이 우리 서비스의 자동차를 구매하도록 유도하고 관련 질문 아니면 대답해줄 수 없다고 해.",
        ),
        (
            "human",
            "{input}"
        ),
    ]
)

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
)

chain = prompt | llm
response = chain.invoke(
    {
        "input": "현대자동차 중고차 구매하고 싶어요.",
    }
)

res = response.to_json()
print(type(res))
pprint(res)
# pprint(response.dict())
