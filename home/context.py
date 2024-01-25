from a_panel.models import *
from home.models import *

def include_categories(request):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    wish_product = Product.objects.all()[3:10]
    products = Product.objects.all()[11:17]
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        wishlist = Wishlist.objects.filter(user = request.user)

    else:
        cart = None
        wishlist = None

    return {
        'cart':cart,
        'categories':category,
        'subcategories':subcategory,
        'wish_product':wish_product,
        'wish':wishlist,
        'product_2':products
        
        }