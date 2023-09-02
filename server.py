from flask import Flask, render_template, request # This is different from requests
from MyTranslator import translate_text
import SpeechTranslator_my as st
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():    
    return render_template("/index.html")

@app.route("/getData")
def get_data():    
    op = request.args.get("operation") # Select operation   
    source_text = request.args.get("source_text") # Source text given by the user for translation
    target_lang = request.args.get("target_language") # Target language selected by the user

    if op == "S2ST" and bool(target_lang): # Speech To Speech Translation
        source_text = st.takeinput()

        audio_trans_text = translate_text(source_text, target_lang)

        audio_translation = st.speak(audio_trans_text)
        audio_translation
        return render_template("index.html")
    
    elif op == "S2TT" and bool(target_lang): # Speech To Text Translation
        source_text = st.takeinput()
        tran_text = translate_text(source_text, target_lang)
        return render_template("index.html",
                               translated_text = tran_text)       
    
    elif op == "T2ST" and bool(target_lang): # Text To Speech Translation

        tran_text = translate_text(source_text, target_lang)
        audio_translation = st.speak(tran_text)
        audio_translation
        return render_template("index.html",
                               translated_text = tran_text)
    
    elif (op == "T2TT" and bool(target_lang)) and bool(source_text.strip()): # Text To Text Translation
        tran_text = translate_text(source_text, target_lang)
        return render_template("index.html",
                               translated_text = tran_text)
    elif op == "ASR":
        return f"{op} Under Construction"

    else:
        return render_template ("index.html",
                                 translated_text = 'Provide "Operation"/"Target Language"/"Text"')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port = 8000) # code for run on local machine
    # serve(app, host="0.0.0.0", port=8000) # code for run in production server