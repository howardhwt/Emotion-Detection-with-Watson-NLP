import requests  # Import the requests library to handle HTTP requests
import json


def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emeotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj,headers=headers)  # Send a POST request to the API with the text and headers

    if (response.status_code == 200):
        # Formatting the response in json format
        formatted_response = json.loads(response.text)
        # Initialize
        emotions = None
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Storing the emotions and their values
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        # Finding the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # returning the required output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    if (response.status_code == 400):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return ("Invalid text! Please try again!")
