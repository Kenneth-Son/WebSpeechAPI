import speech_recognition as sr 
import pyttsx3 
import os

#initialized to allow python to interact with audio
r = sr.Recognizer()
 
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
try:
    while True:
        text = record_text()
        output_text(text)
        print("wrote text")
except KeyboardInterrupt:
    delete_file("output.txt")