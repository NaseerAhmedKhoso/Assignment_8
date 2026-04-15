#Assignment 2: Product Price Manager Task:

products={
    "mouse": 600,
    "CPU": 7000,
    "Charger": 1500
}
for data in products.keys():
    print(data,":", products[data])
products["keyboard"]=1100
print("new product add:",products)
products["mouse"]=800
print("value of mouse is updated:" ,products)
total=(sum(products.values()))
print("Total price:",total)
