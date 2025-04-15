import os
from dotenv import load_dotenv
import log
import sys

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import StreamingStdOutCallbackHandler

# API KEY 정보로드
load_dotenv()

log.langsmith('First Chagbot')

# 1. System prompt (역할 지정)
system_prompt = SystemMessagePromptTemplate.from_template(
    "당신은 친절하고 지식이 풍부한 한국어 AI 챗봇입니다. 항상 정중하고 상세하게 대답하세요."
)

# 2. User prompt 설정

user_prompt = HumanMessagePromptTemplate.from_template("{user_input}")

# 3. CahtPromptTemplate으로 결합
chat_prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

# 4. Streaming 가능한 LLM 구성
model = ChatOpenAI(
    model= 'gpt-4-turbo',
    temperature= 0.7,
    max_tokens=256,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# 5. Output Parser
parser = StrOutputParser()

# 6. 전체 체인 구성
chain = chat_prompt | model | parser

# Method
def run_chatbot():
    print("🥔🥔🥔 말하는 감자의 스트리밍 챗봇에 오신 걸 환영합니다! (종료: exit)🥔🥔🥔")
    while True:
        print("\n👤 User: ", end="", flush=True)
        try:
            user_input = sys.stdin.readline().strip()
        except UnicodeDecodeError:
            print("❌ 입력 인코딩 오류가 발생했습니다. 다시 입력해주세요.")
            continue

        print("🤖 챗봇: ", end="", flush=True)
        try:
            _ = chain.invoke({"user_input": user_input})
            print("")  # 줄바꿈
        except Exception as e:
            print(f"\n⚠️ 오류 발생: {e}")


if __name__ == '__main__':
    run_chatbot()