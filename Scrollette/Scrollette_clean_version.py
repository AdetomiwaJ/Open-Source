#!usr/bin/env python3
'''
    Script Name: Scrollette (Scroll + Roulette) -
    This script generates a random Bible verse.
    Author: Adetomiwa Jeminiwa
    
    
    -Phase 1: Generate random bible verse using the Book, number of chapters per book,
    number of verses per chapter.
    -Phase 2: Use a Bible API to display the Bible verse on screen.
    -Phase 3: Send bible verse as email, scheduled task.

    
'''
#Importing modules
import random


#Phase 1: Generate a random bible verse
print ("Phase 1: ")

#Declaring variables
count = 0
books_dict = {}
chap_dict = {}
books_list = []
f = open ('files/BibleBooks_Chapters.txt', 'r') #must be in the same folder as the script


#Reading the Bible books & Chapter count into a dict and list
for book in f:
    x = book.split (':')
    key = x[0]
    value = int (x[1])
    
    books_list.append(key)
    books_dict[key] = value

#Generate a random number to select bible book
book_select = random.randint(0,65)
BOD = books_list[book_select]
chapters = books_dict[BOD]


print ("Book of the day is: " + BOD)
if chapters > 1:
    print (BOD + " has " + str(chapters) + " chapters")
       
elif chapters <= 1:
    print (BOD + " has " + str(chapters) + " chapter")
        
#Search folder for Book text file
path = "files/" + BOD + ".txt"
e = open(path,'r')


chap_list = []
verse_list = []

#Reading the Book chapters and verse count into a dict
for chap in e:
    y = chap.split (':')
    key = y[0]
    value = y[1]
       
    chap_dict[key] = int(value)
    chap_list.append(key)
    verse_list.append(value)
    verses = int(value)

#Generate a random chapter

chapter = random.choice(list(chap_dict.keys())) # to select random chapter from Book
no_of_verses = chap_dict[chapter] #to find the number of verses in the chapter


verse = random.randint(1, no_of_verses) #to select a random verse


if no_of_verses > 1:
    print (BOD + " " + chapter + " has " + str(no_of_verses) + " verses!")
       
elif no_of_verses <= 1:
    print (BOD + " " + chapter + " has " + str(no_of_verses) + " verses!")



print ("Verse of the day is: " + BOD + " " + chapter + ":" + str(verse))
print ("\n")

chap_select = chapter.split()

       
#Phase 2: Display the verse on screen
import requests
print ("Phase 2: ")


#API used: https://english.api.rakuten.net/ajith/api/holy-bible/endpoints
#Sign up using the link to get api-key

url = "https://ajith-holy-bible.p.rapidapi.com/GetVerseOfaChapter"

querystring = {"Book":BOD,"chapter":str(chap_select[1]),"Verse":str(verse)}

headers = {
    'x-rapidapi-key': "api-key",
    'x-rapidapi-host': "ajith-holy-bible.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)




print ( BOD + " " + str(chap_select[1]) + ":" + str(verse))

t = response.text

#String manipulation to refine output fro Bible API
w = response.text.find('"Output"')
w = w + len("Output:") + 3
t = t[w:-2]

print (t) #Final output of Bible verse from API


'''
#Phase 3: Send bible verse to email
import smtplib
from email.message import EmailMessage
msg = EmailMessage()

VOD = str( BOD + " " + str(chap_select[1]) + ":" + str(verse))

#Compose email
email_message = 'The verse for today is ' + VOD + ' : ' + t

msg['Subject'] = email_message
msg['From'] = "sender email"
msg['To'] = "recipient email"

s = smtplib.SMTP('localhost') # How to setup sender domain IP etc: https://www.tutorialspoint.com/python/python_sending_email.htm
s.send_message(msg)
s.quit()

'''








'''



API: https://scripture.api.bible/docs
url = "https://api.scripture.api.bible/v1/bibles"

headers = {'api-key': 'api=key'}

response = requests.request("GET", url, headers=headers)

print(response.text)
'''
