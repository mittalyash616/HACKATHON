import speech_recognition as sr

def takecommand():
    command = sr.Recognizer()
    query = None
    while query is None:
        with sr.Microphone() as source:
            print("Listening...")
            command.adjust_for_ambient_noise(source)
            command.pause_threshold = 1
            audio = command.listen(source)
            print("Recognizing...")
            try:
                query = command.recognize_google(audio, language="en-in")
                print(f"User said: {query.capitalize()}")
                query = query.lower()
            except sr.UnknownValueError:
                print("Voice too low. Please try again")
                query = None
            except sr.RequestError:
                print("Internet Problem. Please try again") 
                query = None  
    return query 

content = takecommand()

print(content)

