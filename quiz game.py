def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for i,key in enumerate(questions):
        print("----------------------")
        print(key)
        for option in options[i]:
            print(option)
        guess = input("Your answer is (A, B, C, or D):").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
    display_score(correct_guesses,guesses)
    print("----------------------")
def check_answer(answer, guess):
    if answer == guess :
        print("Correct")
        return 1
    else:
        print("Worng")
        return 0

def display_score(correct_guesses,guesses):
    print("--------------------")
    print("RESULTS")
    print("------------")

    print("Answers: ",end= "")
    for answer in questions:
        print(questions.get(answer),end=" ")
    print()


    print("Guesses: ",end= "")
    for guess in guesses:
        print(guess,end=" ")
    print()

    score = (round((correct_guesses/len(questions))*100,2))
    print("Score:", str(score)+"%")
    

def play_again():
    while True:
        response = input("Do you want to play again? (yes or no): ").lower()

        if response == "yes":
            return True
        elif response == "no":
            return False




questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
print("*****************")
print("Until Next Time!!!")
print("*****************")
    
