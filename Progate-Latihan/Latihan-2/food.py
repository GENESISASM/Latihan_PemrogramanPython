from menu_item import MenuItem

class Food(MenuItem):
    def _init_(self, name, price, calorie_count):
        super()._init_(name, price)
        self.calorie_count = calorie_count

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'

    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))