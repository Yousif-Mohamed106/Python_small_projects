import json
no_words = ["no", "n", "nah", "nope", "stop", "quit"]
with open("tasks_storage.json", "r") as tasks_file:
    tasks_from_storage = json.load(tasks_file)

def insert():
    while True:
     task_to_add = input("what task you want to add:")
     time_of_task = input("the date of your task? example:2/10/26::")

     tasks_from_storage [task_to_add] = time_of_task

     ask_to_continue1 = input("added..\nanything else to add?")
     if any(word == ask_to_continue1 for word in no_words):
         print("As you wish\n..")
         break


def delete():
    while True:
     task_to_delete = input("what task have you done?")
     if task_to_delete in tasks_from_storage:
        del tasks_from_storage[task_to_delete]
        print("The task has been deleted")
     else:
         print("No such task..")
     ask_to_continue2 = input("\nanything else to remove?")
     if any(word == ask_to_continue2 for word in no_words):
          print("As you wish")
          break




def show():
    if not tasks_from_storage:
        print("No tasks found")
    else:
        print(f"you have {len(tasks_from_storage)} tasks ::\n{tasks_from_storage}")
#_______________________________________________________________________________________________

print("hello and welcome to your tasks saver:\n here is your menu:")

while True:

 user_menu = input("1# to insert new tasks.\n2# to delete existing tasks.\n3# to show your tasks \n4# to shut down every thing......\nafter finishing every order you will get back to the menu to chose anew one...\n your choise::")
 if user_menu == "1":
     insert()
 elif user_menu == "2":
     delete()
 elif user_menu == "3":
     show()
 elif user_menu == "4":
     break
with open("tasks_storage.json", "w") as tasks_file:
 json.dump(tasks_from_storage, tasks_file, indent=4)
