from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import time
import streamlit as st

# load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#ChatOpenAI 생성
llm = ChatOpenAI(api_key=api_key,model='gpt-4o-mini')

#프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
  ("system","You are a helpful assistant."),
  ('user',"{input}")
])

# 문자열 출력파서
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

st.title("_AI 시인_  :sunglasses:")
content = st.text_input("시의 주제를 입력하세요", "가을")
st.write("시의 주제", content)

if st.button("시 작성"):
    with st.spinner("Wait for it..."):
      result = chain.invoke({'input':content +"에 대한 시를 만들어줘 "})
      st.write(result)