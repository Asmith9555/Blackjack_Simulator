import random
ranks = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
rank_converter = {'A':11,'K':10,'Q':10,'J':10,
                  '10':10,'9':9, '8':8, '7':7, 
                  '6':6,'5':5,'4':4,'3':3,'2':2}
import matplotlib.pyplot as plt
class Card():
    def __init__(self, rank, value):
        self.rank = rank
        self.value = 0
    def __str__(self):
        return str(self.rank)
    def rank_conversion(self):
        self.value = rank_converter[self.rank]
        return self.value
class Shoe():
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.shoe = self.init_shoe()
        self.deck_pen = 1
    def __str__(self):
        shoe_card_ranks= ''
        for card in self.shoe:
            shoe_card_ranks += str(card)
        return shoe_card_ranks
    def init_shoe(self):
        deck = []
        for every_deck in range(self.num_decks):
            for rank in ranks:
                for every_suit in range(4):
                    deck.append(Card(rank,rank_converter[rank]))
        random.shuffle(deck)
        return deck
    def deal_card(self):
        card = self.shoe.pop()
        return card    
    def reshuffle_check(self):
        self.deck_pen = (1 - (len(self.shoe) / (self.num_decks * 52)))
        if self.deck_pen > 0.65:
            self.shoe = self.init_shoe()
        return self.shoe
class Strategy():
    def __init__(self, player_hand, dealer_hand):
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
        self.dealer_card_value = self.dealer_hand.value()
        self.player_hand_value = self.player_hand.value()
        self.action = 'LOST'
    def determine_strat(self):
        self.action = 'LOST'
        if (((str(self.player_hand) == 'A6') or 
             (str(self.player_hand) == '6A') or 
             (str(self.player_hand) == 'A7') or 
            (str(self.player_hand) == '7A')) and ((self.dealer_card_value <= 6)
            and (self.dealer_card_value != 2))):
            self.action = 'D'
        elif (((str(self.player_hand) == 'A7') or 
             str(self.player_hand) == '7A') and 
            ((self.dealer_card_value >= 9))):
            self.action = 'H'
        elif (((str(self.player_hand) == 'A6') or 
             (str(self.player_hand) == '6A')) and 
             ((self.dealer_card_value >= 7) 
             or self.dealer_card_value == 2)):
            self.action = 'H'
        elif (((str(self.player_hand) == 'A4') or 
               (str(self.player_hand) == '4A') or 
               (str(self.player_hand) == 'A5') or 
               (str(self.player_hand) == '5A')) and 
            ((self.dealer_card_value >= 4) and (self.dealer_card_value <= 6))):
            self.action = 'D'
        elif (((str(self.player_hand) == 'A4') or 
               (str(self.player_hand) == '4A') or 
               (str(self.player_hand) == 'A5') or 
               (str(self.player_hand) == '5A')) and 
            (self.dealer_card_value >= 3)):
            self.action = 'H'
        elif (((str(self.player_hand) == 'A3') or 
               (str(self.player_hand) == '3A') or 
               (str(self.player_hand) == 'A2') or 
               (str(self.player_hand) == '2A')) and 
            ((self.dealer_card_value == 5) or (self.dealer_card_value == 6))):
            self.action = 'D'
        elif (((str(self.player_hand) == 'A3') or 
               (str(self.player_hand) == '3A') or 
               (str(self.player_hand) == 'A2') or 
               (str(self.player_hand) == '2A')) and 
            (self.dealer_card_value >= 4)):
            self.action = 'H'
        elif (self.player_hand_value >= 4) and (self.player_hand_value <= 8):
            self.action = 'H'
        elif ((self.player_hand_value == 9) and 
              ((self.dealer_card_value != 3) or (self.dealer_card_value != 4) 
              or (self.dealer_card_value != 5))):
            self.action = 'H'
        elif ((self.player_hand_value == 12) and 
             ((self.dealer_card_value >= 7) or(self.dealer_card_value <= 3))):
            self.action = 'H'
        elif ((self.player_hand_value <= 16) and 
             (self.player_hand_value >= 13)) and (self.dealer_card_value >= 7):
            self.action = 'H'
        elif (self.player_hand_value == 10) and (self.dealer_card_value >= 10):
            self.action = 'H'
        elif (self.player_hand_value == 11) and (self.dealer_card_value == 11):
            self.action = 'H'
        elif (self.player_hand_value >= 17):
            self.action = 'ST'
        elif ((self.player_hand_value <= 16) and 
             (self.player_hand_value >= 13)) and (self.dealer_card_value <= 6):
            self.action = 'ST'
        elif ((self.player_hand_value == 12) and 
             ((self.dealer_card_value == 4) or (self.dealer_card_value == 5) 
              or (self.dealer_card_value == 6))):
            self.action = 'ST'
        elif (self.player_hand_value == 11) and (self.dealer_card_value <= 10):
            self.action = 'D'
        elif (self.player_hand_value == 10) and (self.dealer_card_value <= 9):
            self.action = 'D'
        elif ((self.player_hand_value == 9) and 
             ((self.dealer_card_value == 3) or (self.dealer_card_value ==  4) 
              or (self.dealer_card_value == 5))):
            self.action = 'D'
        else:
            pass
        return self.action
