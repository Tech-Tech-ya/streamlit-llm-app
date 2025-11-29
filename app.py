from dotenv import load_dotenv
import os
from langchain.chat_models  import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st
load_dotenv()

# OpenAI APIキーを取得
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI APIキーが設定されていません。環境変数を確認してください。")


st.title("サンプルアプリ: Chatアプリ")

st.write("##### ジャンルを選択して特定の領域の質問に上手に答えるアプリです。")
st.write("質問のジャンルを選択して、テキストで質問を入力してください。「実行」ボタンを押してください。")

selected_item = st.radio(
    "質問のジャンルを選択してください。",
    ["健康", "仕事"]
)

st.divider()

if selected_item == "健康":
    input_message = st.text_input(label="質問を入力してください。")

else:
    input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "健康":
        if input_message:
            try:
                llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
                messages = [
                    SystemMessage(content="あなたは健康アドバイザーです。"),
                    HumanMessage(content=input_message),
                ]
                response = llm(messages)
                st.write(f"回答: {response.content}")
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")
    else:
        if input_message:
            try:
                llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
                messages = [
                    SystemMessage(content="あなたは仕事のアシスタントです。"),
                    HumanMessage(content=input_message),
                ]
                response = llm(messages)
                st.write(f"回答: {response.content}")
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")        
        


