tries = 0
def increase_tries():
    global tries
    tries += 1
    return tries
#----------------------------------------------------------------------------
count = 0
import random
def increase():
     global count
     count += 1
     return count
#---------------------------------------rule1--------------------------------
def rule1():
    print("you are now playing with the regular rules🕹️;\n press [0] to end the game;   ")
    print("press [A] to play the another game mod;" )
    print("ather ways just play and make your guess😗 ")

    while True:
         q2 = input("Your guess (1–5): ")
         ran_num = random.choice(["1","2","3","4","5"])
         print("My choice was:", ran_num)

         if q2 == ran_num:
             increase()
             print("Wow 🥳 you guessed it!")
             print("your score is:", count ,"keep it up🤗")
       #-------------------------------
         elif q2.lower() == " a ":
             rule2()
         elif q2.lower() == "0":
             print("Thank you for playing")
             break
       #-----------------------------------
         else:
             print("Nice try, but wrong😞.")
             print("your scour is ",count)

         q3 = input("Do you want to try again? (yes/no): ").lower()
         if q3 == "no":
             print("As you wish. Exiting the game...")
             break
#-----------------------------rule2-----------------------------------------------
def rule2():
    import random
    number = int(random.randint(1,100))
    print(" ❗🕹️I chose a number between 1 and 1000 and you need to guess it right in lower tries as you can do 😗 ")
    print(" by the way you can give up at any time you wise...just write{0}")
    print("you can also go no the another mod if you are pored just write{3}")
    while True:
     choise2 = int(input("ok make your guess"))
     if choise2 == number:
         print("You guessed right!🫡")
         print("you had make it in about", tries, "tries")
         break
     elif choise2 > int(number) :
         increase_tries()
         print("you went to high 😗 ")
         print("your tries so far are", tries)

     elif choise2 < int(number) :
         increase_tries()
         print("you went too low 😗 ")
         print("your tries so far are",tries)
     elif choise2 == 0:
         print("ok as you wise🫡..")
         print("you had make ",tries)
         break
     elif choise2 == 3:
         rule1()



#----------------------------------main skript--------------------------------------
def main_guess_game ():

 print("guess_game_is_on 🎮\nthis how to  to play; ")
 print("1. I chose a number and you simply guess it. ")
 print("2. I chose a number and and you guess it. but  i will teal you is it lower or higher. ")
 q0 = input("chose ([1] or [2])..... or inter {0} to close the game: ")
 if q0 == "1":
     rule1()
 elif q0 == "2":
     rule2()
 elif q0 == "0":
     print("Thank you for playing....game off...")


main_guess_game ()


