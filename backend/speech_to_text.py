# import whisper
# model = whisper.load_model("medium")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio(r"C:\Users\Admin\Desktop\speech_to_text\backend\audio\test_1_30s.mp3")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)


import whisper

# Load mô hình
model = whisper.load_model("small")  # Có thể thay "base" bằng "tiny", "small", "medium", "large"

# Nhận dạng văn bản từ file âm thanh
result = model.transcribe(r"backend\audio\test_2_30s_vi.mp3")  # Đường dẫn tới file âm thanh
# print(result['text'])
# for segment in result['segments']:
#     start = segment['start']  # Thời gian bắt đầu
#     end = segment['end']      # Thời gian kết thúc
#     text = segment['text']    # Văn bản nhận dạng
#     print(f"[{start:.2f}s - {end:.2f}s]: {text}")

import re

def split_text_into_sentences(text):
    """
    Chia đoạn văn bản thành các câu và lưu vào một danh sách.

    Args:
        text (str): Đoạn văn bản cần chia.

    Returns:
        list: Danh sách các câu.
    """
    # Biểu thức chính quy để tách câu dựa trên các ký tự kết thúc câu phổ biến
    sentence_pattern = r'(?<=[.!?])\s+'
    
    # Sử dụng re.split để chia đoạn văn bản
    sentences = re.split(sentence_pattern, text)
    
    # Loại bỏ các khoảng trắng dư thừa xung quanh câu và bỏ các câu rỗng
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return sentences

# Ví dụ sử dụng

sentences = split_text_into_sentences(result['text'])
print(sentences)
