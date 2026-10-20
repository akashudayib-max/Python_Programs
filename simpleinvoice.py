product_name =str(input("enter the name: "))
print("Product name:", product_name)
unit_price =int(input("enter the price :"))
print("Unit price:", unit_price)
quantity =int(input("enter the quantity :"))
print("Quantity:", quantity)
discount =int(input("enter the discount :"))
print("Discount:", discount)
subtotal = unit_price * quantity
print("Subtotal:", subtotal)
final_bill = subtotal - discount
print("Final bill:", final_bill)