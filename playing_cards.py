import unittest
class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()

class PlayingCard():
    PlayingCard.suit == [
                        ' of heart', ' of diamond', ' of spade', ' of club'
                        ]
    PlayingCard.rank == [
                        'ace', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', 'jack', 'queen', 'king'
                        ]
    PlayingCard.hand == ['royal flush','straight flush','four of kind',
                        'full house','flush','straight','three of kind',
                        'two pair','one pair','high card'
                    ]
    def __init__(self, suit=0, rank=0,):
        self.suit = suit
        self.rank = rank


    def rank(self):
        if self.rank in ranks:
            ranks[self.rank] = self.rank
            return self.rank


    def suit(self):
        if self.suit in suits:
            suits[self.suit] = self.suit
            return self.suit

    def mapping(self):
        dict = {}
        junk = map(
                    lambda PlayingCardsuit, PlayingCardrank:
                    dict.update({PlayingCard.suit: PlayingCard.rank}
                    )
                    , PlayingCardsuit, PlayingCardrank
                    )
