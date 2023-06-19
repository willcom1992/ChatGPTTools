import openai
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()
# OpenAI APIキーの設定
openai.api_key = os.environ.get("OPENAI_API_KEY")


def chat_with_ai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

conversation = [
    {"role": "system", "content": "語尾に「はむ」をつけて返答してください"},
    {"role": "system", "content": "あなたの名前は「ライト」という名前の犬という設定で会話をしてください。"},
]

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    conversation.append({"role": "user", "content": user_input})
    response = chat_with_ai(conversation)
    print("Bot: " + response)
    conversation.append({"role": "assistant", "content": response})
