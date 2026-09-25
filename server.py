from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection():
    text_to_analyse = request.args.get("textToAnalyze")

    if not text_to_analyse:
        return "Invalid input! Please enter a sentence."

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid input! Please enter a valid sentence."

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
