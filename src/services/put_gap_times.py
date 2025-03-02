from pydub import AudioSegment

def add_silent_gaps_to_audio(audio_path, output_path, gap_times, gap_duration=2):
    """
    Thêm khoảng nghỉ vào file MP3 tại các thời gian chỉ định (tính bằng giây).

    Args:
        audio_path (str): Đường dẫn tới file MP3 gốc.
        output_path (str): Đường dẫn lưu file MP3 sau chỉnh sửa.
        gap_times (list): Danh sách thời gian (giây) để thêm khoảng nghỉ.
        gap_duration (int): Thời gian khoảng nghỉ (giây). Mặc định là 1 giây.
    """
    # Load file âm thanh gốc
    audio = AudioSegment.from_file(audio_path)
    
    # Chuyển đổi gap_times sang mili giây
    gap_times_ms = [int(time * 1000) for time in sorted(gap_times)]
    gap_duration_ms = gap_duration * 1000  # Thời gian khoảng nghỉ (ms)
    
    # Tạo khoảng nghỉ
    silent_gap = AudioSegment.silent(duration=gap_duration_ms)
    
    # Thêm các khoảng nghỉ vào file âm thanh
    output_audio = AudioSegment.empty()
    current_time = 0

    for gap_time_ms in gap_times_ms:
        # Thêm đoạn âm thanh từ vị trí hiện tại đến vị trí khoảng nghỉ
        output_audio += audio[current_time:gap_time_ms]
        # Thêm khoảng nghỉ
        output_audio += silent_gap
        # Cập nhật thời gian hiện tại
        current_time = gap_time_ms

    # Thêm phần còn lại của file âm thanh
    output_audio += audio[current_time:]
    
    # Lưu file âm thanh sau khi chỉnh sửa
    output_audio.export(output_path, format="mp3")
    print(f"File âm thanh với khoảng nghỉ đã được lưu tại: {output_path}")

# # Ví dụ sử dụng:
# audio_path = r"backend\audio\test_1_30s_en.mp3"   # Đường dẫn file MP3 gốc
# output_path = r"backend\audio\test_1_36s_en.mp3" # Đường dẫn file MP3 sau khi thêm khoảng nghỉ
# gap_times = [5, 10, 15]          # Thời gian thêm khoảng nghỉ (tính bằng giây)
# gap_duration = 1                 # Thời gian khoảng nghỉ (giây)

# add_silent_gaps_to_audio(audio_path, output_path, gap_times, gap_duration)
