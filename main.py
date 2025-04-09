# version 7
'''
implemented the Leaderboard feature 
'''
import random
from utils.file_oprations import load_questions, reg_users, log_users, score_store, top_leaderboard
from utils.timer import Timer


# To ask random Questions
def ask(questions,level,subject,username):
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
         print("="*55,"\n")
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
            print("\n Time's up while answering! Ending the quiz.")
            break
         if ans==q["correct"]:
             print("Correct")
             score+=1
         else:
            print(f"Wrong!! Correct answer:{q['correct']}\n")
    print("="*55)        
    print(f"Quiz Complete!\n Your Score: {score}/{len(diff)}")
    time_taken=timer.time_elapsed()
    score_store(username, subject, level, score, len(diff), int(time_taken))
    print("Score Saved ..")
    print("="*55)
    print(" 1.Yes \n 2. No")
    show=int(input(" \n  Do you want to see the Leaderboard: "))
    if show==1:
        show_leaderboard()
    
    
#To set difficulty level
def choice_difficulty():
    print("="*55)
    print(" 1. Easy \n 2. Medium \n 3. Hard")
    print("="*55)
    level=int(input("Choice Difficulty level:"))
    if level==1:
        return "easy"

    elif level==2:
        return "medium"
        
        
    elif level==3:
        return "hard"
        
    else:
        print("Invalid Choice!!")
        return choice_difficulty()
        

#leaderboard
def show_leaderboard():
    print("="*30)
    print("\t TOP 5 Leaderboard:")
    print("="*30)
  
    leaderboard=top_leaderboard()
    if not leaderboard:
        print("No Scores available yet")
        return
    print("="*75)
    print(f"{'Rank':<10}{'User':<12}{'Subject':<15}{'level':<10}{'Score':<9}{'Time(s)':<8}")
    print("="*75)
    for i ,entry in enumerate(leaderboard,start=1):
       

        print(f"{i:<10}{entry['username']:<12}{entry['subject']:<15}{entry['level']:<10}{entry['score']:<10}{entry['time_taken']:<8}")
        print("="*75)

    

#To Check Login Credential
def check(name,password):
    users=log_users()
    if name in users and users[name]==password:
        print("Login successful!")
        print("="*55)
        return True
    else:
        print("Invalid credentials. Please try again.")
        print("="*55)
        return None

def register():
  
   username=input("Enter Username:")
   password=input("Password:")
   users=log_users()
   if username in users:
       print("Username already exists. Try another one")
       return None
   else:
      reg_users(username, password)
      print("User Registered Successfully! ")
      return username

#To Send Choice Subject Qusetions To User 
def subject(sub_choice,username):
   if sub_choice==1:
       
       level=choice_difficulty()
       ask_questions=load_questions("data/coding_quiz_questions.txt") 
       subject = "Coding"
       
   elif sub_choice==2:
     
       level=choice_difficulty()
       ask_questions=load_questions("data/gk_quiz_questions.txt")
       subject = "GK"
   else:
       print("Invalid Choice!")
       exit()
   ask(ask_questions,level,subject,username)
   

print("="*55)
print("Welcome To Quiz App...")
print("Rules")
print("- Each question has 4 options.\n- Enter the option (A, B, C, D) as your answer.\n- Select Option below To Start")

#Login 
print("1. Login")
print("2. Register")
print("3. View Leaderboard")
print("="*55)
choice=int(input("Enter Your Choice: "))
if choice==1:
    username=input("Enter Username:")
    password=input("Password:")
    if check(username,password):
      print("="*55)
      print("Subjects\n 1. Coding\n 2. GK")
      print("="*55)
      sub_choice=int(input("Enter your Choice:"))
      subject(sub_choice,username)

elif choice==2 :
      register()
elif choice==3:
    show_leaderboard()
else:
    print("Invalid Choice!")
    