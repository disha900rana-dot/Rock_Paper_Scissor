import random

def game_win(comp, you):
    if comp == you:
        return None
    elif comp == "Rock":
        if you == "Paper":
            return True
        elif you == "Scissors":
            return False
    elif comp == "Paper":
        if you == "Scissors":
            return True
        elif you == "Rock":
            return False
    elif comp == "Scissors":
        if you == "Rock":
            return True
        elif you == "Paper":
            return False


user_score = 0
computer_score = 0

# Play 5 times
for i in range(1, 6):

    print(f"\n---------- Round {i} ----------")

    random_No = random.randint(1, 3)

    if random_No == 1:
        comp_choice = "Rock"
    elif random_No == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    user = input("Your Turn: Rock(1), Paper(2), Scissors(3): ")

    if user == "1":
        user_choice = "Rock"
    elif user == "2":
        user_choice = "Paper"
    elif user == "3":
        user_choice = "Scissors"
    else:
        print("Invalid choice! Try again.")
        continue

    result = game_win(comp_choice, user_choice)

    print(f"Computer chose: {comp_choice}")
    print(f"You chose: {user_choice}")

    if result is None:
        print("It's a tie!")

    elif result:
        print("You win!")
        user_score += 1

    else:
        print("You lose!")
        computer_score += 1


# Final score
print("\n========== FINAL SCORE ==========")
print(f"Your marks: {user_score}")
print(f"Computer marks: {computer_score}")

if user_score > computer_score:
    print("You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game is a tie!")