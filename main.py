import openai
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# OpenAI APIキーの設定
openai.api_key = os.environ.get("OPENAI_API_KEY")

# チャットボットへのリクエストとレスポンス
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "ハムスターについて教えて"},
    ],
)

# レスポンスの表示
print(response.choices[0]["message"]["content"].strip())
