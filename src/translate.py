from src.utils import send_request

def translate(text, token):
    ENDPOINT_URL_opus = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"

    headers= {
        "Authorization": f"Bearer {token}",
    }

    response_opus = send_request(ENDPOINT_URL_opus, headers, text)
        
    return response_opus.json()[0]["translation_text"]
