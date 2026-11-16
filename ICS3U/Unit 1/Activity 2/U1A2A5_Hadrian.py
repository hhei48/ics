# source: https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html

tax_bracket=[0, 58523, 117045, 181440, 258482, 1000000000000]
tax_rate=[0.14, 0.205, 0.26, 0.29, 0.33]
total_income_tax=0
print("Welcome to the 2026 Canada federal income tax calculator!")
income=int(input("Please enter your annual taxable income: $"))
for i in range(5):
    bracket_tax=min(income, tax_bracket[i+1])-tax_bracket[i]
    total_income_tax+=bracket_tax*tax_rate[i]
    if(income<=tax_bracket[i+1]):
        break
print(f"Your total federal income tax amount is ${round(total_income_tax, 2)}.")
