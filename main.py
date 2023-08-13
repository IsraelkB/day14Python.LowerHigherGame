from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print (logo)

def get_first_famous():
  index = random.randint(0, len(data) - 1)
  return data[index]

def get_second_famous(first_famous):
  index = random.randint(0, len(data) - 1)
  second_famous = data[index]
  if first_famous['name'] == second_famous['name']:
    get_second_famous(first_famous)
  return second_famous

is_answer_corect = True
corect_score = 0

while is_answer_corect:
  first_famous = get_first_famous()
  second_famous = get_second_famous(first_famous)


  first_famous_follower = first_famous['follower_count']
  
  second_famous_follower = second_famous['follower_count']
  
  print(f"Compare A: {first_famous['name']}, a {first_famous['description']}, from {first_famous['country']}.")
  
  print(vs)
  
  print(f"Against B: {second_famous['name']}, a {second_famous['description']}, from {second_famous['country']}.")

  answer = (input("Who has more followers? Type 'A' or 'B':\n")).lower()
  
  if answer == 'a' and first_famous_follower > second_famous_follower:
    corect_score += 1
    clear()
    print (logo)
    print(f"You're right! Current score: {corect_score}.")

  elif answer == 'b' and first_famous_follower < second_famous_follower:
    corect_score += 1
    clear()
    print (logo)
    print(f"You're right! Current score: {corect_score}.")

  else:
    is_answer_corect = False
    clear()
    print(f"Sorry, that's wrong. Final score: {corect_score}")