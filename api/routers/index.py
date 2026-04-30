from . import customer, orders, analytics, item_ingredients, order_promo

def load_routes(app):
    app.include_router(customer.router)
    app.include_router(orders.router)
    app.include_router(analytics.router)
    app.include_router(item_ingredients.router)
    app.include_router(order_promo.router)