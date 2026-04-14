from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()


#Q1. FILTER PRODUCTS BY MINIMUM PRICE
products = [
    {"name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    {"name": "USB Hub", "price": 799, "category": "Electronics"},
    {"name": "Laptop", "price": 50000, "category": "Electronics"},
    {"name": "Notebook", "price": 50, "category": "Stationery"},
    {"name": "Pen", "price": 20, "category": "Stationery"}
]

@app.get("/products/filter")
def filter_products(
    min_price: Optional[int] = Query(None),
    max_price: Optional[int] = Query(None),
    category: Optional[str] = Query(None)
) -> List[dict]:
    result = products

    if min_price is not None:
        result = [p for p in result if p["price"] >= min_price]

    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]

    if category is not None:
        result = [p for p in result if p["category"].lower() == category.lower()]
    return result


#Q2. GET ONLY THE PRICE OF THE PRODUCT
products = {
    1: {"name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    2: {"name": "Notebook", "price": 99, "category": "Stationery"},
    3: {"name": "USB Hub", "price": 799, "category": "Electronics"},
    4: {"name": "Laptop", "price": 50000, "category": "Electronics"}
}

@app.get("/products/{product_id}/price")
def get_product_price(product_id: int) -> dict:

    product = products.get(product_id)

    if product is None:
        return {"error": "Product not found"}

    return {
        "name": product["name"],
        "price": product["price"]
    }

#Q3. ACCEPT CUSTOMER FEEDBACK
from pydantic import BaseModel, Field
from typing import Optional, List
feedback_list = []

class CustomerFeedback(BaseModel):
    customer_name: str = Field(..., min_length=2)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=300)

@app.post("/feedback")
def submit_feedback(feedback: CustomerFeedback):

    feedback_list.append(feedback.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback,
        "total_feedback": len(feedback_list)
    }


#Q4. BUILD A PRODUCT SUMMARY DASHBOARD

from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    price: float
    category: str
    in_stock: bool
products: List[Product] = [
    Product(name="Laptop", price=80000, category="Electronics", in_stock=True),
    Product(name="Phone", price=30000, category="Electronics", in_stock=False),
    Product(name="Shoes", price=2000, category="Fashion", in_stock=True),
    Product(name="Watch", price=5000, category="Accessories", in_stock=True),
    Product(name="Headphones", price=1500, category="Electronics", in_stock=False),
]

@app.get("/products/summary")
def get_product_summary():
    
    total_products = len(products)
    
    in_stock_count = sum(1 for p in products if p.in_stock)
    out_of_stock_count = total_products - in_stock_count

    cheapest_product = min(products, key=lambda x: x.price)
    most_expensive_product = max(products, key=lambda x: x.price)

    categories = list(set(p.category for p in products))

    return {
        "total_products": total_products,
        "in_stock_count": in_stock_count,
        "out_of_stock_count": out_of_stock_count,
        "cheapest": {
            "name": cheapest_product.name,
            "price": cheapest_product.price
        },
        "most_expensive": {
            "name": most_expensive_product.name,
            "price": most_expensive_product.price
        },
        "categories": categories
    }


#Q5.
from pydantic import BaseModel, Field, EmailStr
products_db = {
    1: {"name": "Wireless Mouse", "price": 499, "in_stock": True},
    2: {"name": "Keyboard", "price": 999, "in_stock": True},
    3: {"name": "USB Hub", "price": 299, "in_stock": False},
    4: {"name": "Monitor", "price": 7000, "in_stock": True},
}
class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=50)

class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: EmailStr
    items: List[OrderItem]
@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):
    
    confirmed = []
    failed = []
    grand_total = 0

    for item in order.items:
        product = products_db.get(item.product_id)
        if not product:
            failed.append({
                "product_id": item.product_id,
                "reason": "Product not found"
            })
            continue
        if not product["in_stock"]:
            failed.append({
                "product_id": item.product_id,
                "reason": f"{product['name']} is out of stock"
            })
            continue
        subtotal = product["price"] * item.quantity
        grand_total += subtotal

        confirmed.append({
            "product": product["name"],
            "qty": item.quantity,
            "subtotal": subtotal
        })

    return {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": grand_total
    }
