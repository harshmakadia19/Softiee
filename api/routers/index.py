from . import customer, orders, analytics

def load_routes(app):
    app.include_router(customer.router)
    app.include_router(orders.router)
    app.include_router(analytics.router)