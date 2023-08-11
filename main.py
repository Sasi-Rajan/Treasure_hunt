print('''
                           |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____               /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _
 __..._____--==/___]_|__|_____________________________[___\==--___,-----' 
|                                                                        /
 \_______________________________________________________________________|
''')
print("Welcomt to the tressure island")
road1=input("You're now at parkinson road. How do you want to move 'left' or 'right \n").lower()
if road1 == 'left':
    designation1=input("You're near the lake. How do you want to move 'swim' or 'wait' \n").lower()
    if designation1 == 'wait':
        print("You sailed form the boat")
        designation2=input("Now you have a 3 doors 'red' , 'blue' and 'yellow'. Choose one \n").lower()
        if designation2 == 'red' or designation2 == 'blue':
            print("Game over")
        else:
            print("You won this game!!!")
    else:
        print("Game over")
else:
    print("Game over")