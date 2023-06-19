"""
RETURN ON INVESTMENT FOR RENTAL PROPERTY
biggerpockets.com/analyzerentalproperty
biggerpockets.com/analysis

FOUR SQUARE METHOD
FOR DUPLEX
if rent = $1000.00 for room
1. INCOME
-- RENTAL INCOME = $2000.00
-- LAUNDRY
-- STORAGE
-- MISC

TOTAL MONTHLY INCOME = $2000
num_rooms = input(how many rooms are you renting?)
cost_room = input(how much are you charging for each room?)
other_charges = input(if you are charging for laundry, storage, etc, what is that total?)
total_monthly_income = num_rooms + cost_room + other_charges

2. EXPENSES
-- TAX = $150.00
-- INSURANCE = $100.00
-- UTILITIES = $0
    - ELECTRIC
    - WATER
    - SEWER
    - GARBAGE
    - GAS
-- HOA == $0
-- LAWN/SNOW CARE = $0
-- VACANCY = $100.00
-- REPAIRS = $100.00
-- CAPITAL EXPENDITURES (CAPEX) = $100
-- PROPERTY MANAGE = $200
-- MORTAGE = $860

TOTAL MONTHLY EXPENSES = $1610

tax = input(enter property tax)
insurance = input(enter insurance cost)
utilities = input(if utilities is fixed, enter amount. if not charging utilites, enter 0)
hoa = input(enter hoa fee?)
care = input(enter groundskeeping fees:)
mortgage = input(enter mortgage payment)
vacancy = 100
repairs = 100
capex = 100
property_manage = 200

total_monthly_expenses = tax + insurance + utilities + hoa + care + mortgage + vacancy + repairs + capex + property_manage






3. CASH FLOW
INCOME - EXPENSES:
$2000 - $1610 = $390

TOTAL MONTHLY CASHFLOW = $390

total_monthly_cashflow = total_monthly_income - total_monthly_expenses
print(f"Your total monthly cashflow for this property is {total_monthly_cashflow}")

down_payment = input(enter down payment:)
closing_costs = input(enter closing costs:)
rehab_budget = input(enter total rehabilitation and repair cost:)
other_costs = input(enter any other costs incurred: )
total_investment = down_payment + closing_costs + rehab_budget + other_costs
print(f"Your total investment for this property is {total_investment}")

roi = (total_monthly_cashflow * 12) / total_investment
print("Your return on investment for this property is {roi}")

4. CASH ON CASH ROI
DOWN PAYMENT = $40000
CLOSING COSTS = $3000
REHAB BUDGET = $7000
MISC OTHER = $0

TOTAL INVESTMENT = $50000
$390 X 12 = $4680
ANNUAL CASH FLOW / TOTAL INVESTMENT
$4680 / $50000 = 9.36 %

CASH ON CASH ROI = 9.36 %


"""


class Investment():
    def __init__(self):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_monthly_cashflow = 0
        self.properties = {}
        self.roi_ = None


    def income(self):
        num_rooms = int(input("how many rooms are you renting?: "))
        cost_room = int(input("how much are you charging for each room?: "))
        other_charges = int(input("if you are charging for laundry, storage, etc, what is that total?: "))
        self.total_monthly_income = num_rooms + cost_room + other_charges
        print(f"\nFor this property, the total monthly income is ${self.total_monthly_income}\n")

    def expenses(self):
        tax = int(input("enter property tax: "))
        insurance = int(input("enter insurance cost: "))
        utilities = int(input("if utilities is fixed, enter amount. if not charging utilites, enter 0: "))
        hoa = int(input("enter hoa fee?: "))
        care = int(input("enter groundskeeping fees: " ))
        mortgage = int(input("enter mortgage payment: " ))
        vacancy = 100
        repairs = 100
        capex = 100
        property_manage = 200
        self.total_monthly_expenses = tax + insurance + utilities + hoa + care + mortgage + vacancy + repairs + capex + property_manage
        print(self.total_monthly_expenses)
        print(f"\nFor this property, the total monthly expenses are ${self.total_monthly_expenses}\n")

    def roi(self):
        self.total_monthly_cashflow = self.total_monthly_income - self.total_monthly_expenses
        if self.total_monthly_cashflow < 0:
            neg = input("Sheeesh, your total cashflow for this property is negative...do you still give a dang?(y/n) ")
            if neg == 'y':
                pass
            if neg == 'n':
                print("Yeah, probably a good idea")
                return go.run()
        else:
            pass
        print(f"Your total monthly cashflow for this property is {self.total_monthly_cashflow}\n")
        down_payment = int(input("enter down payment: " ))
        closing_costs = int(input("enter closing costs: " ))
        rehab_budget = int(input("enter total rehabilitation and repair cost: " ))
        other_costs = int(input("enter any other costs incurred: " ))
        total_investment = down_payment + closing_costs + rehab_budget + other_costs
        print(f"\nYour total investment for this property is ${total_investment}")
        self.roi_ = (self.total_monthly_cashflow * 12) / total_investment



        property_details = {'Total Monthly Income':self.total_monthly_income,
                    'Total Monthly Expenses':self.total_monthly_expenses,
                    'Total Monthly Cashflow': self.total_monthly_cashflow,
                    'Return On Investment':self.roi_
        }

        property_name = input("\nWhat is this properties address?: ")
        self.properties[property_name] = property_details
        print(f"""\nYour investment property has been added to your history! 
Add another property or head to the homepage to view your history and compare investments!\n""")
        while True: 
            response = input("Would you like to look at another property?(y/n) ")
            if response == 'y':
                self.income()
                self.expenses()
                self.roi()
                return
            elif response == 'n':
                while True:
                    response2= input("\nWould you like to return to the home page? (y/n): ").strip().lower()
                    if response2 == 'y':
                        go.run()
                    elif response2 == 'n':
                        print("Word")
                        break
                    else:
                        print("What")
                        response2
            else:
                print("What")
                response

    def history(self):
        print(f"\nYour investment properties:\n")
        for key, value in self.properties.items():
            print(key)
            for detail, detail2 in value.items():
                print(f"{detail}:{detail2}")
        print(f"Your return on investment for this property is {self.roi_}")
        while True: 
            response = input("\nWould you like to look at another property?(y/n) ")
            if response == 'y':
                self.income()
                self.expenses()
                self.roi()
                return
            elif response == 'n':
                while True:
                    response2= input("Would you like to return to the home page? (y/n): ").strip().lower()
                    if response2 == 'y':
                        go
                    elif response2 == 'n':
                        print("Word")
                        break
                    else:
                        print("What")
                        response2
            else:
                print("What")
                response


    def run(self):
        while True:
            print("""Welcome to J-Money's rental property investment calculator, \nwhere you can find if that place you've been looking at is worth a few dubloons over time. 
What would you like to do?\n(Simply enter the number of your choice)\n""")
            print("""
            1. Calculate property's return on investment
            2. Check my history
            3. Quit the calculator
            """)
            response = int(input(">>>: "))
            if response == 1:
                print("Lets do this!!!")
                self.income()
                self.expenses()
                self.roi()
            elif response == '2' or '2.':
                self.history()
            elif response == 3:
                print("Sick")
                break
            else:
                print("What")
                response


















go = Investment()
go.run()
