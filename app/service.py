# service
from .models import Order
from .logger import logger

def create_order(db, customer, amount, bug_mode=None):

    logger.debug("Starting order creation")

    # Inject controlled persistence divergence
    stored_amount = amount
    if bug_mode == "silent_db_bug":
        stored_amount = amount * 100
 
    # Inject inconsistent persistence format
    if bug_mode == "format_bug":
        stored_amount = int(amount * 100)

    # Inject null handling failure
    if bug_mode == "null_bug":
        customer_name = customer["name"]
    else:
        customer_name = customer if isinstance(customer, str) else str(customer)

    order = Order(
        customer=customer_name,
        amount=stored_amount,
        status="CREATED"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    # Inject incomplete observability signal
    if bug_mode == "missing_log":
        logger.info("Order created")
    else:
        logger.info(f"Order created - id={order.id}")

    return order
