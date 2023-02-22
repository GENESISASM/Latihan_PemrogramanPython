from menu_item import MenuItem

class Drink(MenuItem):
    def _init_(self, name, price, volume):
        super()._init_(name, price)
        self.volume = volume

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'