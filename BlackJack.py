import unittest
import random
import time

Values = {
            '2'     :  2,
            '3'     :  3,
            '4'     :  4,
            '5'     :  5,
            '6'     :  6,
            '7'     :  7,
            '8'     :  8,
            '9'     :  9,
            '10'    : 10,
            'Jack'  : 10,
            'Queen' : 10,
            'King'  : 10,
            'Ace'   : 11
         }


class Card:


    def __init__(self, value = 'Ace', suit = 'Heart'):
        self.value_ = value
        self.suit_ = suit
        if suit not in self.suit_:
            raise AttributeError("suit not valid")
        if value not in self.value_:
            raise AttributeError("value not valid")


    def __int__(self):
        return Values[self.value_]


    def __repr__(self):
        return '%s-%s' % (self.value_, self.suit_)


    def is_ace(self):
        return self.value_ == 'Ace'


class Deck:


    def __init__(self):
        self.cards_ = []
        for suit in [
                    color.RED + '♥' + color.END,
                    color.BLUE + '♦' + color.END,
                    '♠', color.GREEN + '♣' + color.END
                    ]:
            for value in Values.keys():
                card = Card(value, suit)
                self.cards_.append(card)


    def deal(self):
        position_in_deck = random.randint(0, len(self.cards_)-1)
        card = self.cards_[position_in_deck]
        self.cards_.pop(position_in_deck)
        return card


class Hand:


    def __init__(self, owner = 'Dealer'):
        self.cards_ = []
        self.owner_ = owner


    def hit(self, deck):
        self.cards_.append(deck.deal())


    def tally(self):
        total = aces = 0
        for card in self.cards_:
            total += int(card)
            if card.is_ace():
                ++aces
        while aces > 0 and total > 21:
            total -= 10
            aces -= 1
        return total


    def is_busted(self):
        return self.tally() > 21


    def might_want_to_hit(self):
        return self.tally() < 18


    def owner(self):
        return self.owner_


    def cards(self):
        text = ''
        for card in self.cards_:
            if text:
                text += ', '
            text += '%s' % card
        return text


    def tally_and_cards(self):
        return '%d: %s' % (self.tally(), self.cards())


    def tally_and_first_card(self):
        return '%d: %s, (DOWN)' % (self.tally(), self.cards_[0])


    def win_or_lose(self, dealer):
        if self.is_busted():
            return 'you busted'

        if dealer.is_busted():
            return color.YELLOW + 'YOU WIN !!!' + color.END

        total_hand = self.tally()
        total_dealer = dealer.tally()

        if total_dealer > total_hand:
            return 'you lose'

        elif total_dealer < total_hand:
            return color.YELLOW + 'YOU WIN !!!' + color.END

        else:
            return 'this is a push'


class Player(Hand):


    def __init__(self, owner = 'Player'):
        Hand.__init__(self, owner)


    def header(self):
        time.sleep(1)
        return '    %s has %s' % (self.owner(), self.tally_and_cards())


    def summary(self):
        time.sleep(1)
        return '    %s has %s' % (self.owner(), self.tally_and_cards())


    def hit_or_stand(self):
        time.sleep(1)
        return '%s, you have %s' % (self.owner(), self.tally_and_cards())


class Dealer(Hand):


    def __init__(self):
        Hand.__init__(self, 'Dealer')


    def header(self):
        time.sleep(1)
        return (color.RED + 'The Dealer has' + color.END +' %s' ) % self.tally_and_first_card()


    def summary(self):
        time.sleep(1)
        return (color.RED + '    Dealer has' + color.END +' %s') % self.tally_and_cards()


    def hit_or_stand(self):
        time.sleep(1)
        return (color.RED + 'Dealer has' + color.END +' %s') % self.tally_and_cards()


