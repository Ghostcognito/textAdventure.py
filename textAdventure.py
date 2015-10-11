print("----------121COM Week 2 Lab Exercise 7----------")
print("----------------<Ghost Out the Shell>---------------")
print("---------------<By Ghostcognito aka Dylan>--------------")
print("\n")

print("You awake in a dark room. Do you:")
print("a) Scream for help.")
print("b) Press the light switch")
firstChoice = input("Enter a or b: ")
if firstChoice == "a":
    print("Something hears your screams...")
    print ('You hear movment on the other side of the door. Do you:')
    print ('a) Wiat for it to go away.')
    print ('b) Open the door to confrunt what is out there.')
    secondChoice = input('Enter a or b: ')
    if secondChoice == 'a':
        print ('You hear the "thing" move away from the door, creeping down the hall.')
        print ('Do you:')
        print ('a) Turn on the light.')
        print ('b) Open the door.')
        thirdChoice = input('Enter a or b: ')
        if thirdChoice == 'a':
            print ('The flood of light blinds you deling 1 damage.')
            print ('After a few moments you regain your vision, you see a sword on the table.')
            print ('Do you:')
            print ('a) Pick it up')
            print ('b) Leave it on the table.')
            print ('c) Curse the creater for being unfair and demand your heath back.')
        elif thirdChoice == 'b':
            print ("Through the darkness you can't see anything.")
            print ('Do you:')
# Where I left. /\
    elif secondChoice == 'b':
        print ("Trembling in fear you open the door, it's Pitch Black™ out there.")
        print ('No monster in sight.')
        print ('Do you:')
        print ('a)')
    else:
        print ('Game over. That was not an option')
        
elif firstChoice == "b":
    print("The light comes on.")
    print("You do not recognise the room but you have a really bad feeling...")
    print ('You take 1 damage and are blinded.')
    print ('Once you regain your vision,')
    print ('You see a sword on the table')
    print ('Do you:')
    print ('a) Pick up the sword.')
    print ('b) Leave the sword on the table and leave the room.')
    forthChoice = input ('Enter a or b: ')
    if forthChoice == 'a':
        print ('')
    elif forthChoice =='b':
        print('') 

else:
    print("That was not an option.  Game Over")
