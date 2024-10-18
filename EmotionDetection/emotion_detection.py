"""module posts text_to_analyse to Watson NLP Emotion Predict and returns result"""
import json
import requests


def emotion_detector(text_to_analyse):
    """takes string input (text_to_analyse),
    returns formatted post to Emotion Predict on that text from Watson NLP"""
    url = ("https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
    my_obj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = my_obj, headers=header, timeout=3)

    if response.status_code == 400:
        return {"dominant_emotion": None}

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_score = 0
    dominant_emotion = ""
    result = {}
    for emotion in emotions:
        score = emotions[emotion]
        result[emotion] = score
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion

    result["dominant_emotion"] = dominant_emotion
    return result
