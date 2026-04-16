from . import orders, order_item, review, order_promo, customer, ingredient, item_ingredient, menu_item, payment, promo_code

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    ingredient.Base.metadata.create_all(engine)
    item_ingredient.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    order_item.Base.metadata.create_all(engine)
    order_promo.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promo_code.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)


