from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()
# Products database (list of dictionaries)
products = [
    {"id": 1, "name": "Laptop", "price": 80000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 500, "category": "Accessories", "in_stock": True},
    {"id": 3, "name": "Keyboard", "price": 1500, "category": "Accessories", "in_stock": True},
    {"id": 4, "name": "Monitor", "price": 12000, "category": "Electronics", "in_stock": False},
    # Newly added products
    {"id": 5, "name": "Laptop Stand", "price": 1200, "category": "Accessories", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 4500, "category": "Accessories", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 3000, "category": "Electronics", "in_stock": True}
]
# API endpoint to get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


#Q.2] ADD A CATEGORY FILTER ENDPOINT
Electronics = {"Product1": "Mobile Phone", 
     "Product2": "Refrigerator",
     "Product3": "Laptop",
     "Product4": "TV",
     "Product5": "Microwave",
     "Product6": "Hair dryer",
     "Product7": "Camera",
     "Product8": "Game console",
     "Product9": "Trimmer",
     "Product10": "Vacuum cleaner"}
Stationary = {"Product1": "Pencils", 
     "Product2": "Pens",
     "Product3": "Notebooks",
     "Product4": "Colour paints",
     "Product5": "Staplers",
     "Product6": "Scissors",
     "Product7": "Glue",
     "Product8": "Binders",
     "Product9": "Paint Brushes",
     "Product10": "Sticky notes"}  
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    if category_name.lower() == "electronics":
        return {"products": Electronics}
    elif category_name.lower() == "stationary":
        return {"products": Stationary}
    else:
        return {"error": "No products found in this category"}


#Q.3] SHOW ONLY IN-STOCK PRODUCTS
products = {
    "ice_cream" : 5,
    "toothpaste": 5,
    "maggi": 10,
    "soap": 6,
    "detergent": 8,
    "wheat_flour": 7,
    "rice_grain": 0,
    "biscuits": 0,
    "shampoo": 2,
    "sanitary_napkins": 0,
    "tissue_roll": 0,
    "ceramic_vase": 1,
    "paintings_by_RajaRaviVerma": 1
}
@app.get("/products/instock")
def in_stock():
    in_stock_products = {}
    for product in products:
        if products[product] != 0:
            in_stock_products[product] = products[product]
    return in_stock_products


#Q.4] BUILD A STORE INFO ENDPOINT
Electronics = {
 "Mobile Phone": True,
 "Refrigerator": True,
 "Laptop": True,
 "TV": False,
 "Microwave": True,
 "Hair dryer": True,
 "Camera": False,
 "Game console": True,
 "Trimmer": True,
 "Vacuum cleaner": True
}
Stationary = {
 "Pencils": True,
 "Pens": True,
 "Notebooks": True,
 "Colour paints": False,
 "Staplers": True,
 "Scissors": True,
 "Glue": True,
 "Binders": False,
 "Paint Brushes": True,
 "Sticky notes": True
}

products = {
 "Electronics": Electronics,
 "Stationary": Stationary
}

@app.get("/store/summary")
def summary():
    total_products = 0
    in_stock = 0
    out_of_stock = 0
    categories = []
    for category in products:
        categories.append(category)
        for item in products[category]:
            total_products += 1
            if products[category][item] == True:
                in_stock += 1
            else:
                out_of_stock += 1
    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

#Q.5] SEARCH PRODUCT BY NAME
products = {
    "Electronics": [
        "Mobile Phone",
        "Refrigerator",
        "Laptop",
        "TV",
        "Microwave",
        "Hair Dryer",
        "Camera",
        "Game Console",
        "Trimmer",
        "Vacuum Cleaner",
        "Wireless Mouse"
    ],
    "Stationary": [
        "Pencils",
        "Pens",
        "Notebooks",
        "Colour Paints",
        "Staplers",
        "Scissors",
        "Glue",
        "Binders",
        "Paint Brushes",
        "Sticky Notes",
        "Book"
    ]
}

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matches = []
    for category in products:
        for product in products[category]:
            if keyword.lower() in product.lower():
                matches.append(product)
    if len(matches) == 0:
        return {"message": "No products matched your search"}
    return {
        "matches": matches,
        "total_matches": len(matches)
    }


#Q.6 - BONUS] CHEAPEST AND MOST EXPENSIVE PRODUCT
products = [
    {"name": "Pen Set", "price": 49},
    {"name": "Notebook", "price": 120},
    {"name": "Wireless Mouse", "price": 799},
    {"name": "Mechanical Keyboard", "price": 2499},
    {"name": "Laptop Stand", "price": 999}
]
@app.get("/products/deals")
def product_deals():
    best_deal = min(products, key=lambda x: x["price"])
    premium_pick = max(products, key=lambda x: x["price"])
    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }
