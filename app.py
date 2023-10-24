
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key
openai.api_type = "azure"
openai.api_base = "https://subzemi-ins1.openai.azure.com/"
openai.api_version = "2023-07-01-preview"

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an excellent AI professor that helps student find information."}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        engine="subzemi",
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去



st.title("👯‍♀️AI  Chikuda teacher😈")

st.write("ChatBot based on ChatGPT3-5")

user_input = st.text_input("Enter message!", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🙋(You)"
        if message["role"]=="assistant":
            speaker="👨(teacher)"

        st.write(speaker + ": 　" + message["content"])
st.image("university_chuo-main.png")
