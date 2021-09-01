from tabulate import tabulate
class Proper_input:
    '''
    funtions that check whether input is in proper format
    '''
    def is_phone_number(num):
        '''
        It returns True if input consists only of numeric values and has 9 or 7 digits
        '''
        num = str(num)
        if num.isnumeric():
            if len(num) == 7 or len(num) == 9:
                return True
            else:
                return False
        else:
            return False

    def is_binary(self, num):
        '''
        if input that has only numeric values consists of signs other than 0 and 1 it returns false,
        otherwise true
        '''
        num = str(num)
        if num.isnumeric():
            for digit in num:
                if digit != '0' and digit != '1':
                    return False
                else:
                    pass
            return True
        else:
            return False


class Phone_book(Proper_input):
    def __init__(self):
        #instance atribute which is a dictionary of contacts
        self.phone_book = {}

    def insert_contact(self):
        name = input('Add contact name: ')
        number = input(f'Add phone number for {name}: ')
        if Proper_input.is_phone_number(number):
            self.phone_book[name] = number
        else:
            print("WRONG INPUT! Phone number should consist of 6 or 9 digits only!.\n")

    def get_contact(self):
        query = input(f'\nWhoose phone number would You like to view?\n')
        return self.phone_book.get(query, 'Contact not found')

    def view_phone_book(self):
        num_of_coctacts_in_phone_book = len(self.phone_book)
        list_to_view = [['name', 'number']]
        if num_of_coctacts_in_phone_book == 0:
            print('Your phone book is empty')
        else:
            for i, j in self.phone_book.items():
                list_to_view.append([i, j])
            print(tabulate(list_to_view))

    def contacts_interface(self):
        choice = input(f'\nChoose one of the following:\n1.View phone book\n2.Insert new contact\n'
                           f'3.Delete contact\n4.Leave contacts menu\n')
        if choice == '1':
            self.view_phone_book()
        elif choice == '2':
            self.insert_contact()
        elif choice == '3':
            #add a function to make calls
            pass
        elif choice == '4':
            #add main menu to go back
            pass