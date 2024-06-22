import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ans = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
lst = [rock, paper, scissors]

if ans == 0:
    print(rock)
elif ans == 1:
    print(paper)
elif ans == 2:
    print(scissors)
else:
    print("Invalid input.")
    exit()
comp = random.randint(0, 2)
print(f"Computer chose:\n{lst[comp]}")
if(ans == 0 and comp == 2) or (ans == 1 and comp == 0) or (ans == 2 and comp == 1):
    print("You win!")
elif ans == comp:
    print("It's a draw.")
else:
    print("You lose.")
