import random

class Madlib:
    def menu(self):
        print('Hello, welcome to our little game during a hard working/studying time.')
        print("You may know about it, it's a Mad Lib game, so here are your options:")
        print('1. Standard stories')
        print('2. Customize your own story')
        print('3. Exit')
        
    def standard(self):
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
    
    #Work in this block is still under construction
    '''def custome(self):
        adv = input('Enter your Adverb: ')
        adj = input('Enter your Adjective: ')
        noun = input('Enter your Noun: ')
        verb = input('Enter your Verb: ')
        vehicle = input('Enter your Vehicle: ')
        color = input('Enter your Color: ')
        person = input ('Enter the person you like: ')
        food = input ('Enter your favorite Food: ')
        saying = input('Enter a Saying: ')
        stories = []
        print('Below this instruction is where you will enter your story, please follow this format:')
        print("Use {} when you want to insert something, for example: 'hello {noun}' then later on the machine will auto apply noun into that and use \ if you want to go down line")
        print("Press stop if you to stop")
        while True:
            user_story = input("Now let me hear your story: ")
            if user_story.lower() == 'stop':
                print("Okay, we'll stop here")
                break
            else:
                stories.append(user_story)'''
        
    
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
                print('This is still under construction, so sorry about it, but you can still play with my standard stories')
                if not self.keep_going():
                    break
            elif option == 3:
                print('Thank you for playing.')
                break
            
play = Madlib()
play.display()