####################### IMPORTS###################

#for record
import pyaudio
import wave
import os
import time

#for AI1
import speech_recognition as sr 
import os.path
#import time

#for app
import sys
from pi import *
import pyttsx3

###R######## short squeeze for Spich :) #########
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
######## short squeeze #########ecord######

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 10
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

SpeakText('Recording Starting for Alice...')
print('Recording Starting for Alice...')
time.sleep(1)
SpeakText('GO!!!')
print("Goo!!!")
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

SpeakText('Finished recording')
print('Finished recording')
path = 'recs/alice'
# Save the recorded data as a WAV file
wf = wave.open(os.path.join(path,filename), 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

#######################RECORDING DONE FOR ALICE#######################################
SpeakText('Analysing audio for Alice')
print("Analysing audio for Alice")
time.sleep(1)
print("Doneeee")
time.sleep(1)

p = pyaudio.PyAudio()  # Create an interface to PortAudio

SpeakText('Recording Starting for Bob...')
print('Recording Starting for Bob...')
time.sleep(1)
SpeakText('Goo!!')
print("Goo!!!")
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()
SpeakText("Finished recording")
print('Finished recording')
path = 'recs/bob'
# Save the recorded data as a WAV file
wf = wave.open(os.path.join(path,filename), 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

SpeakText("Done!")
print("Done!")



##################SESSION DONE#############


###################### AI1##################

filename1 = 'recs/alice/output.wav'

# create a speech recognition object
r = sr.Recognizer()

path2 = "texts"
filename4 = "Alice.txt"

# open the file
with sr.AudioFile(filename1) as source:
    # listen for the data 
    audio_data = r.record(source)
    r.adjust_for_ambient_noise(source, duration=0.2)
    Alice = r.recognize_google(audio_data, language = 'en-IN')
    print(Alice)
    with open(os.path.join(path2,filename4), "w") as text_file:
        text_file.write(Alice)

SpeakText("Analysing results for Alice")
print("Analysing results for Alice")
time.sleep(1)
print("Done")
time.sleep(1)
SpeakText("Analysing results for Bob")
print("Analysing results for Bob")
time.sleep(1)
filename2 = 'recs/bob/output.wav'
b = sr.Recognizer()

path1 = "texts"
filename3 = "Bob.txt"
# open the file
with sr.AudioFile(filename2) as source:
    # listen for the data 
    audio_data = b.record(source)
    # recognize (convert from speech to text)
    b.adjust_for_ambient_noise(source, duration=0.2)
    Bob = b.recognize_google(audio_data, language = 'en-IN')
    print(Bob)

    with open(os.path.join(path1,filename3), "w") as text_file:
        text_file.write(Bob)

##########################SESSION 2 ENDED#################################

###################Filter######################
  
num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0' : '0',
    'One': '1',
    'Two': '2',
    'Three': '3',
    'Four': '4',
    'Five': '5',
    'Six': '6',
    'Seven': '7',
    'Eight': '8',
    'Nine': '9',
    'Zero' : '0',
    '.' : '.',
    'point':'.',
    'points':'.',
    'prints':'.'
}

with open ("texts/Alice.txt", "r") as file:
    Alice = file.read().replace('\n', '')
    Alice = Alice.replace(""," ")

with open ("texts/Bob.txt", "r") as file:
    Bob = file.read().replace('\n', '')
    Bob = Bob.replace(""," ")

  

  
# Convert numeric words to numbers
# Using join() + split()
Alice = ''.join(num_dict[ele] for ele in Alice.split())
Bob = ''.join(num_dict[ele] for ele in Bob.split())



with open("ftexts/Alice.txt", "w") as text_file:
    text_file.write(Alice)
with open("ftexts/Bob.txt", "w") as text_file:
    text_file.write(Bob)

#########SESSION 3 ENDED#######################

######### App ####################
with open ("ftexts/Alice.txt", "r") as file:
    Alice = file.read().replace('\n', '')

with open ("ftexts/Bob.txt", "r") as file:
    Bob = file.read().replace('\n', '')

bob = Bob
alice = Alice

SpeakText("Player one name:")
user1 = input("Player one name: ")
SpeakText("Player two name:")
user2 = input("Player two name: ")


#alice = input("{} Say the pi you know: ".format(user1))
#bob = input("{} Say the pi you know: ".format(user2))

alist = list(alice)
blist = list(bob)

lenA  = len(alist)
lenB  = len(blist)


#Verify order or pi numbers




#Alice verify
for pis in range(lenA):
    global correct1
    if pi_100[0:lenA] == alice:
        pass
        correct1 = True
    else:
        SpeakText("{} is incorrect! :(\n".format(user1))
        print("{} is incorrect! :(\n".format(user1))
        correct1 = False
        break

#Bob verify
for pis in range(lenB):
    global correct2
    if pi_100[0:lenB] == bob:
        correct2 = True
        pass
    else:
        print("{} is incorrect! :(\n".format(user2))
        print("{} is incorrect! :(\n".format(user2))
        correct2 = False
        break


if correct1 == False and correct2 == False:
    print("You both suck! nyeh")
    SpeakText("You both suck! nyeh")
    sys.exit()
elif correct1 == True and correct2 == False:
    Winner = "{} is the winner!".format(user1)
    print(Winner)
    SpeakText(Winner)
    sys.exit()
elif correct2 == True and correct1 == False:
    Winner = "{} is the winner!".format(user2)
    print(Winner)
    SpeakText(Winner)
    sys.exit()
else:
    pass

############ Say the results madam #################

#If they cross this line then its time for lenEval

if len(alice) > len(bob):
    Winner = "{} is the winner!".format(user1)
    print(Winner)
    SpeakText(Winner)
elif len(bob) > len(alice):
    Winner = "{} is the winner!".format(user2)
    print(Winner)
    SpeakText(Winner)
else:
    print("Its a tie between {} and {}".format(user1,user2))
    SpeakText(("Its a tie between {} and {}".format(user1,user2)))


############################################# THE END ################################################################
