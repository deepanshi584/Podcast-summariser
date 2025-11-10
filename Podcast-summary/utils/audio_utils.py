import os
import speech_recognition as sr  # type: ignore
from pydub import AudioSegment

# FFmpeg is now installed through conda and should be available system-wide
# No need to set a specific path


def extract_text_from_audio(file_path):
    """
    Converts an uploaded audio file (mp3/m4a/wav) into text using Google Speech Recognition.
    Automatically converts input to WAV format for compatibility.
    """
    try:
        # Convert any audio format to WAV
        wav_path = os.path.splitext(file_path)[0] + ".wav"
        audio = AudioSegment.from_file(file_path)
        audio.export(wav_path, format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            stt_audio = recognizer.record(source)

        text = recognizer.recognize_google(stt_audio)  # type: ignore
        os.remove(wav_path)
        return text

    except Exception as e:
        return f"❌ Error extracting text: {str(e)}"
