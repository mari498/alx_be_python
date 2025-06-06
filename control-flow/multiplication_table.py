# multiplication_table.py

# طلب إدخال الرقم من المستخدم
number = int(input("Enter a number to see its multiplication table: "))

# استخدام for loop لطباعة جدول الضرب من 1 إلى 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
