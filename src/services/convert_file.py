import os
from pydub import AudioSegment
from moviepy import VideoFileClip



def convert_mp4_to_wav(input_file, output_file=None):
    # Kiểm tra file đầu vào có tồn tại không
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found.")
    
    # Nếu không có tên file đầu ra, đổi đuôi thành .wav
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".wav"

    # Load video và trích xuất audio
    video = VideoFileClip(input_file)
    audio = video.audio

    # Lưu audio dưới dạng WAV
    audio.write_audiofile(output_file, codec='pcm_s16le')

    # Đóng file
    audio.close()
    video.close()

    print(f"Converted '{input_file}' to '{output_file}'")

    return output_file

