import json
import os




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
                 "correct":correct.strip().upper(),
                 "difficulty":difficulty.strip().lower()
                 })
              #returning  Qusetions in Dictionary
   return questions   


# To Login and Register
def log_users(filepath="data/users.txt"):
    users={}
    if os.path.exists(filepath):
        with open(filepath,"r") as f:
            for line in f:
                name,password=line.strip().split("|")
                users[name]=password
    return users
def reg_users(username,password,filepath="data/users.txt"):
    with open(filepath,"a") as f:
        f.write(f"{username}|{password}\n")
        
        
#To Store Score 
def score_store(username,subject,difficulty,score,total,time_taken,filepath="data/score.txt"):
    with open(filepath,"a") as f:
        f.write(f"{username}|{subject}|{difficulty}|{score}/{total}|{time_taken} sec\n")
        


