# version 3
'''
implemented the Timer feature 
'''
import random
from utils.file_oprations import load_questions
from utils.timer import Timer


# To ask random Questions
def ask(questions,level):
    score=0
    diff=[q for q in questions if q['difficulty']==level]
    if not diff:
        print(f"No Questions of {level} level")
    if level == "easy":
        time_limit=120
    elif level=="medium":
        time_limit=180
    elif level=="hard":
        time_limit=300
    else:
        time_limit=120
    timer=Timer(time_limit)
    timer.start()
    random.shuffle(diff) #random Questions
    for i,q in enumerate(diff,start=1):
         print(f"\n Questions {i}: {q['difficulty']}: {q['question']}")
         print(f"A.{q['options'][0]}")
         print(f"B.{q['options'][1]}")
         print(f"C.{q['options'][2]}")
         print(f"D.{q['options'][3]}")
         print(f"Time Left :{timer.time_left()} seconds")
         
         if timer.is_time_up():
             print("Time up")
             break 
         ans=input("Enter Your Answer(A/B/C/D): ").strip().upper() #convert to upper case
         if timer.is_time_up():
            print("\n⏰ Time's up while answering! Ending the quiz.")
            break
         if ans==q["correct"]:
             print("Correct")
             score+=1
         else:
            print(f"Wrong!! Correct answer:{q['correct']}\n")
    print(f"Quiz Complete!\n Your Score: {score}/{len(diff)}")
    
#To set difficulty level
def choice_difficulty():
    level=int(input("\n 1. Easy \n 2. Medium \n 3. Hard\n Choice Difficulty level:"))
    if level==1:
        return "easy"

    elif level==2:
        return "medium"
        
        
    elif level==3:
        return "hard"
        
    else:
        print("Invaild Choose!!")
        return choice_difficulty()
        

#To Check Login Credential
def check(name,password):
   return name=="sujal" and password=="12345"



#To Send Choice Subject Qusetions To User 
def subject(sub_choice):
   if sub_choice==1:
       print("Code Quiz")
       level=choice_difficulty()
       ask_questions=load_questions("data/coding_quiz_questions.txt") 
       
   elif sub_choice==2:
       print("Gk Quiz")
       level=choice_difficulty()
       ask_questions=load_questions("data/gk_quiz_questions.txt")
   else:
       print("Invalid Choice!")
       exit()
   ask(ask_questions,level)
   


print("Welcome To Quiz App...")

#Login 
print("1. Login")
print("2. Register")
choice=int(input("Enter Your Choice: "))
if choice==1:
    username=input("Enter Username:")
    password=input("Password:")
    if check(username,password):
      print("Subjects\n 1. Coding\n 2. GK")
      sub_choice=int(input("Enter your Choice:"))
      subject(sub_choice)
    else:
        print("Wrong User name and Password")
    
elif choice==2 :
    username=input("Enter Username:")
    password=input("Password:")
    print("User Registered Successfully! (Feature to store in file coming soon.)")

else:
    print("Invalid Choice!")
    