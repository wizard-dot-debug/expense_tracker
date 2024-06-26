def expense(a,b,c,d):
    a.append({'money':b, 'type':c, 'month':d})

def expense_list(a):
    print('Your Expense List is Here:')
    for i in a:
        print(f'Amount: {i["money"]} category: {i["type"]} Month: {i["month"]}')

def total_expenses(a):
    return sum(map(lambda a: a['money'], a))

def expenses_list_by_category(a,b):
    return list(filter(lambda y: y['type'] == b, a))

def total_expense_by_category(a,b):
    if lambda y: y['type'] == b:
        return sum(map(lambda y: y['money'] ,a))
    
def total_expense_by_month(a,b):
    if lambda y: y['month'] == b:
        return sum(map(lambda y: y['money'] ,a))

def main():
    a = [] 

    print()
    print('Welcome To The Expense Tracker!')
    print()
    
    while True:
        user_input = input('Choose From The Below Options!\n1.Add Expenses\n2.Show Expenses List\n3.Show Total Expense Amount\n4.Filter Expenses List By Categories\n5.Filter Expenses List By Month.\n6.Filter Total Expense By Category.\n7.Filter Total Expense By Month.\n8.Exit.\n\n')
        
        if user_input == '1':
            amount = float(input('Enter The Amount: '))
            category_name = input('Enter The Category: ').lower()
            month_name = input('Enter The Month: ').lower()
            expense(a, amount, category_name, month_name)
            print()
        elif user_input == '2':
            print(expense_list(a))
            print()        
        elif user_input == '3':
            print(f'\nYour Total Expense Is Here:\n{total_expenses(a)}')
            print()
        elif user_input == '4':
            catagory_input = input('Input The Catagory name:\n ').lower()
            x = expenses_list_by_category(a,catagory_input)
            expense_list((x))
            # for i in a:
            #     if i['type'] == catagory_input:
            #         print(f'Amount: {i["money"]} category: {i["type"]} Month: {i["month"]}')
            print()
        elif user_input == '5':
            month_input = input('Input The Month name: ').lower()
            # expenses_list_by_category(a,month_input)
            # expense_list(expenses_list_by_category)
            for i in a:
                if i['month'] == month_input:
                    print(f'Amount: {i["money"]} category: {i["type"]} Month: {i["month"]}')
            print()
        elif user_input == '6':
             catagory_input_for_total = input('Input The Catagory name:\n ').lower()
             print(f'Your Total Expense In This Category:\n{total_expense_by_category(a,catagory_input_for_total)}')
        elif user_input == '7':
             month_input_for_total = input('Input The Month name:\n ').lower()
             print(f'Your Total Expense In This Category:\n{total_expense_by_month(a,month_input_for_total)}')
        else:
            break
    print()
    print('Thank You For Using Our Program!\nHope It Was Useful To You.')
        
main()

