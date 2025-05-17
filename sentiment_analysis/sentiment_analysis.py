from transformers import pipeline

# 感情分析モデルの初期化
sentiment_analyzer = pipeline("sentiment-analysis")

# ユーザー入力を受け取る
print("感情を分析したいテキストを入力してください（例：I love this movie!）")
text = input("> ")

# 感情分析を実行
result = sentiment_analyzer(text)

# 結果を表示
label = result[0]['label']
score = result[0]['score']
print(f"感情: {label} (確信度: {score:.2%})")
