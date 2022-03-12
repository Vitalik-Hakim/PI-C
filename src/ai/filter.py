
from word2number import w2n
  
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


#########LAST STEPP#######################

with open("ftexts/Alice.txt", "w") as text_file:
    text_file.write(Alice)
with open("ftexts/Bob.txt", "w") as text_file:
    text_file.write(Bob)