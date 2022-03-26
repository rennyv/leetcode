import datetime
class FridgeItem(object):
    def __init__(self, name, amount, expiryDate) -> None:
        self.name = name
        self.amount = amount
        self.expiryDate = expiryDate

class Fridge(object):
    def __init__(self) -> None:
        self.items = {}
        self.id = 0

    def addItem(self, name, amount, expiryDate):
        self.items[self.id] = FridgeItem(name, amount, expiryDate)
        self.id += 1

    def getExpiringItems(self, expiryDate):
        items = []
        for _,i in self.items.items():
            if i.expiryDate < expiryDate:
                items.append(i)
        return items
    

def test_adding_an_item_to_the_fridge():
    f = Fridge()
    assert f.items == {}

    f.addItem('milk', 2, datetime.date(2022, 4, 1))
    assert len(f.items) == 1
    assert f.item[0].name == 'milk'


def test_list_of_expirying_items():
    f = Fridge()
    assert f.items == {}

    f.addItem('milk', 2, datetime.date(2022, 4, 1))
    f.addItem('eggs', 12, datetime.date(2022, 3, 20))
    f.addItem('bread', 2, datetime.date(2022, 5, 1))

    e = f.getExpiringItems(datetime.date(2022, 4, 2))

    assert len(e) == 2

test_list_of_expirying_items()

