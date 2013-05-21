import random

class Card:
    def __init__(self, suit, value):
        if suit < 1 or suit > 4:
            self.suit = 1
        else:
            self.suit = suit
        if value < 2 or value > 14:
            self.value = 2
        else:
            self.value = value
        if self.value < 11:
            self.value_str = str(self.value)
        else:
            faces = ['J','Q','K','A']
            self.value_str = faces[self.value - 11]
        suits = ['D','C','H','S']
        self.suit_str = suits[self.suit-1]

    def __str__(self):
        x = self.value_str + self.suit_str
        return x

    def str(self):
        x = self.value_str + self.suit_str
        return x

    def getSuit(self):
        suits = ['D','C','H','S']
        return suits[self.suit-1]

class Deck():
    def __init__(self,count):
        self.cards = []
        self.count = count - count % 4
        self.cardsRemain = count
        for i in range(4,0,-1):
            for j in range(self.count/4+1,1,-1):
                self.cards.append(Card(i,16-j))
    def __str__(self):
        x = ''
        for i in range(self.cardsRemain):
            x = x + self.cards[i].str() + ' '
        return x
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cardsRemain >= 1:
            card = self.cards.pop()
            self.cardsRemain -= 1
            return card
        else:
            return None

    def reset(self):
        self.cards = []
        self.cardsRemain = self.count
        for i in range(4,0,-1):
            for j in range(self.count/4+1,1,-1):
                self.cards.append(Card(i,16-j))

class Player():
    def __init__(self):
        self.hand = []
    def reset(self):
        self.hand = []
    def recCard(self, card):
        self.hand.append(card)
    def playCard(self, card):
        self.hand.remove(card)
    def displayHand(self):
        x = ''
        for i in range(len(self.hand)):
            x = x + self.hand[i].str() + ' '
        return x

class HPlayer(Player):
    def __init__(self):
        self.hand = []
    def bid(self, suit_open):
        if suit_open:
           choice = raw_input('Pick a suit or pass (P): ')
        else:
           choice = raw_input('Order dealer (O) or Pass (P): ')
        return choice
    def play(self, trump):
        choice = raw_input('Pick a card to play: ')
        card = Card(choice[0],choice[1])
        self.playCard(card)
        return choice
    

class AIPlayer(Player):
    def __init__(self):
        self.hand = []
    def bid(self, suit_open):
        if suit_open:
            return 'D'
        else:
            return 'O'
    def play(self, trump):
        card = self.hand[0]
        self.playCard(card)
        return card.str()
        

class EuchreGame():
    def __init__(self):
        self.deck = Deck(24)
        self.players = [HPlayer(), AIPlayer(), AIPlayer(), AIPlayer()]
        self.trump = None
        self.dealer = random.randint(0,3)
        self.nextToPlay = (self.dealer + 1) % 4
        self.suitOpen = False
        self.playing = True

    def deal(self):
        self.deck.reset()
        self.deck.shuffle()
        for i in range(4):
            self.players[i].reset()
        for i in range(5):
            for j in range(4):
                self.players[j].recCard(self.deck.deal())
        self.topCard = self.deck.deal()

    def display(self):
        print 'Dealer: Player ' + str(self.dealer+1)
        print 'Next to play: Player ' + str(self.nextToPlay+1)
        if not self.trump:
            
            print 'Top Card: ' + self.topCard.str()
            
        else:
            print 'Trump: ' + self.trump
        print 'Your Hand: ' + self.players[0].displayHand()

    def takeTurn(self):
        if not self.trump:
            choice = self.players[self.nextToPlay].bid(self.suitOpen)                
            if choice == 'P' or choice == 'p':

                self.nextToPlay = (self.nextToPlay + 1) % 4
                if self.nextToPlay == (self.dealer + 1) % 4:
                    self.suitOpen = True
            elif choice == 'O' or choice == 'o':
                trump = self.topCard.getSuit()
                self.nextToPlay == (self.nextToPlay + 1) % 4
            else:
                trump = choice
                self.nextToPlay == (self.nextToPlay + 1) % 4
        else:
            #trump is chosen play a card
            choice = self.players[self.nextToPlay].play(self.trump)
            self.nextToPlay == (self.nextToPlay + 1) % 4
    def play(self):
        self.deal()
        while self.playing:
            self.display()
            choice = raw_input('x to quit or c to continue: ')
            if choice <> 'c':
                self.playing = False
            else:
                self.takeTurn()
def Test1():
    #comment
    
    game = EuchreGame()
    game.play()

Test1()
    