class Game:


    def __init__(self, players = range(1, 1)):
        self.deck_ = Deck()
        self.players_ = {}


        for player in players:
            player = input("Enter player name: ")
            hand = Player(color.BOLD + '%s' % player + color.END)
            hand.hit(self.deck_)
            hand.hit(self.deck_)
            self.players_[player] = hand
        self.dealer_ = Dealer()
        self.dealer_.hit(self.deck_)
        self.dealer_.hit(self.deck_)


    def players(self):
        return self.players_.keys()


    def print_header(self):
        dealer = self.dealer_
        for player in self.players():
            hand = self.players_[player]
            print(hand.header())
        print(dealer.header())
        print


    def print_summary(self):
        dealer = self.dealer_
        for player in self.players():
            hand = self.players_[player]
            print('%s - %s!' % (hand.summary(), hand.win_or_lose(dealer)))
        print(dealer.summary())
        print


    def play_player_loop(self, player):


        hand = self.players_[player]
        while True:
            if hand.is_busted():
                print('%s - You busted!' % hand.hit_or_stand())
                break

            question = '%s - Hit or stand? ' % hand.hit_or_stand()
            answer = input(question).lower()

            if 's' in answer:
                break

            hand.hit(self.deck_)
        print


    def play_dealer_loop(self):
        dealer = self.dealer_
        while True:
            if dealer.is_busted():
                break

            elif dealer.might_want_to_hit():
                print('%s - Dealer hits' % dealer.hit_or_stand())
                dealer.hit(self.deck_)

            else:
                break

        print('%s - Dealer stands' % dealer.hit_or_stand())
        print


    def play(self):
        self.print_header()
        for player in self.players():
            self.play_player_loop(player)
        self.play_dealer_loop()
        self.print_summary()


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class TestCard(unittest.TestCase):


    def testSuits(self):
        self.assertEqual(4, len(Card.suits))
        self.assertTrue('hearts' in Card.suits)
        self.assertFalse('weasels' in Card.suits)


    def testValues(self):
        self.assertEqual(13, len(Card.values))
        self.assertTrue('9' in Card.values)
        self.assertTrue('21' not in Card.values)


    def testInit(self):
        pc1 = Card('ace', 'hearts')
        self.assertEqual('ace', pc1.value)
        self.assertEqual('hearts', pc1.suit)
        with self.assertRaises(TypeError):
            pc2 = Card()
        with self.assertRaises(AttributeError):
            pc3 = Card('duke', 'earl')


    def testShortName(self):
        pc1 = Card('9', 'clubs')
        self.assertEqual('9C', pc1.shortName())


    def testLongName(self):
        pc = Card('10', 'hearts')
        self.assertEqual('ten of hearts', pc.longName())



class TestDeck(unittest.TestCase):


    def testInit(self):
        deck = Deck()
        self.assertEqual(52, len(deck.cards))

    def testShuffle(self):
        deck = Deck()
        copy_of_cards = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(copy_of_cards, deck.cards)


if __name__ == '__main__':


    playstart = input(color.CYAN +
    """\t\t
     🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮🂮
     🂮             ---_ ......._-_--.          ___________________       🂮
     🂮           (|\ /      / /| \  \          13    CELL 13    13       🂮
     🂮           /  /     .'  -=-'   `.        13_______________13       🂮
     🂮          /  /    .'             )       ||   ||     ||   ||       🂮
     🂮           _/  /   .'        _.)   /     ||   ||, , ,||   ||       🂮
     🂮          / o   o        _.-' /  .'      ||  (||/|/(\||/  ||       🂮
     🂮          \          _.-'    / .'*|      ||  ||| _'_`|||  ||       🂮
     🂮           \______.-'//    .'.' \*|      ||   || o o ||   ||       🂮
     🂮            \|  \ | //   .'.'_ _|*|      ||  (||  - `||)  ||       🂮
     🂮             `   \|//  .'.'_ _ _|*|      ||   ||  =  ||   ||       🂮
     🂮              .  .// .'.' | _ _ \*|      ||   ||\___/||   ||       🂮
     🂮              \`-|\_/ /    \ _ _ \*\     ||___||) , (||___||       🂮
     🂮   (\____/)    `/'\__/      \ _ _ \*\   /||---||-\_/-||---||\      🂮
     🂮   / @__@ \   /^|            \ _ _ \*\ / ||--_||_____||_--|| \     🂮
     🂮  (  (oo)  ) '  `   .__       \__\ _\ (_(||)-|   666   |-(||)_)    🂮
     🂮   `-.~~.-'    ____ |__| ____ |  | __ |xxxxxxxxxxxxxxxxxxxxxxxx|   🂮
     🂮    /    \    /  _ \|  |/    \|  |/ / |   ♣ PYTHON PRISON ♣    |   🂮
     🂮  @/      \_ (  <_> )  |   |  \    <  |   ♠   ♦  CAMP  ♦  ♠    |   🂮
     🂮 (/ /    \ \) \____/|__|___|  /__|_ \ |   ♥   BlackJack   ♥    |   🂮
     🂮  WW`----'WW                \/     \/ |xxxxxxxxxxxxxxxxxxxxxxxx|   🂮
     🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮 🂮🂮🂮🂮🂮🂮🂮🂮
                            Ready to play? Enter yes.

     \n""" + color.END)
    if playstart == "yes":

        stash = 0
        wager = 0
        names = []
        number_of_players = int(input( 'Number of players? '))
        print
        players = range(1, number_of_players + 1)
        blackjack = Game(players)
        blackjack.play()
