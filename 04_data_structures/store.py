#Adicione uma nova informação: a categoria do produto
#Imprima o dicionário atualizado

product_store = {
    "name" : "Carrot cake",
    "price": 12.99,
    "storage" : 8
    }

print("====== GABI'S STORE ======\n")
print("Welcome to our store. This is our principle product today: \n")
print("Name: " + product_store["name"])
print(f"Price: {product_store['price']}")
print(f"How many do we have? {product_store['storage']}")

product_store["price"] = 9.99
product_store["category"] = "cakes"

print("\n We are on sale today! \n")
print("Name: " + product_store["name"])
print(f"New price: {product_store['price']}")
print(f"How many do we have? {product_store['storage']}")
print("What is the category of the product: " + product_store["category"])