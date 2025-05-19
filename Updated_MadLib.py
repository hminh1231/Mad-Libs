import random

class Madlib:
    def menu(self):
        '''This function is to print out the main menu of the game'''
        print('Hello, welcome to our little game during a hard working/studying time.')
        print("You may know about it, it's a Mad Lib game, so here are your options:")
        print('1. Standard stories')
        print('2. Play with your own stories')
        print('3. Exit')
        
    def menu2(self):
        '''This function will print out the menu of custom stories for option 2'''
        print('Here are your options:')
        print('1. Add story')
        print('2. browse stories')
        print('3. Play')
        print('4. Go back')
        
    def standard(self):
        '''This function will let user play with the standard stories'''
        adv = input('Enter your Adverb: ')
        adj = input('Enter your Adjective: ')
        noun = input('Enter your Noun: ')
        verb = input('Enter your Verb: ')
        vehicle = input('Enter your Vehicle: ')
        color = input('Enter your Color: ')
        person = input ('Enter the person you like: ')
        food = input ('Enter your favorite Food: ')
        saying = input('Enter a Saying: ')
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
    
    def custome(self):
        '''This function will let user input their stories into a file and can use it to generate later'''
        stories = []
        print('Below this instruction is where you will enter your story, please follow this format:')
        print('For your choice, you only have: adv, adj, noun, verb, vehicle, color, person, food, saying')
        print("Use {} when you want to insert something, for example: 'hello {noun}' then later on the machine will auto apply noun into that and use \ if you want to go down line")
        print("Press stop if you to stop")
        while True:
            user_story = input("Now let me hear your story: ")
            if user_story.lower() == 'stop':
                print("Okay, we'll stop here")
                break
            else:
                stories.append(user_story)
        with open('user_stories.txt','a') as file:
            for i in stories:
                file.writelines(f'{i}\n')
                
    def playcustom(self):  
        '''This function will let user play their own stories'''
        print("Let's start playing with your custom stories!")
        # Collect user inputs
        word_dict = {
            'adv': input('Enter your Adverb: '),
            'adj': input('Enter your Adjective: '),
            'noun': input('Enter your Noun: '),
            'verb': input('Enter your Verb: '),
            'vehicle': input('Enter your Vehicle: '),
            'color': input('Enter your Color: '),
            'person': input('Enter the person you like: '),
            'food': input('Enter your favorite Food: '),
            'saying': input('Enter a Saying: ')
        }
        print()

        try:
            with open('user_stories.txt', 'r') as f:
                stories = f.readlines()
            if not stories:
                print("No custom stories to play.")
                return
            chosen = random.choice(stories)
            print("Here's your story:\n")
            print(chosen.format(**word_dict))  # Replace placeholders
            print()
        except FileNotFoundError:
            print("No custom stories found. Please add some first.")
            
    
    def keep_going(self):
        '''This function will decide if the user want to continue or not'''
        choice = True
        while choice:
            working = input('Do you want to continue?(Y/N): ')
            if working.lower() == 'y':
                choice = False
                return True
            elif working.lower() == 'n':
                print('Thank you for your playing')
                choice = False
                return False
            else:
                print('Your choice is invalid, please try again')
    
    def options(self):
        '''This function will get user choice input and process it'''
        while True:
            try:
                user = int(input('What is your choice numer: '))
                if user in range(1,4):
                    break
                else:
                    print('You must choose option from 1-3')
            except ValueError:
                print("Hahaha, no no no, you only need to input a number only, don't try to input anything else")
        return user
    
    def custom_options(self):
        '''This function will get user choice input for custom menu and process it'''
        while True:
            try:
                user = int(input('What is your choice numer: '))
                if user in range(1,5):
                    break
                else:
                    print('You must choose option from 1-4')
            except ValueError:
                print("Hahaha, no no no, you only need to input a number only, don't try to input anything else")
        return user
    
    def browse_stories(self):
        with open('user_stories.txt','r') as stories:
            browse = stories.read()
            for i,story in enumerate(browse,start=1):
                print(f'{i}. {story}')
    
    def custom_display(self):
        while True:
            self.menu2()
            custom_option = self.custom_options()
            if custom_option == 1:
                self.custome()
                if not self.keep_going():
                    break
            elif custom_option == 2:
                self.playcustom()
                if not self.keep_going():
                    break
            elif custom_option == 3:
                self.browse_stories()
            else:
                break
    
    def display(self):
        '''This function will display everything and ask if user want to continue or not'''
        while True:
            self.menu()
            option = self.options()
            if option == 1:
                self.standard()
                if not self.keep_going():
                    break
            elif option == 2:
                self.custom_display()
            elif option == 3:
                print('Thank you for playing.')
                break
            
play = Madlib()
play.display()
