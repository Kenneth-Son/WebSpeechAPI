import speech_recognition as sr 
import pyttsx3 
import os

#initialized to allow python to interact with audio
r = sr.Recognizer()
 
keywords = ["exit","error"]

def record_text():
    while(1):
       try:
           with sr.Microphone() as source2:
               #prepares the recognizer for noise 
               r.adjust_for_ambient_noise(source2, duration=0.2)

               audio2 = r.listen(source2)

               MyText = r.recognize_google(audio2)

               return MyText
           
       except sr.RequestError as e:
           print(e)
       
       except sr.UnknownValueError:
           print("dun know detected")
               
    return



def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    return

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("deleted")
    else:
        print("non existent")

def check_keywords(text,keywords):
    for word in keywords:
        if word in text:
            print (f"recognized {word}")
            if word == 'exit':
                return True
    return False



try:
    while True:
        text = record_text()
        if text:
            output_text(text)
            print("wrote text")
            if check_keywords(text,keywords):
                    print("exiting")
                    raise KeyboardInterrupt
except KeyboardInterrupt:
    text = record_text()
    if text:
        output_text(text)
        print("wrote text")
        delete_file("output.txt")
    else:
        delete_file("output.txt")