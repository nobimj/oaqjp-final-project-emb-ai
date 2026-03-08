'''
This is the server module for the flask emotion detection application
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    '''
    Calls the emotion dection function from the Emotion Detection package
    '''
    text_to_analyze = request.args.get("textToAnalyze", "")
    emotions = emotion_detector(text_to_analyze)
    dominant = emotions['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!"
    formatted_str = f"For the given statement, the system response is " \
                f"'anger': {emotions['anger']}, " \
                f"'disgust': {emotions['disgust']}, " \
                f"'fear': {emotions['fear']}, " \
                f"'joy': {emotions['joy']}, " \
                f"'sadness': {emotions['sadness']}. " \
                f"The dominant emotion is {dominant}."
    return formatted_str
@app.route("/")
def render_index_page():
    '''
    Returns the home page of the application
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
