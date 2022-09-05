import random


class Creatures:
    def __init__(self, name):
        self.name = name


pirates = Creatures('pirates')
cave_creepers = Creatures('cave creepers')
werewolf_pack = Creatures('werewolf_pack')


class Bosses:
    def __init__(self, name):
        self.name = name


Archy = Bosses('Archy The Pirate Captain')
Lex = Bosses('Lex The Disfigured')
Soren = Bosses('Soren The Pack Leader')


will = None

outcome_1 = random.randint(1,10)
outcome_2 = random.randint(1,10)


name = input('Enter your name adventurer! ')
print(f'Welcome {name}, to the quest of a liftetime!')
start = input(f'Will you accept the task the king has bestowed upon you? (yes/no) ').lower()
if start == "yes" or start == "y":
    print('Great! your task is to find the location of the beast who has kidnapped the princess.')
    choice = input(f'Where will you begin your search my good man or women? (forest, caves, or the seaport?) ').lower()
    if choice == 'forest':
        choice_1 = input(f'''
            After leaving the castle gates, you venture towards the direction of the Forest.
            With the information that was given to you, you stumble upon an old farm house surrounded by dead crops.
            After drawing closer, from out of nowhere a werewolf ambushes you!!
            Will you fight or withdraw?
            ''').lower()
        if choice_1 == 'fight':
            choices = ['attack', 'defend']
            choice1_2 = input(f'''
                You stand your ground defending yourself from the first few attacks.
                You manage to defeat a few. but there are more left, will  you choose to attack or defend?
                ''').lower()
        if choice_1 == 'defend':
            will = input('''you defend with all your might. Attacks barraging you from all directions.
                  Choose a number from 1-10.
                  ''')
            if will >= outcome_1:
                print('You die fighting to the last breath, brave adventurer.')
            elif will > outcome_1:
                print('Even with all the attacks coming in, you manage to defeat all the werewolves!!')
        elif input == 'attack':
            choices = ['cower', 'fight']
            choices_3 = input(f'''You somehow manage to defeat the underlings.
                With extreme confidence, you approach the cabin. As you draw closer, you here a noise. 
                BOOM!! Crashing through the door is Soren The Pack Leader, standing a clear 5ft over you. Will you cower and die or fight for survival?
                (cower/ fight)
                ''')
    elif choice == 'caves':
        choice_1 = input(f'''
            After leaving the castle gates, you venture towards the direction of the Forest.
            With the information that was given to you, you stumble upon a cave entrance hidden in a valley.
            After drawing closer, from out of nowhere a cave creepers ambushes you!!
            Will you fight or withdraw?
            ''').lower()
        if choice_1 == 'fight':
            choices = ['attack', 'defend']
            choice1_2 = input(f'''
                You stand your ground defending yourself from the first few attacks.
                You manage to defeat a few. but there are more left, will  you choose to attack or defend?
                ''').lower()
        if choice_1 == 'defend':
            will = input('''you defend with all your might. Attacks barraging you from all directions.
                  Choose a number from 1-10.
                  ''')
            if will >= outcome_1:
                print('You die fighting to the last breath, brave adventurer.')
            elif will > outcome_1:
                print('Even with all the attacks coming in, you manage to defeat all the cave creepers!!')
        elif input == 'attack':
            choices = ['cower', 'fight']
            choices_3 = input(f'''You somehow manage to defeat the underlings.
                With extreme confidence, you approach a giant corridor inside the cave. As you draw closer, you here a noise. 
                Hahaha!! Creeping his way over is Lex The Disfigured, standing a clear 9ft over you. Will you cower and die or fight for survival?
                (cower/ fight)
                ''')
    elif choice == 'forest':
        choice_1 = input(f'''
            After leaving the castle gates, you venture towards the direction of the Forest.
            With the information that was given to you, you stumble upon an old farm house surrounded by dead crops.
            After drawing closer, from out of nowhere a werewolf ambushes you!!
            Will you fight or withdraw?
            ''').lower()
        if choice_1 == 'fight':
            choices = ['attack', 'defend']
            choice1_2 = input(f'''
                You stand your ground defending yourself from the first few attacks.
                You manage to defeat a few. but there are more left, will  you choose to attack or defend?
                ''').lower()
        if choice_1 == 'defend':
            will = input('''you defend with all your might. Attacks barraging you from all directions.
                  Choose a number from 1-10.
                  ''')
            if will >= outcome_1:
                print('You die fighting to the last breath, brave adventurer.')
            elif will > outcome_1:
                print('Even with all the attacks coming in, you manage to defeat all the werewolves!!')
        elif input == 'attack':
            choices = ['cower', 'fight']
            choices_3 = input(f'''You somehow manage to defeat the underlings.
                With extreme confidence, you approach the cabin. As you draw closer, you here a noise. 
                BOOM!! Crashing through the door is Soren The Pack Leader, standing a clear 5ft over you. Will you cower and die or fight for survival?
                (cower/ fight)
                ''')
else:
    print("Then why are you here? Ugh! Waste!")
