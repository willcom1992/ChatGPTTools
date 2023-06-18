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
        {"role": "user", "content": "ハムスターについて3行で教えて"},
        {"role": "assistant", "content": "ハムスターは小型の哺乳動物で、ペットとして飼育されることが多い。"
                                    "彼らは夜行性で、食事のほとんどは種子や果物、野菜などの植物性食物から成る。"
                                    "特定の種類のハムスターは、水がなくても生きていくことができる能力がある。"},
        {"role": "user", "content": "何故水がなくても生きていけるのですか。"},
    ],
)

# レスポンスの表示
print(response.choices[0]["message"]["content"].strip())

# 出力
# ハムスターは、稲わらなどに含まれる水分を吸収することができるため、水がなくても生きていくことができます。
# また、野生種の一部は、体内に水を貯めることができるため、水を飲む必要がなくなる場合もあります。
# しかし、ペットとして飼育される場合は、適切な水分補給が必要です。