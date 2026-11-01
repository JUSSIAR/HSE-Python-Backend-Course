from models.product import Product

def select_products_by_category(products: list[Product], category: str) -> list[Product]:
    return [p for p in products if p.category == category]
