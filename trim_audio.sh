#!/bin/bash

# 入力ディレクトリ
INPUT_DIR="./rms_voices"
# 出力ディレクトリ
OUTPUT_DIR="./trimmed_rms_voices"

# 出力ディレクトリが存在しない場合は作成
mkdir -p "$OUTPUT_DIR"

# 入力ディレクトリ内のすべてのWAVファイルを処理
find "$INPUT_DIR" -type f -name "*.wav" | while read -r file; do
    # 相対パスを維持しつつ、出力ファイルのパスを作成
    rel_path="${file#$INPUT_DIR/}"
    output_file="$OUTPUT_DIR/${rel_path}"

    # 出力ファイルのディレクトリが存在しない場合は作成
    mkdir -p "$(dirname "$output_file")"

    # soxコマンドを実行
    sox "$file" "$output_file" trim 0.2

    echo "Processed: $file -> $output_file"
done

echo "All files have been processed."
