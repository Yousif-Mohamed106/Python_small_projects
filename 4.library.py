#library
#-----------------------person1------------------------------------------------


def person1():

  li1 = {
      "p1_info":{"name":"","age":25,"address":""}
  }
  print("wellcome to loq library🫡🔒, how i can help you?")
  print("#loq library is a place where you can save all your data;")
  print("            ##❗❗dont forget your password or you will lose all your Access❗❗#### ")
  pass_key = input("your passkey;")
  print("ok pass word has been sit,🫡")
  print("here is you menu,now")
  while True:

   print("A.press;[0] to see you information ")
   print("B.press;[1]to input your personal information[make you passkey]")
   print("C.press;[2]to delete your personal information")
   print("D.press;[3]to close your session")
   q1 = input("")
   if q1 == "0" :                                           #option0
       while True:

        check0 = input("input your pass key")
        if check0 == pass_key :
            print(li1.get("p1_info"))
            break
        else:
            print("❌access deny ")
            print("sorry,wrong password,try again")


   elif q1 == "1":                                         #option1
      n = input("your name;")
      a = input("your age;")
      ad = input("your address;")
      li1["p1_info"]["name"] = n
      li1["p1_info"]["age"] = a
      li1["p1_info"]["address"] = ad
      print("all right ",n," your information are save with me🔒")

   elif q1 == "2":                                        #option2
       while True:
        check1 = input("enter your password pls")
        if check1 == pass_key:
           print("✅ Access approved")
           sure1 =input("are you sure that you want to delete your personal information?")
           if sure1.strip().lower() == "yes":
               li1.pop("p_info")
               print("done")
               break
           else:
               print("ok,as you wise")
               break
        else:
           print("❌access deny ")
           print("sorry,wrong password,try again")
   elif q1 == "3":                                        #optaion3
       break


#-----------------------person2------------------------------------------------

def person2 ():

  li2 = {
      "p2_info":{"name":"","age":25,"address":""}
  }
  print("wellcome to loq library🫡🔒, how i can help you?")
  print("#loq library is a place where you can save all your data;")
  print("            ##❗❗dont forget your password or you will lose all your Access❗❗#### ")
  pass_key = input("your passkey;")
  print("ok pass word has been sit,🫡")
  print("here is you menu,now")
  while True:

   print("A.press;[0] to see you information ")
   print("B.press;[1]to input your personal information[make you passkey]")
   print("C.press;[2]to delete your personal information")
   print("D.press;[3]to close your session ")
   q1 = input("")
   if q1 == "0" :                                           #option0
       while True:

        check0 = input("input your pass key")
        if check0 == pass_key :
            print(li2.get("p2_info"))
            break
        else:
            print("❌access deny ")
            print("sorry,wrong password,try again")


   elif q1 == "1":                                         #option1
      n = input("your name;")
      a = input("your age;")
      ad = input("your address;")
      li2["p2_info"]["name"] = n
      li2["p2_info"]["age"] = a
      li2["p2_info"]["address"] = ad
      print("all right ",n," your information are save with me🔒")

   elif q1 == "2":                                        #option2
       while True:
        check1 = input("enter your password pls")
        if check1 == pass_key:
           print("✅ Access approved")
           sure1 =input("are you sure that you want to delete your personal information?")
           if sure1.strip().lower() == "yes":
               li2.pop("p2_info")
               print("done")
               break
           else:
               print("ok,as you wise")
               break
        else:
           print("❌access deny ")
           print("sorry,wrong password,try again")
   elif q1 == "3":                                        #optaion3
       break

#--------------------------------person3--------------------------------------------
def person3():
  li3 = {
      "p3_info":{"name":"","age":25,"address":""}
  }
  print("wellcome to loq library🫡🔒, how i can help you?")
  print("#loq library is a place where you can save all your data;")
  print("            ##❗❗dont forget your password or you will lose all your Access❗❗#### ")
  pass_key = input("your passkey;")
  print("ok pass word has been sit,🫡")
  print("here is you menu,now")
  while True:

   print("A.press;[0] to see you information ")
   print("B.press;[1]to input your personal information[make you passkey]")
   print("C.press;[2]to delete your personal information")
   print("D.press;[3]to close your session0")
   q1 = input("")
   if q1 == "0" :                                           #option0
       while True:

        check0 = input("input your pass key")
        if check0 == pass_key :
            print(li3.get("p3_info"))
            break
        else:
            print("❌access deny ")
            print("sorry,wrong password,try again")


   elif q1 == "1":                                         #option1
      n = input("your name;")
      a = input("your age;")
      ad = input("your address;")
      li3["p3_info"]["name"] = n
      li3["p3_info"]["age"] = a
      li3["p3_info"]["address"] = ad
      print("all right ",n," your information are save with me🔒")

   elif q1 == "2":                                        #option2
       while True:
        check1 = input("enter your password pls")
        if check1 == pass_key:
           print("✅ Access approved")
           sure1 =input("are you sure that you want to delete your personal information?")
           if sure1.strip().lower() == "yes":
               li3.pop("p3_info")
               print("done")
               break
           else:
               print("ok,as you wise")
               break
        else:
           print("❌access deny ")
           print("sorry,wrong password,try again")
   elif q1 == "3":                                        #optaion3
       break

#------------------------------------------------------------------------  #------------------------------------------------------------------------
#------------------------------------------------------------------------  #------------------------------------------------------------------------
#------------------------------------------------------------------------  #------------------------------------------------------------------------
#------------------------------------------------------------------------  #------------------------------------------------------------------------
#                                                        MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
def library():
    while True:
     print("library_mod_on")
     print("witch person are you?")
     print("person 1?")
     print("person 2?")
     print("person 3?")
     print("press {0} to shut down the library")
     m_q1 = input("")
     if m_q1.strip().lower() == "1":
         person1()
     elif m_q1.strip().lower() == "2":
         person2()
     elif m_q1.strip().lower() == "3":
         person3()
     elif m_q1.strip().lower() == "0":
         break
library()