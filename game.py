from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear(): return os.system('cls')


def score(deck):
    if sum(deck) > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
        return sum(deck)
    else:
        return sum(deck)


def compare_scores(deck1_score, deck2_score):
    if deck1_score == 21:
        print("Win with a Blackjack 😎")
        return True
    elif deck2_score == 21:
        print("Lose, opponent has Blackjack 😱")
        return True
    elif deck1_score < 21 and computer_turn == False:
        return False
    elif deck1_score == deck2_score:
        print("Draw 🙃")
        return True
    elif deck1_score > 21:
        print("You went over. You lose 😭")
        return True
    elif deck2_score > 21:
        print("Opponent went over. You win 😁")
        return True
    elif deck1_score > deck2_score:
        print("You win 😃")
        return True
    else:
        print("You lose 😤")
        return True


def deal_cards(deck):
    deck.append(random.choice(cards))


def game_run():
    print(logo)

    player = random.choices(cards, k=2)
    computer = random.choices(cards, k=2)

    player_score = score(player)
    computer_score = score(computer)

    print(f"\nYour cards: {player}, current score: {player_score}")
    print(f"Computer's first card: {computer[0]}")

    game_over = False
    global computer_turn
    computer_turn = False

    if player_score == 21:
        print("Win with a Blackjack 😎")

    while not game_over:
        should_continue = input(
            "Type 'h' to Hit another card or type 's' to Stand: ")

        if should_continue == 's':
            computer_turn = True
            while computer_score < 17:
                deal_cards(computer)
                computer_score = score(computer)

            print(
                f"\nYour final hand: {player} with a score of: {player_score}")
            print(
                f"Computer's final hand: {computer} with a score of: {computer_score}")
            compare_scores(player_score, computer_score)
            game_over = True
        else:
            deal_cards(player)
            player_score = score(player)
            print(f"\nYour cards: {player}, current score: {player_score}")
            game_over = compare_scores(player_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game_run()
