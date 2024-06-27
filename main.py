import speech_recognition as sr
import pyttsx3
import webbrowser
import pyjokes
import pywhatkit as kit

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    print(command)
    parts = command.split(" ")
    response="I can play your favourite songs, or open different sites, or tell a joke"
    if "open" in parts:
        open_index = parts.index("open")
        if open_index + 1 < len(parts):
            site = parts[open_index + 1]
            response=f"Sure! opening {site}"
            webbrowser.open(f"https://{site}.com")
    elif("joke" in command):
        response=f"Sure ! {pyjokes.get_joke()}"
    
    elif "play" in parts:
        play_index = parts.index("play")
        if play_index + 1 < len(parts):
            song = " ".join(parts[play_index + 1:])
            song = song.replace("me", "").strip()
            song = song.replace("for", "").strip()
            response = f"Sure! Playing {song}"
            # if "Spotify" in parts:
            #     song = song.replace("on spotify", "").strip()
            #     kit.playonspotify(song)
            # else:
            song = song.replace("on youtube", "").strip()
            kit.playonyt(song)
    elif "hi jarvis" in command.lower():
        response="Hi, Sandesh how may i help you today?"
    speak(response)


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        #This is to listen only for the wake word of JARVIS        
        
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,phrase_time_limit=2)
            print("Processing...")
            
            word = r.recognize_google(audio)
            print("You said: " + word)

            if ("jarvis" in word.lower()):
                speak("Ya..")

                #This is finally to give command once the wake word is provided
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                    command=r.recognize_google(audio)

                if command == "shutdown":
                    speak("Shutting down")
                    break
                else:
                    processCommand(command)

        except Exception as e:
            print(f"An error occurred: {e}")
