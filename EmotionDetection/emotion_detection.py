import requests
import json
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 400:
        # Return all None if blank input or invalid request
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None}
    result = json.loads(response.text)
    emotion_scores = result['emotionPredictions'][0]['emotion']
    filtered_emotions = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness']}
    dominant = max(filtered_emotions, key=filtered_emotions.get)
    filtered_emotions['dominant_emotion'] = dominant
    return filtered_emotions
