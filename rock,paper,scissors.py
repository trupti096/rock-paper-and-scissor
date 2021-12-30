from random import randint
def win():
    print ('You win!')
def lose():
    print ('You lose!')
while True:
    player= input('What do you pick? (rock, paper, scissors)')
    player.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer = moves[random_move]
    if player == computer:
        print ('Draw!')
    elif player == 'rock' and computer == 'scissors':
        print("win rock")
    elif player == 'paper' and computer == 'scissors':
        print("lose paper")
    elif player == 'scissors' and computer == 'paper':
        print("win scissors")
    elif player == 'scissors' and computer == 'rock':
        print("lose scissors")
    elif player == 'paper' and computer == 'rock':
        print("win paper")
    elif player == 'rock' and computer == 'paper':
        print("lose rock")
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break

