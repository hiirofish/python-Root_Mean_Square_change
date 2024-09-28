import os
import numpy as np
import librosa
import soundfile as sf
from tqdm import tqdm

def rms_normalize(audio_data, target_rms=0.1):
    rms = np.sqrt(np.mean(audio_data**2))
    if rms > 0:
        gain = target_rms / rms
        normalized_audio = audio_data * gain
    else:
        normalized_audio = audio_data
    return normalized_audio

def process_audio(input_path, output_path):
    try:
        audio_data, sr = librosa.load(input_path, sr=None)
        normalized_audio = rms_normalize(audio_data)
        sf.write(output_path, normalized_audio, sr)
        return True
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False

def main(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.wav'):
                # 入力ファイルのパス
                input_path = os.path.join(root, file)
                
                # 出力ディレクトリのパス（入力ディレクトリ構造を維持）
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                
                # 出力ディレクトリが存在しない場合は作成
                os.makedirs(output_subdir, exist_ok=True)
                
                # 出力ファイルのパス（'rms_' プレフィックスを追加）
                output_filename = f"rms_{file}"
                output_path = os.path.join(output_subdir, output_filename)
                
                # 音声処理を実行
                if process_audio(input_path, output_path):
                    print(f"Processed: {input_path} -> {output_path}")
                else:
                    print(f"Failed to process: {input_path}")

if __name__ == "__main__":
    input_dir = os.path.join(os.getcwd(), 'voices')
    output_dir = os.path.join(os.getcwd(), 'rms_voices')
    
    print(f"Processing audio files from {input_dir}")
    print(f"Saving normalized files to {output_dir}")
    
    main(input_dir, output_dir)
    
    print("Processing complete.")
