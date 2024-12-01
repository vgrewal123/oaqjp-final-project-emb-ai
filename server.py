''' Dosctring for flask server
    '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector", methods = ['GET'])
def sent_detector():
    ''' This code receives the text from the HTML interface.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    output = emotion_detector(text_to_analyze)

    anger = output['anger']
    disgust = output['disgust']
    fear = output['fear']
    joy = output['joy']
    sadness = output['sadness']
    dominant_emotion = output['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
    f"For the given statement, the system response is 'anger': {anger},"
    f" 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and"
    f" 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
