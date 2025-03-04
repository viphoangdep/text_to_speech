from pydub import AudioSegment

def add_silent_gaps_to_audio(audio_path, output_path, gap_times, gap_duration=2):
    """
    Thêm khoảng nghỉ vào file MP3 tại các thời gian chỉ định (tính bằng giây).

    Args:
        audio_path (str): Đường dẫn tới file MP3 gốc.
        output_path (str): Đường dẫn lưu file MP3 sau chỉnh sửa.
        gap_times (list): Danh sách thời gian (giây) để thêm khoảng nghỉ.
        gap_duration (int): Thời gian khoảng nghỉ (giây). Mặc định là 2 giây.
    """
    # Load file âm thanh gốc
    audio = AudioSegment.from_file(audio_path)
    
    # Chuyển đổi thời gian từ giây sang mili giây
    gap_times_ms = [int(time * 1000) for time in sorted(gap_times)]
    gap_duration_ms = gap_duration * 1000
    
    # Tạo khoảng nghỉ
    silent_gap = AudioSegment.silent(duration=gap_duration_ms)
    
    # Thêm khoảng nghỉ vào file âm thanh
    output_audio = AudioSegment.empty()
    current_time = 0

    for gap_time_ms in gap_times_ms:
        if gap_time_ms > len(audio):
            break  # Nếu thời gian nghỉ vượt quá độ dài file, bỏ qua
        
        # Thêm phần âm thanh trước khoảng nghỉ
        output_audio += audio[current_time:gap_time_ms]
        # Thêm khoảng nghỉ
        output_audio += silent_gap
        # Cập nhật current_time đến sau khoảng nghỉ
        current_time = gap_time_ms

    # Thêm phần còn lại của file âm thanh (sau khoảng nghỉ cuối)
    output_audio += audio[current_time:]
    
    # Xuất file mới
    output_audio.export(output_path, format="mp3")
    print(f"✅ File mới đã lưu tại: {output_path}")
    print(f"🎧 Độ dài file gốc: {len(audio) // 1000}s")
    print(f"📀 Độ dài file mới: {len(output_audio) // 1000}s")

# Ví dụ sử dụng
audio_path = r"audio\VN_5minutes (mp3cut.net).mp3"
output_path = r"audio\VN_5minutes (mp3cut.net)+25.mp3"
gap_times = [5, 10, 15, 20, 25]  # Các mốc thời gian thêm khoảng nghỉ (giây)
gap_duration = 5  # Thời gian khoảng nghỉ (giây)

add_silent_gaps_to_audio(audio_path, output_path, gap_times, gap_duration)
