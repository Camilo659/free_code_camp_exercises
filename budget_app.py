class Category():
    data = {'amount':[], 'description':[]}
    data_transfered = {'amount':[], 'description':[]}

    def __init__(self):
        self.amount = 0
 
    def deposit(self, quantity, description):
        self.description = f'{description:.23s}'
        self.amount = self.amount + quantity
        self.data['amount'].append(quantity)
        self.data['description'].append(self.description)
        
    def withdraw(self, quantity, description):  
        if quantity > self.amount:  return ('not founds enough')
        else:                       
            self.data['amount'].append(quantity * -1)
            self.data['description'].append(self.description)
            self.amount -= quantity
            self.description = f'{description:.23s}'

        if self.amount > 0: return True       
        else:               return False
    
    def get_balance(self):       
        return self.amount
    
    def transfer(self, quantity, transfer_to):
        if quantity > self.amount:  return False
        else:  
            self.transfering = input('Transfer to: ')             
            self.data['amount'].append(quantity * -1)      
            self.amount -= quantity
            transfer_to.deposit(quantity, 'Transfer to ' + self.transfering)

    def check_funds(self, quantity):
        if self.amount < quantity: return False 
        else:                      return True
            
#Calling the category here       
Clothing = Category()
Food = Category()

ledger = Category()
ledger.deposit(1000.00, 'Initial deposit')
ledger.withdraw(10.15, 'groceries')
ledger.withdraw(15.89, 'restaurant and more food')
ledger.transfer(50.00, Clothing)
ledger.transfer(50.00, Food)

#Print the budget function
def printing():
    balance = list()
    get_balance = ledger.data

    for i in get_balance:
        balance.append(get_balance[i])
    get_amount_balance = balance[0]
    get_description_balance = balance[1]

    cat = input('Category name is: ')
    cat = cat.center(30)
    print(cat.replace(' ','*'))

    printed = '\n'.join('{0:<23}{1:>7.2f}'.format(i,o) 
    for i, o in zip(get_description_balance, get_amount_balance))
    print(printed)
    print('Total:', ledger.get_balance())



#Whithout create_spend_chart :(