class Hand():
    def __init__(self, hand):
        self.hand = hand
        self.hand_value = 0
        self.number_of_aces = 0
        self.grand_number_of_aces = 0
    
    def __str__(self):
        hand_ranks = ''
        for card in self.hand:
            hand_ranks += str(card)
        return hand_ranks
    def value(self):
        self.hand_value = 0
        self.number_of_aces = 0
        self.grand_number_of_aces = 0
        for card in self.hand:
                if card.rank == 'A':
                    self.number_of_aces += 1
                    self.grand_number_of_aces += 1
                else:
                    pass
        for card in self.hand:
            self.hand_value += card.rank_conversion()
        while (self.number_of_aces > 0) and (self.hand_value > 21):
            self.hand_value -= 10
            self.number_of_aces -= 1
        return self.hand_value   
class Player():
    def __init__(self, name, hand = Hand([]), dealer_hand = Hand([])):
        self.hand = hand
        self.dealer_hand = dealer_hand
        self.name =  name
        self.money = 20
        self.bet = 1
        self.status = 'Playing'
        self.split_status = None
        self.blackjack_status = None
        self.blackjack_count = 0
        self.strategy = None
        self.strat = None
        self.win_count = 0
        self.loss_count = 0
        self.push_count = 0
        self.double_win_count = 0
        self.double_loss_count = 0
        self.blackjack_overall_count = 0
    def check_strategy(self, hand, dealer_hand):
        self.strategy = Strategy(hand, dealer_hand)
        self.strat = self.strategy.determine_strat()
    def first_card(self, shoe):
        if len(self.hand.hand) == 0:
            self.hand.hand.append(shoe.deal_card())
    def second_card(self, shoe):
        if len(self.hand.hand) == 1:
            self.hand.hand.append(shoe.deal_card())            
    def __str__(self):
        return str(self.hand)
    def split_hand_check(self):
        self.card1 = self.hand.hand[0]
        self.card2 = self.hand.hand[1]
        self.card1_value = self.card1.rank_conversion()
        if ((self.card1.rank == self.card2.rank) and 
            ((self.card1_value == 2) or (self.card1_value == 3) or
             (self.card1_value == 7)) and (self.dealer_hand.hand_value <= 7)):
            self.split_status = True
        elif ((self.card1.rank == self.card2.rank) and 
              ((self.card1_value == 11) or (self.card1_value == 8))):
            self.split_status = True
        elif ((self.card1.rank == self.card2.rank) and 
            (self.card1.rank_conversion() == (9)) and 
            ((self.card1_value <= 6) or (self.card1_value == 8) or
             (self.card1_value == 9))):
            self.split_status = True
        elif ((self.card1.rank == self.card2.rank) and 
            (self.card1_value == 4) and 
            ((self.dealer_hand.hand_value == 5) or
             (self.dealer_hand.hand_value == 6))):
            self.split_status = True
        else:
            self.split_status = False 
    def split_hand(self, shoe):
        self.hand = [Hand([split_card]) for split_card in self.hand.hand]
        for hands in self.hand:
            hands.hand.append(shoe.deal_card())
    def split_action(self, shoe):
        for hand in self.hand:
            self.check_strategy(hand, self.dealer_hand)
            if self.strat == 'H':
                while hand.hand_value < 15:
                    hand.hand.append(shoe.deal_card())
                    hand.hand_value = hand.value()
            elif self.strat == 'ST':
                pass
            elif self.strat == 'SP':
                pass
            elif self.strat == 'D':
                hand.hand.append(shoe.deal_card())
                hand.hand_value = hand.value()
                self.bet = (self.bet * 2)
            elif self.strat == 'LOST':
                raise ValueError('Strategy un-coded for')
            else:
                raise ValueError('Strat not applying')
    def normal_action(self, shoe):
        self.check_strategy(self.hand, self.dealer_hand)
        if self.strat == 'H':
            while self.hand.hand_value < 15:
                self.hand.hand.append(shoe.deal_card())
                self.hand.hand_value = self.hand.value()
        elif self.strat == 'ST':
            pass
        elif self.strat == 'SP':
            pass
        elif self.strat == 'D':
            self.hand.hand.append(shoe.deal_card())
            self.hand.hand_value = self.hand.value()
        elif self.strat == 'LOST':
                raise ValueError('Strategy un-coded for')
        else:
            raise ValueError('Strat not applying')
    def check_blackjack(self):
        if self.split_status == True:
            for hands in self.hand:
                if hands.value() == 21 and (len(hands.hand) ==2):
                    self.blackjack_status = True
                    self.blackjack_count += 1
                else:
                    self.blackjack_status = False
        else:
            if self.hand.value() == 21 and (len(self.hand.hand) == 2):
                self.blackjack_status = True
            else:
                self.blackjack_status = False
    def blackjack_win(self):
        self.money = (self.money + (self.bet * 1.5))
        self.status = 'BIG WINNER'
        self.blackjack_overall_count += 1
    def lose(self):
        if self.strat == 'D':
            self.money = (self.money - (self.bet*2))
            self.status = 'LOSER'
            self.double_loss_count += 1
        else:
            self.money = (self.money - self.bet)
            self.status = 'LOSER'
            self.loss_count += 1
    def win(self):
        if self.strat == 'D':
            self.money = (self.money + (self.bet*2))
            self.status = 'WINNER'
            self.double_win_count += 1
        else:
            self.money = (self.money + self.bet)
            self.status = 'WINNER'
            self.win_count += 1
    def push(self):
        self.push_count += 1
        self.status = 'PUSHED '
