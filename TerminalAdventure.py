import random
import time

#####################################################
# Function(s):
def choices(xp, money, level, rod):
# hidden level up if xp >= 100:
    while xp >= 100:
        level += xp / 100
        xp_remaining %= 100
        xp = 0 + xp_remaining
    
    print('What do you want to do?\n')
    time.sleep(1.5)
    print('1. Go fishing')
    print('2. Go to the store')
    print('3. Check your stats')
    print('4. Exit game\n')
    
    choice = input('> ')
    if choice == '1':
        xp, money, level = fishing(xp, money, level, rod)
        choices(xp, money, level, rod)
    elif choice == '2':
        money, rod = store(money, rod)
        choices(xp, money, level, rod)
    elif choice == '3':
        stats(xp, money, level, rod)
        choices(xp, money, level, rod)
    elif choice == '4':
        print('All the progresses will be erased. Are you sure to quit the game?')
        print('                [YES]                   [NO]')
        quit = input('>')
        if quit == 'YES' or 'yes' or 'Yes':
            print('                        Thanks for playing !')
        else:
            choices(xp, money, level, rod)
    else:
        print('Invalid choice. Please try again.')
        choices(xp, money, level, rod)

def stats(xp, money, level, rod):
    print('-' * 36)
    print(' ' * 3 + 'YOUR STATS:')
    print(' ' * 5 + 'XP: ' + str(xp))
    print(' ' * 5 + 'Money: $' + str(money))
    print(' ' * 5 + 'Level: ' + str(level))
    print(' ' * 5 + 'Fishing rod: ' + rod)
    print('-' * 36)
    time.sleep(1.5)
    
def fishing(xp, money, level, rod):
    print('You start fishing...\n')
    monologue = random.randint(1, 3)
    fish = random.randint(1, 6)
    time.sleep(2)
    print('.... ....... ...')
    if monologue == 1:
        print('You\'re using all your power to pull the fish out of the water...\n')
    elif monologue == 2:
        print('You\'re pretending to be a fish so you can make friend with them...\n')
    elif monologue == 3:
        print('You\'re dancing to get attention from the fish... lol..\n')
    
    #############################################################################
    #### THE TIME IT TAKES TO CATCH A FISH IS BASED ON THE ROD YOU'RE USING #####
    if rod == 'BASIC Fishing Rod':     
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
    elif rod == 'AQUATIC Fishing Rod':
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
        time.sleep(1)
        print('         .')
    elif rod == 'CODEDEX Fishing Rod':
        time.sleep(1)
        print('         .')
            
    if fish == 1:
        xp += 5.0
        money += 5.0
        print('You caught a salmon!     +5.0 xp  +$5.0')
    elif fish == 2:
        xp += 4.0
        money += 4.5
        print('You caught a trout!      +4.0 xp  +$4.5')
    elif fish == 3:
        xp += 3.5
        money += 5.0
        print('You caught a bass!       +3.5 xp  +$5.0')
    elif fish == 4:
        xp += 8.0
        money += 7.0
        print('You caught a catfish!     +8.0 xp  +$7.0')
    elif fish == 5:
        xp += 10.0
        money += 10.0
        print('You caught a gold fish!   +10.0 xp  +$10.0')
    else:
        print('You caught nothing...     +0.0 xp  +$0.0')
    return xp, money, level

def store(money, rod):
    print('You go to the store.\n')
    time.sleep(1.5)
    print('These items you can buy:\n')
    time.sleep(1.5)
    
    ######################################################################
    #### THE ITEMS IN THE STORE ARE BASED ON THE ITEMS YOU'VE BOUGHT #####
    if rod == 'BASIC Fishing Rod':
        print('1. AQUATIC Fishing Rod ($100.0)')
        print('2. CODEDEX Fishing Rod ($500.0)')
        print('3. Exit store\n')

        store_choice = input('> ')
        
        if store_choice == '1':
            if money >= 100:
                money -= 100
                rod = 'AQUATIC Fishing Rod'
                print('You upgraded your fishing rod!')
            else:
                print('You don\'t have enough money!')
                
        elif store_choice == '2':
            if money >= 500:
                money -= 500
                rod = 'CODEDEX Fishing Rod'
                print('You upgraded your fishing rod!')
            else:
                print('You don\'t have enough money!')
                
        elif store_choice == '3':
            print('You exit the store.')
            time.sleep(1.5)
            
        else:
            print('Invalid choice. Please try again.\n')
            store(money, rod)
        return money, rod
    
    elif rod == 'AQUATIC Fishing Rod':
        print('1. CODEDEX Fishing Rod ($500.0)')
        print('2. Exit store\n')

        store_choice = input('> ')
        
        if store_choice == '1':
            if money >= 500:
                money -= 500
                rod = 'CODEDEX Fishing Rod'
                print('You upgraded your fishing rod!')
            else:
                print('You don\'t have enough money!')
                
        elif store_choice == '2':
            print('You exit the store.')
            time.sleep(1.5)
            
        else:
            print('Invalid choice. Please try again.\n')
            store(money, rod)
        return money, rod
    
    elif rod == 'CODEDEX Fishing Rod':
        print('1. Exit store\n')
        store_choice = input('> ')
        
        if store_choice == '1':
            print('You exit the store.')
            time.sleep(1.5)
            
        else:
            print('Invalid choice. Please try again.\n')
            store(money, rod)
        return money, rod
##########################################################
################### GAME STARTS HERE #####################

# Introduction
print('\n\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ')
print('          FISHING ADVENTURE')
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n\n')

# Pre-scene
for i in range(0, 3):
    time.sleep(1.5)
    print(' ' * 18 + '.\n')

time.sleep(1.5)
print('          5:30 A.M (DAWN)\n')
time.sleep(1.5)
print('You\'ve just found a comfortable place for fishing.\n')
time.sleep(1.5)
print('Now you can level up and make money by fishing up the fish and go to the store:\n')
time.sleep(3)
print(' ' * 18 + '.\n')

## Goals:
print('-' * 18 + 'FISH:' + '-' * 18)
print('  1. SALMON      5.0 xp, $5.0')
print('  2. TROUT       4.0 xp, $4.5')
print('  3. BASS        3.5 xp, $5.0')
print('  4. CATFISH     8.0 xp, $7.0')
print('  5. GOLD FISH   10.0 xp, $10.0')
print('-' * 36) 
time.sleep(2)

## stats:
xp = 0
money = 0 ## Change here if you want to cheat !!!!!!
level = 1
rod = 'BASIC Fishing Rod'

print(' ' * 3 + 'YOUR STATS:')
print(' ' * 5 + 'XP: ' + str(xp))
print(' ' * 5 + 'Money: $' + str(money))
print(' ' * 5 + 'Level: ' + str(level))
print(' ' * 5 + 'Fishing rod: ' + rod)
print('-' * 36) 

time.sleep(2)

choices(xp, money, level, rod) # -> I built a loop here to keep the game going until the player chooses to exit.
