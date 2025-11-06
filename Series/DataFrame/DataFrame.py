import pandas as pd

products = pd.DataFrame({
    "name": ["Laptop", "Phone", "Tablet"],
    "price": [1200, 800, 400],
    "quantity": [5, 10, 8]
})

products["total_value"] = products["price"] * products["quantity"]
products = products.sort_values("total_value", ascending=False)

products.to_csv("products.csv", index=False)
products_loaded = pd.read_csv("products.csv")

print(products_loaded)
