# version 1
def check(name,password):
   return name=="sujal" and password=="12345"
def subject(sub_choice):
   if sub_choice==1:
       print("Code Quiz")
   elif sub_choice==2:
       print("Gk Quiz")
   else:
       print("Invalid Choice!")
   


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
    