print("Welcome to the Quiz Game.")
print("Type 'Q' to exit the Game.")

playing = input("Do you want to play? (Y/N): ")

if playing.upper() != "Y":
    print("Okay! maybe next time.")
    quit()

print("Okay! Let's play: ")
score = 0

answer = input("What is the capital of India? (Type 'q' to quit): ")
if answer.upper() == "Q":
    print("Quitting the quiz...")
    quit()
elif answer.lower() == "delhi":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (Delhi)")

answer = input("Which direction is the opposite of north?: ")
if answer.upper() == "Q":
    print("Quitting the quiz...")
    quit()
elif answer.lower() == "south":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (South)")

answer = input("What festival is known as 'Festival of lights'?: ")
if answer.upper() == "Q":
    print("Quitting the quiz...")
    quit()
elif answer.lower() == "diwali":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (Diwali)")

answer = input("Is Jammu & Kashmir in North India?: ")
if answer.upper() == "Q":
    print("Quitting the quiz...")
    quit()
elif answer.lower() == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (Yes)")


answer = input("Is Mahakumbh celebrated every '12' or '144' years?: ")
if answer.lower() == "144":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (144 Years)")

answer = input("What is the full form of CPU?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("The correct answer is (Central Processing Unit)")

print(f"You got {score} questions correct!")

total_questions = 6
percentage_score = (score / total_questions) * 100
print(f"You got {percentage_score:.2f}%.")