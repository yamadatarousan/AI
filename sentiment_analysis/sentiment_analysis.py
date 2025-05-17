from transformers import pipeline

# モデルを指定
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# ユーザー入力
print("感情を分析したい日本語テキストを入力してください（例：この映画最高！）")
text = input("> ")

# 感情分析
result = sentiment_analyzer(text)

# 結果を解釈
score = int(result[0]['label'].split()[0])
if score >= 4:
    label = "ポジティブ"
elif score <= 2:
    label = "ネガティブ"
else:
    label = "中立"
confidence = result[0]['score']
print(f"感情: {label} (確信度: {confidence:.2%})")
