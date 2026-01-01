import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0

    while score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    
    return score

def compare_score(u_score, c_score):
    if c_score == u_score:
        return "It's a draw"
    elif c_score == 0:
        return "lose, opponent has blackjack"
    elif u_score == 0:
        return "Win with blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Computer went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    user_cards = []
    computer_cards = []
    c_score = -1
    u_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_over == False:
        c_score = calculate_score(computer_cards)
        u_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, current score = {u_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if c_score == 0 or u_score == 0 or u_score > 21:
            game_over = True
        else:
            pick_again = input("Type 'y' to get another card, type 'n' pass: ").lower()
            if pick_again == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while c_score != 0 and c_score < 17:
        computer_cards.append(deal_card())
        c_score = calculate_score(computer_cards)

    print(f"Your final hand:{user_cards}, final score = {u_score}")
    print(f"Computer's final hand:{computer_cards}, final score = {c_score}")
    output = compare_score(u_score, c_score)
    print(output)

while input("Do you want to play a game of blackjack Type 'y' or 'n': ").lower() == 'y':
    play_game()







