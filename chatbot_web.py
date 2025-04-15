# chatbot_web.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
import log
import streamlit as st

# 환경변수 로딩
load_dotenv()

# LangSmith 설정은
log.langsmith('First Chagbot')

# 시스템 프롬프트 및 프롬프트 템플릿 설정
system_prompt = SystemMessagePromptTemplate.from_template(
    "당신은 친절하고 지식이 풍부한 한국어 AI 챗봇입니다. 항상 정중하고 상세하게 대답하세요."
)
user_prompt = HumanMessagePromptTemplate.from_template("{user_input}")
chat_prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

# 모델 및 파서
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=512,
)
parser = StrOutputParser()
chain = chat_prompt | llm | parser

# Streamlit UI
st.set_page_config(page_title="🥔🥔🥔 말하는 감자", page_icon="🥔")
st.title("🥔 말하는 감자의 한국어 챗봇")
st.write("GPT-4 기반 챗봇입니다. 궁금한 점을 물어보세요!")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 메시지 기록 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if user_input := st.chat_input("무엇을 도와드릴까요?"):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        # 응답 생성
        with st.spinner("답변 생성 중..."):
            response = chain.invoke({"user_input": user_input})
            st.markdown(response)

    # 챗봇 메시지 추가
    st.session_state.messages.append({"role": "assistant", "content": response})
