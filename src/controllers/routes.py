from flask import Blueprint, request, jsonify
from src.services.convert_file import convert_mp4_to_wav
from src.services.speech_to_text import transcribe_audio
convert_bp = Blueprint('convert', __name__)

@convert_bp.route('/convert', methods=['POST'])
def convert():
    # Kiểm tra nếu không có file trong request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # Kiểm tra nếu không có file được chọn
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

        # Lưu file vào thư mục upload
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    
    # Chuyển đổi âm thanh thành văn bản

    transcribed_text = transcribe_audio(wav_file_path)
    

    return jsonify({
        "message": "File processed successfully",
        "transcribed_text": transcribed_text
    })

    