class Dealer():
    def __init__(self, hand):
        self.hand = hand
    def first_card(self, shoe):
        if len(self.hand.hand) == 0:
            self.hand.hand.append(shoe.deal_card())
    def second_card(self, shoe):
        if len(self.hand.hand) == 1:
            self.hand.hand.append(shoe.deal_card())
    def action(self, shoe):
        self.hand.hand_value = self.hand.value()
        while (self.hand.hand_value < 17):
            self.hand.hand.append(shoe.deal_card())
            self.hand.hand_value = self.hand.value()
         # ADD OR REMOVE TO CODE FOR HIT ON SOFT 17 OR STAY RESPECTIVELY   
#        while ((self.hand.hand_value < 18) and 
#               (self.hand.grand_number_of_aces > 0) and 
#               (len(self.hand.hand) == 2)):
#            self.hand.hand.append(shoe.deal_card())
#            self.hand.hand_value = self.hand.value()
class Game():
    def __init__(self, players, num_decks):
        self.round_count = 0
        self.players = players
        self.dealer = Dealer(Hand([]))
        self.shoe = self.shoe_set_up(num_decks)
    def shoe_set_up(self, num_decks):
        self.shoe = Shoe(num_decks)
        return self.shoe
    def round_reset(self):
        self.dealer.hand = Hand([])
        for player in self.players:
            player.status = 'Playing'
            player.split_status = None
            player.hand = Hand([])
            player.bet = 1
            player.hand.grand_number_of_aces = 0
        self.shoe.reshuffle_check()
        self.round_count = (self.round_count + 1)
    def deal(self):
        for player in self.players:
            player.first_card(self.shoe)
        self.dealer.first_card(self.shoe)
        for player in self.players:
            player.second_card(self.shoe)
        for player in self.players:
            player = Player(player.hand, self.dealer.hand)
    def split_check(self):
        for player in self.players:
            player.split_hand_check()
    def split_action_player(self):
        for player in self.players:
            if player.split_status == True:
                player.split_hand(self.shoe)
                player.split_action(self.shoe)
            else:
                pass
    def normal_action_player(self):
        for player in self.players:
            if player.split_status == False:
                player.normal_action(self.shoe)
            else:
                pass
    def action_dealer(self):
        self.dealer.second_card(self.shoe)
        self.dealer.action(self.shoe)
    def resolve_split_game(self):
        for player in self.players:
            player.check_blackjack()
            if player.split_status == True:
                if player.blackjack_status == True:
                    if player.blackjack_count == 2:
                        player.blackjack_win()
                        player.blackjack_win()
                    elif player.blackjack_count == 1:
                        for hand in player.hand:
                            if hand.hand_value == 21:
                                player.blackjack_win()
                            else:
                                if hand.value() > 21:
                                    player.lose()
                                elif self.dealer.hand.value() > 21:
                                    player.win()
                                elif hand.value() < self.dealer.hand.value():
                                    player.lose()
                                elif hand.value() > self.dealer.hand.value():
                                    player.win()
                                else:
                                    player.push()
                    else:
                        pass
                else:
                    for hand in player.hand:
                        if hand.value() > 21:
                            player.lose()
                        elif self.dealer.hand.value() > 21:
                            player.win()
                        elif hand.value() < self.dealer.hand.value():
                            player.lose()
                        elif hand.value() > self.dealer.hand.value():
                            player.win()
                        else:
                            player.push()
            else:
                pass
    def resolve_normal_game(self):
        for player in self.players:
            player.check_blackjack()
            if player.split_status == False:
                if player.blackjack_status == True:
                    player.blackjack_win()
                if player.hand.value() > 21:
                    player.lose()
                elif self.dealer.hand.value() > 21:
                    player.win()
                elif player.hand.value() < self.dealer.hand.value():
                    player.lose()
                elif player.hand.value() > self.dealer.hand.value():
                    player.win()
                else:
                    player.push()
            else:
                pass
    def normal_round_report(self):
        for player in self.players:
            if player.split_status == False:
                print(('**ROUND: '+str(self.round_count)+'** \nStatus-'+
                       str(player.status)+' New Balance-('+str(player.money)+
                       ')'))
            else:
                pass
    def split_round_report(self):
        for player in self.players:
            if player.split_status == True:
                print(('Round: '+str(self.round_count)+
                       '\nStatus-Split Balance-('+str(player.money)+')'))
            else:
                pass
    def play_round(self):
        self.round_reset()
        self.deal()
        self.split_check()
        self.split_action_player()
        self.normal_action_player()
        self.action_dealer()
        self.resolve_split_game()
        self.resolve_normal_game()
        self.normal_round_report()
        self.split_round_report()   
