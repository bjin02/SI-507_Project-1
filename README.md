This readme includes the overall of the project1 in IS507

Overview:
This is a project to test a Cards Game.

How to run the code:
Clone the repository and run the tests.py with Python3.

Functions:
test_cardConstructor_defaultValue
Functionality: This is testing if the card's default value is matching or not. There are three default values for suit names, rank_level, and faces.

test_cardConstructor_validValue
Functionality: This is testing if the value is valid. In the following situation, the values are valid. For four suit names:Diamonds, clubs, hearts, spades. Rank level is from 1-13. Faces is matching 1: "Ace", 11: "Jack", 12: "Queen", 13: "King", the others are the numbers. In addition, the combination of these should be correct.

test_cardConstructor_invalidInput(self):
Functionality: This is testing if there is an invalid input. The number is less than 0 is invalid. 

test_card_stringMethod
Functionality: This is testing the return result of string is correct. Should be Aces of spades or 2 of clubs etc.

test_deck_buildCardsList
Functionality: This is testing if the deck constructor has the following features that there is a list of 52-card deck. Any pop card should be card.

test_deck_stringMethod
Functionality: This is testing if the count of the card is totally 52.

test_deck_popCardMethod_defaultInput
Functionality: This is testing that the deck card should be poped with default value.

test_deck_popCardMethod_validInput
Functionality: This is testing if poping card with valid input, the result should be card.

test_deck_popCardMethod_cardsSize
Functionality: To test the card size should be 52. After one pop, size will be 51

test_deck_popCardMethod_invalidInput
Functionality： This is testing if the pop card is valid. If the card is poping out of number 52 is invalid.

test_deck_popCardMethod_popEmptyCards
Functionality: This is testing if the card has been removed by all, the action is invalid if no card can be poped.

test_deck_shuffleMethod
Functionality: This is testing if the self.cards list has a random order.

test_deck_replaceCard_addDuplicateCard
Functionality; If the card instance input is in the deck, it is not added back to the deck.

test_deck_replaceCard_addNewCard
Functionality: If the card instance input is not in the deck, it will be added.

test_deck_sort_cards_ascending
Functionality: The cards deck is in ancsceding order. "Diamond, Club, Heart, Spade"

test_deck_dealHand_invalidInput
Functionality: To test if the input is invalid for deal hands.

test_deck_dealHand_possibleDeal
Functionality: Hand should be able to be dealt up to the full size of the current deck.

test_deck_dealHand_impossibleDeal
Functionality:  If one cards have been removed from the deck and not replaced, it should not be dealed for 52 cards and the size is still 51.

test_deck_playWarGame
Functionality: There are 3 possible outcomes: the Player1 score is larger than the Player2 score and Player1 wins, the Player2 score is larger than the Player1 score and Player2 wins, or the two scores are the same and there is a tie.

test_showSong_defaultValue
Functionality:The default value output is a song.

test_showSong_validValue
Functionality: It creates a Song object with a valid input.

test_showSong_sameSong
Functionality: To test if the default input and customized input has the same result for "Winner".


