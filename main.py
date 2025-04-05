# version 2
import random


#To Load Questions 
def load_questions(filename):       #geting file name from users choice
   questions=[]
   with open(filename,"r") as file:     #Reading Qusetions From file
       for line in file:
           parts=line.strip().split(",")
           #To ensure all Qusstions is in correct fromat
           if len(parts)==7:             
              #Unpacks the 7 elements into individual variables.
              question, op1,op2,op3,op4,correct,difficulty =parts 
             #Storing  Qusetions in Dictionary
              questions.append({
                 "question":question,
                 "options": [op1,op2,op3,op4],
                 "correct":correct.strip(),
                 "difficulty":difficulty.strip()
                 })
              #returning  Qusetions in Dictionary
       return questions   
# To ask random Questions
def ask(questions):
    score=0
    random.shuffle(questions) #random Questions
    for i,q in enumerate(questions,start=1):
         print(f"\n Question{i}: {q['difficulty']}: {q['question']}")
         print(f"A.{q['options'][0]}")
         print(f"B.{q['options'][1]}")
         print(f"C.{q['options'][2]}")
         print(f"D.{q['options'][3]}")
         
         ans=input("Enter Your Answer(A/B/C/D): ").strip().upper() #convert to upper case
         if ans==q["correct"]:
             print("Correct")
             score+=1
         else:
            print(f"Wrong!! Correct answer:{q['correct']}\n")
    print(f"Quiz Complete!\n Your Socre: {score}/{len(questions)}")
    
    
    


        

#To Check Login Credential
def check(name,password):
   return name=="sujal" and password=="12345"



#To Send Choice Subject Qusetions To User 
def subject(sub_choice):
   if sub_choice==1:
       print("Code Quiz")
       ask_questions=load_questions("data/coding_quiz_questions.txt")     
   elif sub_choice==2:
       print("Gk Quiz")
       ask_questions=load_questions("data/gk_quiz_questions.txt")
   else:
       print("Invalid Choice!")
       exit()
   ask(ask_questions)
   


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
    