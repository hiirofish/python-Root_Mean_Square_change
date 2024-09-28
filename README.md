# 音声RMSノーマライゼーションツール

## 概要

このツールは、音声ファイルのRMS（Root Mean Square）ノーマライゼーションを行い、オプションで音声の冒頭をトリミングする機能を提供します。

RMSノーマライゼーションとは、音声の平均的な音量レベルを一定の値に調整する処理です。これにより、異なる音源間の音量差を軽減し、全体的に一貫した音量レベルを実現します。

## 機能

1. RMSノーマライゼーション（Python スクリプト）
   - WAVファイルのRMSレベルを調整
   - ディレクトリ構造を維持しながら処理
   - 処理済みファイルに 'rms_' プレフィックスを追加

2. 音声トリミング（シェルスクリプト、オプション）
   - 音声ファイルの冒頭の指定秒数を削除

## 必要条件

- Python 3.6以上
- 必要なPythonライブラリ：numpy, librosa, soundfile, tqdm
- sox（音声トリミング用、オプション）

## インストール

1. このリポジトリをクローンまたはダウンロードします。
2. 必要なPythonライブラリをインストールします：

```bash
pip install numpy librosa soundfile tqdm
```

3. （オプション）soxをインストールします（音声トリミング用）。

## 使用方法

### 1. RMSノーマライゼーション

1. `Root_Mean_Square_change.py` を音声ファイルがある親ディレクトリに配置します。
2. 以下のコマンドで実行します：

```bash
python Root_Mean_Square_change.py
```

デフォルトでは：
- 入力：カレントディレクトリの 'voices' フォルダ
- 出力：カレントディレクトリの 'rms_voices' フォルダ

入力/出力ディレクトリを変更するには、スクリプト内の以下の行を編集します：

```python
input_dir = os.path.join(os.getcwd(), 'voices')
output_dir = os.path.join(os.getcwd(), 'rms_voices')
```

### 2. 音声トリミング（オプション）

1. `trim_audio.sh` に実行権限を付与します：

```bash
chmod +x trim_audio.sh
```

2. 以下のコマンドで実行します：

```bash
./trim_audio.sh
```

デフォルトでは：
- 入力：'./rms_voices' ディレクトリ
- 出力：'./trimmed_rms_voices' ディレクトリ
- トリム時間：冒頭0.1秒

設定を変更するには、スクリプト内の以下の行を編集します：

```bash
INPUT_DIR="./rms_voices"
OUTPUT_DIR="./trimmed_rms_voices"
sox "$file" "$output_file" trim 0.1  # 0.1を希望の秒数に変更
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルを参照してください。

## 注意事項

- 処理前に元のファイルのバックアップを取ることをおすすめします。
- トリミング時間を変更する際は、音声内容を考慮して適切な値を設定してください。

## サポート

問題や提案がある場合は、GitHubのIssueを開いてください。

---

作成者：[あなたの名前]
