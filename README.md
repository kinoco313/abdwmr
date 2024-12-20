# Analyzing Baseball Data with Marimo Recommended

## 環境構築
1. uv をインストール
2. `uv init hoge` でプロジェクトを作成し、hoge ディレクトリに移動
3. `uv add marimo[recommended]` で marimo をインストール

### marimo[recommended]とは？
marimo[recommended]は、marimoに加え、以下のパッケージを追加でインストールする
- duckdb: 高速で軽量なカラムストア型データベース
- altair: 宣言的な統計可視化ライブラリ
- polars: 高速なデータフレームライブラリ
- openai: OpenAIのAPIを利用するためのライブラリ
- ruff: Pythonのコード品質ツール
  
基本的に上記のライブラリを利用して、分析を行う