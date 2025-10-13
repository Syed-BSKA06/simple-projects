import random
CHOICES = ["rock", "paper", "scissors"]
WIN_MAP = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors": "paper"
}
player_score = 0
cpu_score = 0
while True:
    user = input("Your move {rock/paper/scissors or q): ").strip().lower()
    if user in ("q","quit"):
        print("\nThanks for playing!")
        break
    if user not in CHOICES:
        print("Invalid choice. Try again.\n")
        continue
    cpu = random.choice(CHOICES)
    print(f"Computer chose: {cpu}")

    if user == cpu:
        print("Result: Its a tie! \n")
    elif WIN_MAP[user] == cpu:
        print("Result: You win this round\n")
        player_score+=1
    else:
        print("Result: Computer wins this round\n")
        cpu_score+=1
    
    print(f"Score --> You : {player_score}\n Computer Score: {cpu_score}/n")


