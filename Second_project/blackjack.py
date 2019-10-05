import classes
import matplotlib.pyplot as plt
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Must be an integer")
        else:
            if chips.bet > chips.amount:
                print("Cannot bet more money than you have")
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_aces()
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input ("Would you like to Hit or Stand? enter h or s ")
        if x[0].lower()=='h':
            hit(deck, hand)
        elif x[0].lower()=='s':
            print("Player stands, dealer plays")
            playing = False
        else:
            print("Sorry try again")
            continue
        break
def show_some(player, dealer):
    print("\n Dealer's hand")
    print(" <card hidden> ")
    print("",dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("\nPlayer's Value: {}".format(player.value))
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
b = classes.Deck()
a = classes.Card("blue","yellow")
print(a )
print(b)
b.shuffle_deck()
print(b)
test_player = classes.Hand()
test_player.add_card(b.deal())
test_player.add_card(b.deal())
for card in test_player.cards:
    print(card)
print(test_player.value)
test_player.adjust_aces()
print(test_player.value)
player_chips = classes.Chips(100)
money = []
money.append(player_chips.amount)
while True:
    print ("Welcome to blackjack baby")
    deck = classes.Deck()
    deck.shuffle_deck()

    player_hand = classes.Hand()
    dealer_hand = classes.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    

    take_bet(player_chips)
    show_some(player_hand, dealer_hand)
    global playing
    playing = True
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break  
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
    print("\nPlayer's winnings stand at",player_chips.amount)
    money.append(player_chips.amount)
    # Ask to play again
    if player_chips.amount>0:
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    else:
        print("No money")
        break
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
plt.plot(money)
plt.show()