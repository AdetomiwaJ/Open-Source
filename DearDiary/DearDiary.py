#!bin/python3

'''
    Script name: DearDiary.py
    Author: Adetomiwa Jeminiwa

    UI requirements:
    - A Layout/canvas
    - A multiline text field
    - Buttons
    - Labels
    - Calendar widget

'''

#Imports and variables

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import os


import datetime


#Create text file
dt = datetime.datetime.now()

folder = 'Diary Entries'

try:
    os.mkdir(folder)

except FileExistsError:
    print ('Folder/Directory exists!')

filename = str(folder) + "/Diary entry for " + str (dt) + ".txt"

f = open (filename, 'a')



class MainLayout(FloatLayout):
    #Initialize keywords
    def __init__(self, **kwargs):

        super (MainLayout, self).__init__(**kwargs)

        #self.cols = 1 #Number of columns in grid
        
        #Adding widgets

        
        self.Entry = TextInput (multiline = True)
        self.add_widget(self.Entry)
        
        
        self.New_Entry = Button(text = "New Entry", size_hint_y = None, height = 30,
                              size_hint_x = None, width = 150, pos_hint = {'left': 1})
        self.New_Entry.bind(on_press = self.entry_press)
        self.add_widget(self.New_Entry)
        
        self.Exit = Button(text = "Exit", size_hint_y = None, height = 30,
                              size_hint_x = None, width = 150, pos_hint = {'right': 1})
        self.Exit.bind(on_press = self.exit_press)
        self.add_widget(self.Exit)

        
            
    def entry_press(self, instance):
        Entry = self.Entry.text
        f.write (Entry)
        #f.close()
        
        self.Entry.text = ''
      
    def exit_press(self, instance):
        quit()


class DearDiary(App):

    def build(self):

        return MainLayout()

        

DearDiary().run()

