import time
import random
import string
Full_answer = 10


def welcome():
    Full_answer = 10
    welc = "Welcome!"
    welc_back ="Welcome Back, Take a look around"
    new_or_not = 0
    def welcomed(Full_answer):
        Full_answer = 10
        if new_or_not == 0:
            print(welc)
        elif new_or_not == 1:
            print(welc_back)
        else:
            print("are you bug hunting...")
        time.sleep(0.4)
        print("1. Proceed to the tasks.")

        time.sleep(0.2)

        print("2. Info on the tasks.")

        time.sleep(0.2)

        print("3. Update Log")

        time.sleep(0.2)

        print("4. Contact the developer.")

        time.sleep(0.2)

        print("5. Quit program")
        
        time.sleep(0.2)
        
        Full_answer = int(input("Enter: "))
        print("*"*30)
        return Full_answer
    Full_answer = welcomed(Full_answer)
       
    
        
        
    def proceed_to_tasks(Full_answer):
        if Full_answer == 1:
            print("1. making a carpet!")
            print("2. Password and username Generator")
            print("3. Exit")
            Tasks_input = int(input("Enter an input: "))
            if Tasks_input == 1:
                Full_answer = 7
                return Full_answer
            elif Tasks_input == 2:
                Full_answer = 8
                return Full_answer
            elif Tasks_input == 3:
                Full_answer = welcomed(Full_answer)
                return Full_answer

    
    def info_on_tasks(Full_answer):
        time.sleep(0.2)
        print("There is one task at the moment, which is making a patten for carpets.")
        time.sleep(0.4)
        
        print("The second one makes a random username which uses a set list of names taht are joined tougther and then it makes a random password")
        print("")
        print("*"*30)
        time.sleep(0.2)
        input("press enter to go back: ")
        print("*"*30)
        Full_answer = welcomed(Full_answer)
        return Full_answer

    def update_logs(Full_answer):
        print("This is the second version and it is in beta so their will be bugs. ")
        time.sleep(0.2)
        print("Username and password generator which is fully random")
        time.sleep(0.2)
        print("If you find any bugs pleas contact me and report them , Thank you!")
        time.sleep(0.2)
        input("Press enter to go back: ")
        print("*"*30)
        Full_answer = welcomed(Full_answer)
        return Full_answer
        
    def contact_the_dev(Full_answer):
        print("You can contact the developer on discord by adding the account (chaositys_og)") 
        time.sleep(1)
        input("Press Enter to go back: ")
        print("*"*30)
        Full_answer = welcomed(Full_answer)
        return Full_answer
    while True:
        if Full_answer == 1:
            Full_answer = proceed_to_tasks(Full_answer)
        elif Full_answer == 2:
            Full_answer = info_on_tasks(Full_answer)
        elif Full_answer == 3:
         Full_answer = update_logs(Full_answer)
        elif Full_answer == 7 or Full_answer == 8:
            return Full_answer
            break
        elif Full_answer == 4:
            Full_answer = contact_the_dev(Full_answer)
        elif Full_answer == 5:
            exit()
        else:
            print("Invaild Input!")
            time.sleep(0.3)
            print("loading.")
            time.sleep(0.3)
            print("loading..")
            time.sleep(0.3)
            print("loading...")
            time.sleep(0.75)
            print("done!")
            return 69




def making_a_carpet():  
    
    
    text = "WELCOME"
    time.sleep(0.3)
    print("Enter the width of your carpet")
    time.sleep(0.3)
    print("Requiremeats:")
    time.sleep(0.3)
    print("An odd number.")
    time.sleep(0.3)
    print("less than 50 and greater than 5 (can change this is settings): ")
    time.sleep(1)#
    row = int(input("Enter your number: "))
    aspect_ratio = 3
    collem = row*aspect_ratio
    one_half = (collem-3)/2
    (one_half) = int(one_half)
    middle = ".|."
    number_of_middle = 1
    change = 0
    def welcome():
        answer = 0
        print("Welcome!")
        time.sleep(0.4)
        print("1. Proceed to the task.")

        time.sleep(0.2)

        print("2. Understand how it works.")

        time.sleep(0.2)

        print("3. Settings.")

        time.sleep(0.2)

        print("4. Contact the developer.")

        time.sleep(0.2)

        print("5. Exit")
        answer = int(input("Enter: "))
        return answer

    answer =welcome()

    def settings(aspect_ratio,text,row):
        while True:
            print("work in Developmeant")
            print("1. aspect ratio")
            print("2. Text in middle of pattern")
            print("3. width of carpet")
            print("4. exit")
            anser_3_input =int(input("enter: "))
            if anser_3_input == 1:
                aspect_ratio = int(input("enter a aspect ratio (width : height) 1 : "))
            elif anser_3_input == 2:
                text = input("Enter the text, 1 word, less than 12 letters long: ")
            elif anser_3_input == 3:
                row = int(input("Enter the width of your carpet: "))
            elif anser_3_input == 4:
                break
        return(aspect_ratio,text,row)
    

    if answer == 1:
        time.sleep(0.1)
    elif answer == 2:
        print("Task Explanation:")
        print("This task involves creating a carpet pattern based on user input.")
        print("1. You will be asked to enter the width of your carpet (odd number between 5 and 100).")
        print("2. The program will then generate a welcome pattern on the carpet.")
        print("3. Enjoy the visual representation of the welcome pattern!")
        time.sleep(0.5)
        input("Press Enter to go back: ")
        answer= welcome()

    elif answer == 3:
        aspect_ratio,text,row = settings(aspect_ratio,text,row)
        answer= welcome()
    elif answer == 4:
        print("You can contact the developer on discord by adding the account (chaositys_og)") 
        time.sleep(1)
        input("Press Enter to go back: ")
        answer= welcome()
    elif answer == 5:
        print("Loading...")
        time.sleep(1)
        return 100
    collem = row*aspect_ratio
    one_half = (collem-3)/2
    (one_half) = int(one_half)
    middle = ".|."
    number_of_middle = 1
    change = 0
    while answer == 1:
        if row> 5 and row<50:
            if row%2 != 0:
                for i in range(0,row):
            
                    if one_half == 0:
                        holder = one_half
                        one_half = (collem-len(text)+1)/2
                        one_half = int(one_half)
                        print("-"*one_half+text+"-"*one_half)
                        change = 1
                        one_half = holder+3
                        number_of_middle -=2
                    print("-"*one_half+middle*number_of_middle+"-"*one_half)
            
                    if change == 1:
                        one_half = one_half + 3
                        number_of_middle -= 2
                    elif change == 0:
                        one_half = one_half-3
                        number_of_middle += 2
                    if number_of_middle == -1:
                        answer = 10
                        break
                
            
            else:
                print("invalid input")
                answer = 10
                break
        else:
            print("invalid input")
            answer = 10
            break
        

