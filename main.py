from webbrowser import get, open_new
from time import sleep
import pyautogui as pag
import random as rd
import string as str

def generate_random_sequence():
    '''
    Generates a random word to be searched in Bing.
    '''
    # Define the set of characters tKPd&RvzwZ]
    # o use: letters, digits, and punctuation
    characters = str.ascii_letters + str.digits + str.punctuation
    # Generate a random 10-character sequence
    sequence = ''.join(rd.choice(characters) for _ in range(10))
    return sequence

def search(searchNum):
    '''
    Repeats the search for the specified number of times.
    '''
    for x in range(1, searchNum):
        print('Executing search.')
        pag.click(310, 113)
        pag.hotkey('ctrl', 'a')  # Selects all text
        pag.press('backspace')  # Clears the last search
        pag.typewrite(generate_random_sequence())  # Types a new random word
        pag.press('enter')  # Presses enter to search
        sleep(7)  # Waits 7 seconds for the next search

# AFTER YOU CLICK RUN, DO NOT MOVE YOUR MOUSE!

# Number of searches to execute
searchRepeats = int(input('How many searches do you want to execute? '))

# Change the path to msedge.exe on your computer
# If you're on Windows, the current path should work
# This command should open Edge and navigate to the Bing page
get(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe').open_new('https://www.bing.com/')

sleep(7)  # Allows time for the page to load

# Clicks on the search bar and types a random word
pag.click(874, 286)
pag.typewrite(generate_random_sequence())
pag.press('enter')
sleep(7)  # Waits 7 seconds for the next search

# Does the searching after first search
search(searchRepeats)

# Signals that the script has finished by showing a message in the search bar
pag.click(310, 113)
pag.hotkey('ctrl', 'a')
pag.press('backspace')
pag.typewrite('Done! Closing browser...')
sleep(5)  # Pauses for 5 seconds
pag.hotkey('ctrl', 'w')  # Closes the browser
