#------------------------------عداد النقصان الالغاز---------------
tries1 = 3
def chance():
    global tries1
    tries1 -= 1
    return tries1
#------------------------عداد الزياده للالغاز -----------------------
count1 = 0
def points():
    global count1
    count1 += 1
    return count1
#--------------------------------------------------
def eazy():
 while True:
    q1 = input("I can talk but am not a human, what am I🧐?")
    if "parrot".lower() in q1 or "Mockingbird".lower() in q1:
        points()
        print("✅ you are right,")
        print("your points are:",count1)
        print("you what to go up a little bit 🙃?")
        a1 = input()
        if "yes".lower() in a1:
           print("ok, take the medium😶")
           medium()
        elif "no".lower() in a1:
           print("ass you wise ")
           print("you reached", count1, " points🫡")
           break
    else:
        chance()
        print("sorry,❌wrong answer try again")
        print("you have ",tries1," tries left!!")
    if tries1 == 0:
        print("game over!!")
        print("you reached", count1, " points🫡")
        break
#------------------2-----------2-------2---------2--------2-------2----------2----------2----------------------------
def medium():
 while True:
     print("am a thing, every time you take something from me i got more from that thing\nwhat am I🧐?")
     a2 = input()
     if "hole".lower() in a2:
        points()
        print("wow✅,you got it🥳🥳,")
        print("your points are:", count1)
        print('you want to go harder ?')
        z1 = input()
        if "yes".lower() in z1:
            print("so, you think you are smart🙃\nok lets fund out:")
            hard()
        elif "no".lower() in z1:
            print("if you say so😶")
            print("you reached", count1, "🫡")
            break
     else :
        chance()
        print("sorry❌,try again🙃")
        print("you have ", tries1, " tries left!!")
     if tries1 == 0:
        break

#------------3------------------3--------------------3---------------------3---------------------3---------------------
def hard():
 while True:
    a3 = input("If it takes 5 machines 5 minutes to make 5 items, how long will it take 100 machines to make 100 items?(time by minutes)")
    if "5" in a3:
        points()
        print("✅ok i admit it, you are Really  smart🫡")
        print("your points are:", count1)
        print("are you ready for the bloody mode☠️?")
        z2 = input()
        if "yes".lower() in z2:
            print("ok genus lets got started🙃 ")
            bloody()
        elif "no".lower() in z2:
            print("that what i thought😜")
            print("you reached", count1, "🫡")
            break
    else:
        chance()
        print("sorry,try again")
        print("you have ", tries1, " tries left!!")
    if tries1 == 0:
     print("game over ")
     print("you reached", count1, "🫡")
     break
#----------------4------------------------------4------------------------------4---------------------4------------------
def bloody():
 while True:
    print("I’m a three-digit number.\nMy tens digit is five more than my ones digit,")
    a3 = input("and my hundreds digit is eight less than my tens digit.\nwhat number am I🧐")
    if "194" in a3:
        points()
        print("✅yes in deed, you have all my respect,🫡")
        print("you reached", count1, "🫡")
        break
    else:
        chance()
        print("❌wrong answer,try again")
        print("you have ", tries1, " tries left!!")
    if tries1 == 0:
        print("you reached",count1, "🫡")
        break

#_______________________________
def quiz_game():

 print("quiz_game_is_on🧐: ")
 print("be carful you only have 3 shots!!!!,\n so make sure before answer😉 ")
 while True:
  print("chose the Difficulty: ")
  print("eazy👶:\nmedium😶:")
  print("hard🧐:\nbloody☠️")
  print("type: out to but the game down ")
  diff = input()
  if "eazy".lower() in diff:
    print("dont worry,i will go eazy on you😉")
    eazy()
  elif "medium".lower() in diff:
    print("so you chose the middle one😗,not bad")
    medium()
  elif "hard".lower() in diff:
    print("so, you think you are smart🙃\nok lets fund out:")
    hard()
  elif "bloody".lower() in diff:
    print("amm  so we have a genius here☠, lets test him up😈😈")
    bloody()
  elif "out".lower() in diff:
   break
  else :
   print("sorry i dont have that option😅 ")
#✨ Suggested improvements

#Add score tracking (like score += 1 for each correct answer).✅

#Add a limit to attempts (e.g., max 3 tries per question).✅

