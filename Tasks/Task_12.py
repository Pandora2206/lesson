class BankList:
    __number: str = None
    __name: str = None
    balance: str = None

    def input_information(self, number, name, balance):
        #  проверка на кол-во цифр, должно быть 10 и только цифры от 0 до 9
        if len(number) != 10:
            print(' больше или меньше  10 символов в номере счёта ')
            return

        self.__number = number
        self.__name = name
        self.balance = balance

    def display_info(self):
        print(self.__name,
              self.balance,
              self.__number,
              sep='\n')

    def add_money(self, money):
        self.balance+=money
        print("New balance:", self.balance)

    def reduce_money(self, money):
        self.balance-=money
        print("New balance:", self.balance)

bank_list = BankList()

bank_list.input_information("1233488455", 'Bender Pushkin', '100')
bank_list.display_info()

