from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

        self.session.modified = True

    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = quantity

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = product_quantity

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        prod_ids = self.cart.keys()
        products = Product.objects.filter(id__in=prod_ids)
        return products

    def get_quantity(self):
        quantities = self.cart
        return quantities
