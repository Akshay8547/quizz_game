print("WELCOME TO QUIZ PALACE")
playing = input("Do you want to play QUIZ PALACE? ")
if playing.lower() == "yes" :
    print("Let's start QUIZ PALACE ")
    score = 0
else :
    print("quit")
answer = input("Name the fastest animal on land? ")
if answer.lower() == "cheetah" :
    print("Your answer is correct and you have scored one point")
    score += 1
else :
    print("Your answer is incorrect!Better luck next time")


answer = input("Who is currently the richest man in the world? ")
if answer.lower() == "elon musk" :
    print("Your answer is correct and you have scored one point")
    score += 1
else :
    print("Your answer is incorrect!Better luck next time")


answer = input("which is the tallest building in the world? ")
if answer.lower() == "burj kalifah" :
    print("Your answer is correct and you have scored one point")
    score += 1
else :
    print("Your answer is incorrect!Better luck next time")

   
answer = input("How many states are there in india? ")
if answer.lower() == "28" :
    print("Your answer is correct and you have scored one point")
    score += 1
else :
    print("Your answer is incorrect!Better luck next time")
    

print("You got " + str(score) + " questions correct and " + str(score) + " points")
print("You got " + str((score/4)*100) + "%")
