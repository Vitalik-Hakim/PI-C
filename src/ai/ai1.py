import speech_recognition as sr 
import os.path
import time

filename1 = 'recs/alice/output.wav'

# create a speech recognition object
r = sr.Recognizer()

path2 = "texts"
filename4 = "Alice.txt"

# open the file
with sr.AudioFile(filename1) as source:
    # listen for the data 
    audio_data = r.record(source)
    Alice = r.recognize_google(audio_data, language = 'en-IN')
    print(Alice)
    with open(os.path.join(path2,filename4), "w") as text_file:
        text_file.write(Alice)


print("Anaylising results for Alice")
time.sleep(5)
print("Done")
time.sleep(5)
print("Anaylising results for Bob")
time.sleep(5)
filename2 = 'recs/bob/output.wav'
b = sr.Recognizer()

path1 = "texts"
filename3 = "Bob.txt"
# open the file
with sr.AudioFile(filename2) as source:
    # listen for the data 
    audio_data = b.record(source)
    # recognize (convert from speech to text)
    Bob = b.recognize_google(audio_data, language = 'en-IN')
    print(Bob)

    with open(os.path.join(path1,filename3), "w") as text_file:
        text_file.write(Bob)