def password_and_username_generator():
    string_e = ["hello", "world", "python", "programming", "example", "computer", "language", "developer", "learning", "knowledge",
            "coding", "challenge", "algorithm", "data", "science", "intelligence", "machine", "learning", "openai", "gpt-3",
            "chatbot", "artificial", "neural", "network", "deep", "learning", "creative", "innovation", "technology", "robotics",
            "automation", "future", "digital", "transformation", "web", "development", "cloud", "computing", "cybersecurity",
            "blockchain", "cryptocurrency", "bitcoin", "ethereum", "smart", "contract", "decentralized", "finance", "token",
            "crypto", "wallet", "secure", "privacy", "internet", "of", "things", "augmented", "reality", "virtual", "reality",
            "smartphone", "tablet", "application", "interface", "user", "experience", "design", "interface", "graphics", "game",
            "entertainment", "music", "art", "design", "creativity", "inspiration", "innovation", "explore", "discover", "imagine",
            "create", "inspire", "world", "unity", "diversity", "inclusion", "equality", "sustainability", "environment", "planet",
            "earth", "ocean", "forest", "wildlife", "conservation", "climate", "change", "global", "warming", "renewable", "energy"]

# Check the length of the updated list


    def welcome():
        answer = 0
        print("Welcome!")
        time.sleep(0.4)
        print("1. Proceed to the task.")

        time.sleep(0.2)

        print("2. Understand how it works.")

        time.sleep(0.2)

        print("3. Contact the developer.")

        time.sleep(0.2)

        print("4. Exit out")
        answer = int(input("Enter: "))
        return answer

    answer = welcome()

    if answer == 2:
        print("   Task Explanation:")
        print("   This task involves creating a random username and password.")
        print("1. You will enter all of the characters that you want to be in your password.")
        print("2. The program will then generate a random Password.")
        print("3. you will get given the combination of words mixed together press 'R' to regenerate a new one.")
        time.sleep(0.5)
        input("Press Enter to go back: ")
        answer = welcome()
    elif answer == 3:
        print("You can contact the developer on discord by adding the account (chaositys_og)")
        time.sleep(1)
        input("Press Enter to go back: ")
        answer = welcome()
    elif answer == 4:
        print("Loading...")
        time.sleep(1)
        return 100

    while True:
        if answer == 1:
            list_of_letters = input("Enter the characters that you want to be in your password (e.g., ABCDEFGHIGabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()): ")
            username_length = random.randint(2, 4)
            password_length = random.randint(15, 25)
            numfirst_username = random.randint(3,99)
            numsecond_username = numfirst_username - random.randint(1,numfirst_username-1)
            # Generate a random username with the first part of the first word and the last part of the second word
            username = ''.join(random.choice(string_e[numfirst_username][:len(string_e[numfirst_username]) // 2]) + random.choice(string_e[numsecond_username][len(string_e[numsecond_username]) // 2:]) for i in range(username_length - 1))


            # Generate a random password
            password = ''.join(random.choice(list_of_letters) for i in range(password_length))

            print("Generated Username: ",username)
            print("Generated Password: ",password)
            print("press 'P' to see your password and 'U' to see your username: ")
            regenerate = input("Press 'R' to regenerate or any other key to go back: ")
            if regenerate.upper() == 'R':
                print("*"*30)
            elif regenerate == 'P':
                print(password)
                input("press enter to go back")
                break
            elif regenerate == 'U':
                print(username)
                input("press enter to go back")
                break
    return welcome()

# Call the function
Full_answer = welcome()

if Full_answer == 7:
    print("")
    print("=" * 30)
    print("=" * 30)
    print("")
    time.sleep(0.5)
    making_a_carpet()
elif Full_answer == 8:
    print("")
    print("=" * 30)
    print("=" * 30)
    print("")
    time.sleep(0.5)
    cheack_to_exit = password_and_username_generator()

elif Full_answer ==69:
    Full_answer = welcome()


if cheack_to_exit == 100:
    Full_answer = welcome()
