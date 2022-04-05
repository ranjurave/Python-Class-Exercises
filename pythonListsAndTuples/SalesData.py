print("Enter sales figures for this week")
sales_data = []
for x in range(7):
    sales = float(input(f"Day {x+1} : "))
    sales_data.append(sales)
total = 0.0
day = 1
for sale in sales_data:
    total += sale
    print(f"Sale for day {day} is {sale}")
    day += 1
print(f"Total sales for the week is {total}")
print(f"Biggest sale was {max(sales_data)} on day {sales_data.index(max(sales_data))+1}")
print(f"Average sale of the week is {total/len(sales_data)}")