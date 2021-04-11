#import os
#os.system("cls") doesn't work in pycharm :/

def clear():
    print("\n"*15)

Questions_file = open("Questions.txt", "r")
Answers_file = open("Ansvers.txt", "r")

Questions = Questions_file.readlines()
Answers = Answers_file.readlines()

print("This is a ten question test\n"
      "You will see your result and the correct answers after you answered all the questions\n"
      "Have Fun")
input()

Again = "y"
while True:
    clear()
    if Again.lower() == "y":
        your_answer = []
        points = 0
        for i in range(len(Questions)):
            print("Soru #%d\n%s" % (i + 1, Questions[i].strip('\n')))
            your_answer.append(input("Enter your answer: "))
            # os.system("cls")
            clear()
            if your_answer[i].lower() == Answers[i].strip("\n").lower():
                #print("Correct")
                points += 10
        # os.system("cls")
        clear()
        if points > 50:
            print(f"\n\n{points} Points\nCongratulations You Have Passed The Test\n")
        else:
            print(f"\n\n{points} Points\nYou Have Failed\n")

    elif Again.lower() == "q":
        len(Answers)
        for i in range(len(Answers)):
            clear()
            print("Question #%d: %s\n\tCorrect answer: %s\n\tYour answer: %s" % (i + 1, Questions[i].strip("\n"), Answers[i].strip("\n"), your_answer[i]))
            input()
        print(f"Your score is {points}\n")
        print("Thank you for taking the test")
        exit()

    Again = input("To take the Test again press 'y'\n"
                  "To see the Answers and quit press 'q':\n  ")
