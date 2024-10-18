"""main web app for emotion detection"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/")
def render_index():
    """main route"""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():
    """emotion detection handling"""
    text_to_analyze = request.args.get('textToAnalyze')
    results = emotion_detector(text_to_analyze)

    dominant_emotion = results["dominant_emotion"]

    if dominant_emotion is None:
        return "<b>Invalid text! \n Please try again! </b>"

    response = "For the given statement, the system response is "

    for key, value in results.items():
        if key != "dominant_emotion":
            response += "'" + key + "': " + str(value) + ", "

    response = response[:len(response) - 2]

    response += f". The dominant emotion is <b>{dominant_emotion}</b>."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
