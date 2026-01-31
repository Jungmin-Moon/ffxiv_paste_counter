import shelve
    

shelve_file = shelve.open("paste counter")
                
def menu():

    print("You currently have " + str(shelve_file["paste"]) + " paste currently.")
    print("This is a menu of options:")
    print("Press 1 to add 15 from expert")
    print("Press 2 to add 15 from level cap")
    print("Press 3 to add 20 from leveling")
    print("Press 4 to add 8 from Heavyweight normals")
    print("Press 5 to add 3 from Dawntrail fates")
    print("Press 6 to add 5 from Occult Crescent CEs")
    print("Press 7 to set how many paste you currently have in your inventory.")
    print("Press 0 to exit the script")
    
    
def paste_options(response):

    match response:
        case 1:
            shelve_file["paste"] = int(shelve_file["paste"]) + 15
        case 2:
            shelve_file["paste"] = int(shelve_file["paste"]) + 15
        case 3:
            shelve_file["paste"] = int(shelve_file["paste"]) + 20
        case 4:
            shelve_file["paste"] = int(shelve_file["paste"]) + 8
        case 5:
            shelve_file["paste"] = int(shelve_file["paste"]) + 3
        case 6:
            shelve_file["paste"] = int(shelve_file["paste"]) + 5
        case 7:
            set_current_paste()
        case _:
            print("That is not a valid option.")

def set_current_paste():

    print("Please enter how much paste you have currently:")
    print("If you hit 7 by accident type 0 to go back.")
    
    while True:
        current_paste = input(">")
        
        if current_paste.isnumeric() and 1 <= int(current_paste) <= 1201:
            shelve_file["paste"] = current_paste
            break
        elif int(current_paste) == 0:
            break
        print("Invalid input, please enter a number between 1 and 1200.")

 
def get_user_input_menu():

    while True:
        user_input = input(">")
        
        if user_input.isnumeric() and int(user_input) in range(0,8):
            return int(user_input)
        
        print("Invalid input, please enter a number between 0 and 7.")
        
menu()

response = get_user_input_menu()

while response != 0:
    
    paste_options(response)
    print("You still need " + str(1200 - int(shelve_file["paste"])) + " paste still.")
    
    if shelve_file["paste"] >= 1200:
        print("Congrats you got all 1200 paste you need.") 
        break
    
    menu()
    response = get_user_input_menu()
   
  

shelve_file.close();

