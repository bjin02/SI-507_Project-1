
import unittest
from SI507F17_project1_cards import *
from helper_functions import *


class TestCards(unittest.TestCase):
    def test_cardConstructor_defaultValue(self):
        card = Card()
        self.assertEqual(card.suit, "Diamonds")
        self.assertEquals(card.rank, 2)
        self.assertEqual(card.rank_num, 2)

    def test_cardConstructor_validValue(self):
        card = Card(1, 2)
        self.assertEqual(card.suit_names,
                         ["Diamonds", "Clubs", "Hearts", "Spades"])
        self.assertEqual(card.rank_levels, range(1, 14))
        self.assertEqual(card.faces,
                         {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"})
        self.assertEqual(card.suit, "Clubs")
        self.assertEqual(card.rank, 2)
        self.assertEqual(card.rank_num, 2)

    def test_cardConstructor_invalidInput(self):
        with self.assertRaises(Exception):
            card = Card(0, 0)

    def test_card_stringMethod(self):
        card = Card(1, 2)
        self.assertEqual(str(card), "2 of Clubs")
        card = Card(3, 1)
        self.assertEqual(str(card), "Ace of Spades")


class TestDeck(unittest.TestCase):
    def test_deck_buildCardsList(self):
        deck = Deck()
        self.assertTrue(type(deck.cards) is list)
        self.assertEqual(len(deck.cards), 52)
        self.assertTrue(type(deck.cards[0]) is Card)

    def test_deck_stringMethod(self):
        deck = Deck()
        self.assertEqual(str(deck).count('\n'), 51)

    def test_deck_popCardMethod_defaultInput(self):
        deck = Deck()
        card = deck.cards[-1]
        self.assertEqual(deck.pop_card(), card)

    def test_deck_popCardMethod_validInput(self):
        deck = Deck()
        card = deck.cards[0]
        self.assertEqual(deck.pop_card(0), card)

    def test_deck_popCardMethod_cardsSize(self):
        deck = Deck()
        card = deck.pop_card(51)
        self.assertEqual(len(deck.cards), 51)

    def test_deck_popCardMethod_invalidInput(self):
        deck = Deck()
        with self.assertRaises(IndexError):
            deck.pop_card(52)
        with self.assertRaises(IndexError):
            deck.pop_card(-1)

    def test_deck_popCardMethod_popEmptyCards(self):
        deck = Deck()
        for i in range(0, 52):
            deck.pop_card()
        with self.assertRaises(IndexError):
            deck.pop_card(-1)

    def test_deck_shuffleMethod(self):
        deck = Deck()
        str1 = str(deck)
        deck.shuffle()
        str2 = str(deck)
        self.assertNotEqual(str1, str2)

    def test_deck_replaceCard_addDuplicateCard(self):
        deck = Deck()
        str1 = str(deck)
        for i in range(0, 4):
            for j in range(1, 14):
                card = Card(i, j)
                deck.replace_card(card)
                str2 = str(deck)
                self.assertEqual(str1, str2)

    def test_deck_replaceCard_addNewCard(self):
        deck = Deck()
        str1 = str(deck)
        card = deck.pop_card()
        deck.replace_card(card)
        str2 = str(deck)
        self.assertEqual(str1, str2)

    def test_deck_sort_cards_ascending(self):
        deck = Deck()
        deck.sort_cards()
        for i in range(0, 52):
            if i/13 == 0:
                self.assertEqual(deck.cards[i].suit, "Diamonds")
            elif i/13 == 1:
                self.assertEqual(deck.cards[i].suit, "Clubs")
            elif i/13 == 2:
                self.assertEqual(deck.cards[i].suit, "Hearts")
            elif i/13 == 3:
                self.assertEqual(deck.cards[i].suit, "Spades")

    def test_deck_dealHand_invalidInput(self):
        deck = Deck()
        with self.assertRaises(IndexError):
            deck.deal_hand(53)
            deck.deal_hand(-1)

    def test_deck_dealHand_possibleDeal(self):
        deck = Deck()
        deck.deal_hand(3)
        self.assertEqual(len(deck.cards), 49)

    def test_deck_dealHand_impossibleDeal(self):
        deck = Deck()
        deck.pop_card()
        deck.deal_hand(52)
        self.assertEqual(len(deck.cards), 51)

    def test_deck_playWarGame(self):
        res, p1, p2 = play_war_game(True)
        if p1 > p2:
            self.assertEqual(res, "Player1")
        elif p1 < p2:
            self.assertEqual(res, "Player2")
        elif p1 == p2:
            self.assertEqual(res, "Tie")

    def test_showSong_defaultValue(self):
        song = show_song()
        self.assertEqual(type(song), Song)

    def test_showSong_validValue(self):
        song = show_song("When I was Your Man")
        self.assertEqual(type(song), Song)

    def test_showSong_sameSong(self):
        song1 = show_song()
        song2 = show_song("Winner")
        self.assertEqual(song1, song2)
