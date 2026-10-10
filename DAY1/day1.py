c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32
k = c + 273.15

print(f"Celsius: {c:.2f}°C")
print(f"Fahrenheit: {f:.2f}°F")
print(f"Kelvin: {k:.2f}K")

print("\nConversion Table")
print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")

for c in range(-40, 101, 10):
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f"{c:10.2f} {f:12.2f} {k:10.2f}")

# Q2. Three-Number Analyzer
a, b, c = map(int, input("enter three numbers: ").split())

largest = max(a, b, c)
smallest = min(a, b, c)
average = (a + b + c) / 3
print("Largest:", largest)
print("Smallest:", smallest)
print(f"Average: {average:.2f}")

# Classify another number
n = int(input("Enter another number: "))

if n > 0:
    if n % 2 == 0:
        print("Classification: Positive and Even")
    else:
        print("Classification: Positive and Odd")

elif n < 0:
    if n % 2 == 0:
        print("Classification: Negative and Even")
    else:
        print("Classification: Negative and Odd")

else:
    print("Classification: Zero and Even")

# Q3. Leap Year + Grade Calculator

year = int(input("Year: "))
marks = int(input("Marks: "))

# Check whether the year is a leap year
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# Check whether the marks are valid and calculate the grade
if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Q4. Placement Bill Calculator
prices = []
while True:
    value = input("Enter item price (or 'done' to finish): ")

    if value.lower() == "done":
        break

    prices.append(float(value))

subtotal = sum(prices)
if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0
tax = (subtotal - discount) * 0.05
total = subtotal - discount + tax

print("\nItem         Price")
print("------------------")

for i, price in enumerate(prices, start=1):
    print(f"Item {i:<6} {price:8.2f}")

print("------------------")
print(f"Subtotal:    {subtotal:8.2f}")
print(f"Discount:    {discount:8.2f}")
print(f"Tax:         {tax:8.2f}")
print(f"Final:       {total:8.2f}")

# Q5. Swap Without Temporary Variable

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Before Swap: a = {a}, b = {b}")
a, b = b, a
print(f"After Swap: a = {a}, b = {b}")

# Q6. Simple Interest Report
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
if p < 0 or t < 0:
    print("Invalid input. Principal and time must be non-negative.")
else:
    # Calculate simple interest
    si = (p * r * t) / 100

    # Calculate total amount
    amount = p + si

    # Print the formatted report
    print(f"Principal     : {p:.2f}")
    print(f"Rate          : {r:.2f}%")
    print(f"Time          : {t:.2f} years")
    print(f"Simple Interest: {si:.2f}")
    print(f"Total Amount  : {amount:.2f}")

# Q7. Type Inspector
value = input("Enter a value: ")
print("Original value type :", type(value).__name__)
try:
    num = int(value)
    print("Integer value       :", num)
    print("Integer type        :", type(num).__name__)
except ValueError:
    print("Invalid integer conversion")


try:
    num = float(value)
    print("Float value          :", num)
    print("Float type           :", type(num).__name__)
except ValueError:
    print("Invalid float conversion")

# Q8. Fix the Bug: Input Types

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
total = a + b
print(f"Sum: {total:.2f}")

# Q9. Multiple Assignment Analyzer

a, b, c, d, e = 10, 3.14, "Python", True, None
print(f"Value: {a}     Type: {type(a).__name__}")
print(f"Value: {b}    Type: {type(b).__name__}")
print(f"Value: {c}  Type: {type(c).__name__}")
print(f"Value: {d}    Type: {type(d).__name__}")
print(f"Value: {e}    Type: {type(e).__name__}")

# Q10. Expression Evaluator
a = 19
b = 4
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Demonstrate negative floor division
print("-19 // 4 =", -19 // 4)