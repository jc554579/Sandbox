def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    Numbers_OfMonths = int(input("How many months? "))

    for month in range(1, Numbers_OfMonths + 1):
        income = float(input("Enter income for months {}:" .format(month)))
        incomes.append(income)
    print_Income_Report(Numbers_OfMonths,incomes)

def print_Income_Report(Numbers_OfMonths,incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, Numbers_OfMonths + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f}\
        Total: ${:10.2f}".format(month, income, total))


main()