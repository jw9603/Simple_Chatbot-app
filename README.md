# Simple_Chatbot-app

LangChain + OpenAI + Streamlit으로 만든 [한국어 기반 스트리밍 챗봇 프로젝트](https://malgamchatbot.streamlit.app/)입니다.

![챗봇 시연](./demo/앱.gif)


## 1. 소개
LangChain Expression Language (LCEL) 을 활용한 간단하고 깔끔한 체인 구성

System + User PromptTemplate 으로 역할과 질문을 구분

OpenAI GPT-4-Turbo 모델 사용

Streamlit 인터페이스로 누구나 쉽게 사용 가능

StreamingStdOutCallbackHandler로 실시간 응답 제공


## 2. 기술 스택

- **Python 3.11+**
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4 Turbo](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [Poetry](https://python-poetry.org/) (패키지 관리)



## 3. 주요 파일 구성

| 파일명 | 설명 |
|--------|------|
| `chatbot.py` | 터미널 기반 챗봇 실행용 |
| `chatbot_web.py` | Streamlit 기반 웹 챗봇 실행용 |
| `(.gitnore) .env` | OpenAI API 키 등 환경변수 저장 (커밋 제외) |
| `.streamlit/secrets.toml` | 배포용 비밀키 설정 파일 |
| `README.md` | 프로젝트 소개 문서 |

---

## 4. 🧸 TODO

- [ ] 웹 UI 꾸미기 (Streamlit 레이아웃 개선)
- [ ] 사용 로그 저장 기능 추가
- [ ] 검색 연동 기능 추가 (Wikipedia / DuckDuckGo)


이 프로젝트는 공부용으로 시작된 개인 프로젝트입니다.

이슈나 PR은 언제든지 환영합니다! 😊

