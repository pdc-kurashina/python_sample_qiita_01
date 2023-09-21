# Pythonの公式イメージをベースにする
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt .
COPY app.py .
COPY templates templates/

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt
