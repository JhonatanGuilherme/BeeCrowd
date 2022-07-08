purchased_products = int(input())
products_description = ((1001, 1002, 1003, 1004, 1005), (1.5, 2.5, 3.5, 4.5, 5.5))
purchase_amount = 0
for _ in range(purchased_products):
  product_name, product_quantity = map(int, input().split())
  purchase_amount += product_quantity * products_description[1][products_description[0].index(product_name)]
print(f"{purchase_amount:.2f}")