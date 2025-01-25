import pyttsx3
import string
# from yapper import Yapper

voiceoverDir = "voiceovers"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def create_voice_over(filename, rawText):
    translator = str.maketrans('', '', string.punctuation) 
    text = rawText.translate(translator)
    filePath=f"{voiceoverDir}/{filename}.wav"
    engine.setProperty('rate', 160)
    engine.setProperty('voice', voices[2].id)
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return(filePath)