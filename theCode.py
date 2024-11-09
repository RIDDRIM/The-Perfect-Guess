import random
n = random.randint(1,100)
a =-1
guesses=1

while(a!=n):
    
    a = int(input("Guess the nummber:"))

    if (a>n):
        print("lower number please")
        guesses +=1

    elif(a<n) :
        print("higher number please")
        guesses +=1

print(f"you have gussed the number correctly in {guesses} attempts")
