#!bin/python

'''
    Script name: Wordu!
    Author: Adetomiwa Jeminiwa

    Phase 1 (Engine):Select a random word from a list of five (5) leter words
    Phase 2 (API call): Check if word exists in Oxford dictionary
    Phase 3 (The game!): Play the game!


'''

#Phase 1

import random
import json
import requests

#Declaring variables

f = open ('listofwords.txt','r')
f = f.read().splitlines()
api_key = open ('api_key.txt', 'r') #read api_key into code
api_id = open ('api_id.txt', 'r') #read api_id into code

alpha = [] #empty list for word

for a in f:
    alpha.append(a)

#function to select random word from list
def word_choice():

    word = random.choice(alpha)

    return word

#print (word_choice())

#Phase 2

app_id = str (api_id.read())
app_key = str (api_key.read())

language = "en-gb"
word_id = word_choice()

def api_call(w):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

    return r

r = api_call(word_id)


while 'error' in r.text:
    api_call(word_id)
    word_id = word_choice()
    r = api_call (word_id)
    

#Phase 3

user = input ('Do you want to play Wordu!?: ')

position = []

if user.upper() == 'Y':
    print ("Wordu! has selected the word for today!\nYou have six (6) guesses")
    count = 1

    while count < 7:
        
        input_text = 'Guess ' + str (count) + ': '
        guess = input (input_text)
        common = list(set(guess.upper()) & set(word_id.upper()))
        #common_str =

        
        if guess.upper() == word_id.upper():
            print ('Correct! The Wordu! of the day is: ' + guess)
            break
        else:

            if common:
                if guess.upper() == word_id.upper():
                    print ('Correct! The Wordu! of the day is: ' + guess)
                
                else:
                    for a in common:
                        pos = (list(word_id.upper())).index(a)
                        pos +=1
                        position.append (pos)

                    print ('Wrong! but you got "' + str (common)
                           + ' in position ' + str(position) + '" correct')
                    position = []
                
            else:
                print ("Wrong! You didn't get any letter correct")
            
            count +=1
            continue
        
    
    

print ("The Wordu! of the day is: " + word_id.upper()) 
