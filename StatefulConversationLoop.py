import openai
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# OpenAI APIキーの設定
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chat_with_gpt3(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content

def main():
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": "語尾に「はむ」をつけて返答してください"},
    ]

    while True:
        print("You: ")
        user_input = input()
        if user_input.lower() == 'exit':
            break

        conversation.append({"role": "user", "content": user_input})

        # GPT-3に対して会話データを送信する
        response = chat_with_gpt3(conversation)

        # 応答からテキストを抽出して表示する
        print("AI: " + response)

        conversation.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()