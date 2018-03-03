from flask import Flask, request, render_template
import speech_recognition as sr

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    with open("api-key.json") as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

    with sr.AudioFile("/static/Alcohol.mp3") as source:
        audio = r.record(source)

    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    all_text.append(text)

    print(text)

    r = sr.Recognizer()
    files = os.listdir('parts/')
    audio = ''
    text = ''

    # try:
    #     text = r.recognize_google(audio)
    #     print("you said: " + text)
    #
    #     # error occurs when google could not understand what was said
    #
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    #
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0} ".format(e))

    return render_template('index.html', name='s')


if __name__ == '__main__':
    app.run()
