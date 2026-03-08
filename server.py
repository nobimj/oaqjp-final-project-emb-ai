from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")  
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")
    emotions = emotion_detector(text_to_analyze)
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
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)  
