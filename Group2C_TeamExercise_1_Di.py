
def getStartNum():
    while True:
        n=input("starting number: ")
        if n.isdigit():
            n=int(n)
            if n<=0:
                print("You are supposed to input a positive number")
            elif n>length:
                print("You cannot input a number bigger than the length of your song")
            else:
                return n
                break
        else:
            print("Please input a number")

def getEndNum():
    while True:
        n=input("ending number: ")
        if n.isdigit():
            n=int(n)
            if n<0:
                print("You are supposed to input a positive number")
            elif n>length:
                print("You cannot input a number bigger than the length of your song")
            else:
                return n
                break
        else:
            print("Please input a number")
            
    
      
    
song=input("Please type in the first line of your favourite song： ")
length=len(song)
print("length:"+str(length))
while True:
    startNum=getStartNum()
    endNum=getEndNum()
    if endNum<startNum:
        print("Ending number must be bigger than starting number")
    else:
        print(song[startNum-1:endNum])
        break
    
"""Question2"""
"""
rain=input("Is it raining?(yes or no): ").strip().lower()
if rain=="yes":
    windy=input("Is it windy?(yes or no): ").strip().lower()
    if windy=="yes":
        print("It’s too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day")
"""
   
    
