purchase = float(input("Enter the purchase amount: "))
final_price = 0
discount = 0

if purchase <= 100.00:
  final_price = purchase
  print("You didn't get a discount.")
elif purchase > 100.00 and purchase <= 300.00:
  discount = purchase * 0.10
  final_price = purchase - discount
  print("You got a 10% discount.")
else:
  discount = purchase * 0.15
  final_price = purchase - discount
  print("You got a 15% discount.")

print(f"Your final price is: ${final_price:.2f}")