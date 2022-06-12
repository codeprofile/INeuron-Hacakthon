import random

import time
from io import BytesIO
import zipfile
import os
from flask import Flask, render_template, request,send_file
import speech_recognition as sr
from Multilingual_Text_to_Speech.pretrained_model_multilinguial import run_model_multilinguial
from WaveRNN.pretained_model import run_model
from constants import *

app = Flask(__name__)

@app.route("/sub_dub/<language>/", methods=["POST"])
def sub_dub(language):
    try:
        if request.method == "POST":
            print(f"API call received Video Conversion to {language} language")
            language = language.upper()
            if LANGUAGE_SUPPORTED.get(language, None) is None:
                return {"message": f'Entered language {language} seems not to be supported', "status": 400}, 400
            if "file" not in request.files or not request.files["file"].filename.endswith(".wav"):
                return {"message": "Please Upload the .wav file ", "status": 400}, 400
            file = request.files["file"]
            if file:
                recognizer = sr.Recognizer()
                audioFile = sr.AudioFile(file)
                with audioFile as source:
                    data = recognizer.record(source)
                transcript = recognizer.recognize_google(data, key=None)
                speaker_no = random.Random(["00-fr", "00-de", "00-nl", "09-ru","00-zh"])
                final_transcript = transcript + speaker_no + language
                run_model_multilinguial([final_transcript])
                run_model()
                timestr = time.strftime("%Y%m%d-%H%M%S")
                fileName = "my_data_dump_{}.zip".format(timestr)
                memory_file = BytesIO()
                file_path = os.getcwd() + "\\WaveRNN" + "\\output"
                with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(file_path):
                        for file in files:
                            zipf.write(os.path.join(root, file))
                memory_file.seek(0)
                resp = {"message": "Please Check the downloads . Successfully processed the file", "status": 200}
                return send_file(memory_file,attachment_filename=fileName,as_attachment=True),200
    except Exception as e:
        return {"message" : "Something went wrong . please contact Administrator","status":500} ,500


if __name__ == "__main__":
    app.run()