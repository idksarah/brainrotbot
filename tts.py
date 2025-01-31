import pyttsx3
import string

voiceoverDir = "voiceovers"

# creates a tts file for given input

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

create_voice_over("hello there", "what is up")

#this is the tts script. its imported in main.py to create new .wavs for each new comment, but this is just a test. 