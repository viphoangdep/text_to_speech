import whisper
import os
from convert_file import convert_mp4_to_wav
def transcribe_audio(input_path: str, model_size: str = "medium", no_speech_threshold: float = 0.6) -> str:
    """
    Chuyển đổi âm thanh thành văn bản sử dụng mô hình Whisper và lưu kết quả vào file .txt.

    Args:
        input_path (str): Đường dẫn đến file âm thanh (mp3, wav, ...).
        model_size (str): Kích thước mô hình Whisper (tiny, small, medium, large).
        no_speech_threshold (float): Ngưỡng để xác định đoạn không có giọng nói.

    Returns:
        str: Đường dẫn đến file .txt chứa kết quả phiên âm.
    """
    # Load mô hình Whisper
    model = whisper.load_model(model_size)
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File '{input_path}' không tồn tại.")
    ext = os.path.splitext(input_path)[1].lower()
    if ext not in ['.wav', '.mp4','.mp3']:
        raise ValueError(f"Unsupported file format: {ext}. Only .wav, .mp4, and .mp3 files are supported.")
    if ext == '.mp4':
        # Chuyển đổi file mp4 thành wav
        input_path = convert_mp4_to_wav(file_path)
    # Kiểm tra file tồn tại
    

    # Nhận dạng văn bản từ file âm thanh
    result = model.transcribe(
        audio=input_path,
        verbose=False,
        no_speech_threshold=no_speech_threshold,
        # word_timestamps= True,
    )
    print(result['text'])

    # Tạo tên file đầu ra (thay đuôi bằng .txt)
    output_path = f"{os.path.splitext(input_path)[0]}.txt"

    # Ghi kết quả vào file .txt
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(f"Language: {result['language']}\n\n")
        for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text']
            file.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")

    print(f"Kết quả đã được lưu vào: {output_path}")
    return True

transcribe_audio(r"audio\VN_5minutes (mp3cut.net).mp3")