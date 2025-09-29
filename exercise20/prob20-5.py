from functools import partial


class Discount:

    def apply_discount(self, price):
        return price * 0.9


class VIPDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.8


def fixed_price():
    return 100


get_fixed_price = partial(fixed_price)

regular_discount = Discount()
vip_discount = VIPDiscount()

original_price = get_fixed_price()
regular_discounted_price = regular_discount.apply_discount(original_price)
vip_discounted_price = vip_discount.apply_discount(original_price)

print(f"Original price: ${original_price}")
print(f"Price after regular discount: ${regular_discounted_price:.2f}")
print(f"Price after VIP discount: ${vip_discounted_price:.2f}")
