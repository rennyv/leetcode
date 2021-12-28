# Initial offers
# Offers to BUY: $100, $100, $99, $99, $97, $90
# Offers to SELL: $109, $110, $110, $114, $115, $119

# A match occurs when two people agree on a price. Some new offers do not match. These offers should be added to the active set of offers. For example:
#   Tim offers to SELL at $150. This will not match. No one is willing to buy at that price so we save the offer.
#   Offers to SELL:: $109, $110, $110, $114, $115, $119, $150
# When matching we want to give the customer the “best price”. Example matches:
#   If Jane offers to BUY at $120, she will match and buy a book for $109 (the lowest offer to sell is the best price). The sell offers should be updated to reflect the match
#   Offers to SELL: $110, $110, $114, $115, $119, $150
# If Connie offers to SELL at $99 she will match and sell her book for $100 (the highest offer to buy is the best price). The buy offers should be updated to reflect the match
#   Offers to BUY: $100, $99, $99, $97, $90

from typing import List

class BookSelling():
    def __init__(offersToBuy: List[int]):
        pass

    def OfferToBuy(self, offer) -> int:
        pass

    def OfferToSell(self, offer) -> int:
        pass

    def printOut(self):
        pass

