from expense import Expense
import calendar
import datetime

def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    
 
    #get user input for expense
    expense = get_user_expense()
    
    
    #write into file
    save_expense_to_file(expense ,expense_file_path )
    
    #Read file and summarize expence 
    Summarize_expenses(expense_file_path , budget)
  
    
def get_user_expense():
    print(f"Getting the user expense")
    expense_name = input("Enter Expense Name :")
    expense_amount = float(input("Enter Expense amount :"))
    print(f"You've Entered {expense_name} , {expense_amount}")    
    
    expense_categories = [ "🧆Food" , "🏠Home" , "🧑‍💼Work" , "🔫Fun" , "Misc" ]
    
    while True:
        print("Select a Catogory :")
        for i , category_name in enumerate(expense_categories):
            print(f" {i +1 } {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a Category Number  {value_range}:")) - 1
        
        if selected_index in range(len(expense_categories)):
           selected_category = expense_categories[selected_index]
           new_Expense = Expense(name = expense_name , category= selected_category , amount= expense_amount)
           return new_Expense
        else:
            print("Invalid Category , Please try again!")
            
def save_expense_to_file(expense : Expense , expense_file_path):
    print(f"Saving user expense : {expense} to {expense_file_path}")
    with open(expense_file_path , "a") as f :
        f.write(f"{expense.name} ,{expense.amount} ,{expense.category}\n")  
        
def Summarize_expenses(expense_file_path , budget):
    print(f"Summarising user Expensive:")
    expenses: list[Expense] = []
    with open(expense_file_path , "r") as f:
        lines = f.readlines()
        for line in lines:
            name, amount, category = line.strip().split(",")
            line_expense = Expense(
                name=name,
                category=category,
                amount=float(amount)
            )
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category  
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f"   {key} : ${amount:.2f}")
        
    total_spent = sum([ex.amount for ex in expenses])
    print(f"You've spent {total_spent:.2f} for this month!:")
    
    remaining_budget = budget - total_spent
    print(f"Budget remaining {remaining_budget:.2f} for this month!:")
    
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    
    daily_budget = remaining_budget/remaining_days
    print(green(f"Budget per day {daily_budget:.2f}"))    
    
def green(text):
    return f"\033[92m{text}\033[0m"
if __name__ == "__main__":
    main()
