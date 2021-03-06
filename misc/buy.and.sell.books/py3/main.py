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
    def __init__(self, offersToBuy: List[int], offersToSell: List[int]):
        offersToBuy.sort(reverse=True)
        offersToSell.sort()
        self._offersToSell = offersToSell
        self._offersToBuy = offersToBuy

    def OfferToBuy(self, offer) -> int:
        retVal = None
        
        for price in self._offersToSell:
            if offer >= price:
                self._offersToSell.remove(price)
                return price

        #add to sell
        self._offersToSell.append(offer)
        self._offersToSell.sort()

    def OfferToSell(self, offer) -> int:
        for price in self._offersToBuy:
            if offer <= price:
                self._offersToBuy.remove(price)
                return price

        #add to sell
        self._offersToSell.append(offer)
        self._offersToSell.sort()
        return None

    def printOut(self):
        pass

def test_ex1():
    offersToSell = [109, 110, 110, 114, 115, 119]
    offersToBuy = [100, 100, 99, 99, 97, 90]
    bs = BookSelling(offersToBuy, offersToSell)

    #   Tim offers to SELL at $150. This will not match. No one is willing to buy at that price so we save the offer.
    #   Offers to SELL:: $109, $110, $110, $114, $115, $119, $150
    ans1 = [109, 110, 110, 114, 115, 119, 150]

    result = bs.OfferToSell(150)    

    assert result is None
    assert ans1 == bs._offersToSell

    #   If Jane offers to BUY at $120, she will match and buy a book for $109 (the lowest offer to sell is the best price). The sell offers should be updated to reflect the match
    #   Offers to SELL: $110, $110, $114, $115, $119, $150
    ans2 = [110, 110, 114, 115, 119, 150]

    result = bs.OfferToBuy(120)

    assert result == 109
    assert ans2 == bs._offersToSell

    # If Connie offers to SELL at $99 she will match and sell her book for $100 (the highest offer to buy is the best price). The buy offers should be updated to reflect the match
    # Offers to BUY: $100, $99, $99, $97, $90
    ans3 = [100, 99, 99, 97, 90]

    result = bs.OfferToSell(99)

    assert result == 100
    assert ans3 == bs._offersToBuy


test_ex1()