######################Simulation Block#########################################
        ##SIMULATES N ROUNDS AND TRACKS OUTCOME##
test_player = Player('Austin')
# EDIT SHOE SIZE HERE Game([test_player, *]) * = number of decks
test_game = Game([test_player], 1)
for player in test_game.players:
    # EDIT NUMBER OF ROUNDS HERE range(0, *) * = number of rounds
    for i in range(0, 5000000):
        test_game.play_round()
    print(('Normal Win Count: '+str(player.win_count)+'\nLoss Count: '+
           str(player.loss_count)+'\nPush Count: '+str(player.push_count)+
           '\nBlackjack Win Count: '+str(player.blackjack_overall_count)+
           '\nDouble Win Count: '+str(player.double_win_count)+
           '\nDouble Loss Count: '+str(player.double_loss_count)))
   ##GRAPHS BALANCE OVER ROUND FOR A SIMULATION OF N PLAYERS##
fig = plt.figure()
for i in range(0,10):
    for player in test_game.players:
        player.money = 10
        x = range (0, 100)
        y = [10]
        for i in range(0, 99):
            test_game.play_round()
            y.append(player.money)
        plt.plot(x, y)
        plt.grid(True)
        plt.ylabel('Balance')
        plt.xlabel('Round')
   
    
    
    
    
    