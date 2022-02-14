'''
    Script Name: Valentine Flames GUI
    Author: Adetomiwa Jeminiwa

    FLAMES is a popular game named after the acronym:
    Friends, Lovers, Admirers, Marriage, Enemies, Situationship.
    This game does not accurately predict whether or
    not an individual is right for you,
    but it can be fun to play this with your friends


   | F | L | A | M | E | S |
   | 1 | 2 | 3 | 4 | 5 | 6 |
     6   7   8   8 | 9 | 10|
     11  12  13  14| 15| 16|
     17  18  19  20| 21| 22|
     23  24  25  26| 27| 28|

    F = 1,6,11,17,23
    L = 2,7,12,18,24
    A = 3,8,13,19,25
    M = 4,9,14,20,26
    E = 5,10,15,21,27
    S = 6,11,16,22,28

    GUI reqs:
    - Two (2) Labels
    - Two (2) text fields for the names
    - Two (2) buttons (submit & exit)

    Logic:
    -User inputs both names.
    -On submit_button click
        -Names are assigned to variable and passed to engine.
        -Engine processes and returns result.
        -Result is displayed in a label.
        -Text field is cleared
'''

#imports

import kivy
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder

class MainLayout(GridLayout):
    #Initialize keywords
    '''def __init__(self, **kwargs):

        super (MainLayout, self).__init__(**kwargs)
        '''

    def do_action(self,instance):
        #Variables for widgets

        name = self.ids.name.text
        other_name = self.ids.other_name.text

        self.ids.Display_label.text = 'Result for '+ str(name) + 'and' + str(other_name)

        self.result_label.text = engine (name, other_name)

        self.ids.name.text = ''
        self.ids.other_name.text =''
    
    def engine(a,b):

        Name = a.split()

        Name = Name[0] + Name[1]
        
        Other_Name = b.split()

        Other_Name = Other_Name[0] + Other_Name[1]

        All_Names = Name.upper() + Other_Name.upper()

        unique_name = ''.join(set(All_Names)) # variable to store unique letters from both names

        size = len(unique_name)
        
        F = [1,6,11,17,23]
        L = [2,7,12,18,24]
        A = [3,8,13,19,25]
        M = [4,9,14,20,26]
        E = [5,10,15,21,27]
        S = [6,11,16,22,28]

        #big IF statements

        if size in F:
            return ('You are FRIENDS!')
        elif size in L:
            return ('You are LOVERS!')
        elif size in A:
            return ('You are ADMIRERS!')
        elif size in M:
            return ('You should be MARRIED!')
        elif size in E:
            return ('Run! You are ENEMIES!')
        elif size in S:
            return ('You are in a SITUATIONSHIP!')

class FLAMES(App):

    def do_action(self,instance):
        #Variables for widgets

        name = self.ids.name.text
        other_name = self.ids.other_name.text

        self.ids.Display_label.text = 'Result for '+ str(name) + 'and' + str(other_name)

        self.result_label.text = engine (name, other_name)

        self.ids.name.text = ''
        self.ids.other_name.text =''

    def build(self):

        return Builder.load_file('FLAMES.kv')

if __name__ == '__main__':
    FLAMES().run()

        
