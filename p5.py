import speech_recognition as sr
import pyttsx3
import google.generativeai as genai  

genai.configure(api_key="AIzaSyDnX7pNCRYb26WMoj9wqK-V2nPqQnwAvj8")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
        return None

def generate_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Error:", e)
        return "Sorry, I am unable to generate a response right now."

def ai_assistant():
    user_input = recognize_speech()
    if user_input:
        ai_response = generate_response(user_input)
        print("AI:", ai_response)
        speak(ai_response)

# Run the AI assistant
ai_assistant()
