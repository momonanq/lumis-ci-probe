import stripe


def charge(amount):
    return stripe.Charge.create(amount=amount)
