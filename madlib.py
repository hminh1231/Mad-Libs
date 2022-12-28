import random
print('Welcome to madlib game:')
print('1. Start \n2. Exit game')
choice = int(input("What's your choice (Please enter number): "))
print('')
while choice == 1:
    adv = input('Adverb: ')
    adj = input('Adjective: ')
    noun = input('Noun: ')
    verb = input('Verb: ')
    vehicle = input('Vehicle: ')
    color = input('Color: ')
    person = input ('Person you like: ')
    food = input ('Food: ')
    saying = input('Saying: ')
    print('')
    madlib1 = f"Today I went to my favorite restaurant called the {adv} {noun}, unlike most food stands, \
they cook and prepare food in {vehicle}. The best thing on the menu is the {color} {person}. Instead of ground beef \
they fill the food with {food}. If that doesn't make your mouth water, then it' just like {person} say: {saying} "
    madlib2 = f"I was so {adv} today because yesterday when I {verb} my {adj} {food}, it was so {adv}. Then {person} \
told me that: {saying}. Then I went out and {verb} my {color} {vehicle} that I just bought at {noun}. That's why \
I'm {adv} today."
    madstory = [madlib1, madlib2]
    print(random.choice(madstory))
    print('')
    choice = int(input('Do you want to continue? \n1. Yes \n2. No \nWhat is your choice (Please select number:)'))
    
