from starlette.middleware.cors import CORSMiddleware

from . import (customer, orders, analytics,
               item_ingredients, order_promo,
               ingredients, menu_items, order_items,
               payments, promo_codes, reviews)

def load_routes(app):
    app.include_router(customer.router)
    app.include_router(orders.router)
    app.include_router(analytics.router)
    app.include_router(item_ingredients.router)
    app.include_router(order_promo.router)
    app.include_router(ingredients.router)
    app.include_router(payments.router)
    app.include_router(promo_codes.router)
    app.include_router(reviews.router)
    app.include_router(order_items.router)
    app.include_router(menu_items.router)