''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector as ED

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the label and its confidence 
        score for the provided text.'''
    text_to_analyse = request.args.get("textToAnalyze", "")

    response = ED(text_to_analyse)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is \
        'anger': {anger_score}, \
        'disgust': {disgust_score}, \
        'fear': {fear_score}, \
        'joy': {joy_score} and \
        'sadness': {sadness_score}. \
        The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
