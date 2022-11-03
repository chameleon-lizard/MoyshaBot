from src.translate import translate
from src.utils import send_request

def transcribe(file, token):
    ENDPOINT_URL_whisper = "https://api-inference.huggingface.co/models/openai/whisper-small"

    headers= {
        "Authorization": f"Bearer {token}",
    }

    response_whisper = send_request(ENDPOINT_URL_whisper, headers, file)
        
    return translate(response_whisper.json()["text"], token)
