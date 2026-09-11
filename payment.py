import random
def process_payment(method):
    transaction_id = "TXN" + str(random.randint(100000,999999))
    return {
        "status":"success",
        "transaction":transaction_id,
        "method":method
    }