import random
def get_computer_choice():
    choices = ["rock","paper","scissores"]
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    if computer_choice == user_choice:
        print("It's a Tie")
    elif (computer_choice == "rock" and user_choice == "scissores")or (computer_choice == "scissores" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "rock"):
        print("user win")
    else:
        print("Computer win")

def main():
    print("Enter to rock-paper-scissores:")
    print("Your options are:rock,scissores,paper")

    user_choice = input("Enter your choice:").strip().lower()
    if user_choice not in ["rock","scissores","paper"]:
        print("Invalid choice ! please enter a choice rock,paper,scissores")
        return

    computer_choice = get_computer_choice()
    print(f"Computer choose:{computer_choice}")

    result = determine_winner(user_choice,computer_choice)
    print(result)

if __name__ == "__main__":
    main()