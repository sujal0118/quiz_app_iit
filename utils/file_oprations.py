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
       

        f.write(f"{username}|{subject}|{difficulty}|{score}|{total}|{time_taken}\n")



#Leaderboard
def load_scores():
    scores=[]
    try:
        with open("data/score.txt","r") as f:
            for line in f:
                parts=line.strip().split("|")
                if len(parts)==6:
                    username,subject,level,score,total,time_taken=parts
                    scores.append({
                        "username":username,
                        "subject":subject,
                        "level":level,
                        "score":int(score),
                        "total":int(total),
                        "time_taken":int(time_taken)
                        })
    except FileNotFoundError:
        pass
    return scores


def top_leaderboard(n=5,path="data/leaderboard.txt"):
    scores=load_scores()
    
    top_5=sorted(scores,key=lambda x:(-x["score"],x["time_taken"]))[:n]
    
    try:
        with open(path,"w") as f:
            f.write(f"{'Rank':<10}{'Username':<15}{'Subject':<15}{'level':<15}{'Score':<10}{'Total':<10}{'Time(s)':10}\n")
            f.write("="*60+"\n")
            for i,entry in enumerate(top_5,start=1):
                f.write(f"{i:<10}{entry['username']:<15}{entry['subject']:<15}{entry['level']:<15}{entry['score']:<10}{entry['total']:<10}{entry['time_taken']:<10}\n")
        print("Leaderboard exported to 'leaderboard.txt' successfully.")
    except Exception as e:
        print("Error writing to leaderboard file:", e)

    return top_5            


