
from django.urls import path, include

from django.conf.urls.static import static
from . import views

app_name = 'api'

urlpatterns = [
   
   #Accounts API Urls
   path('signup/', views.signup),
   path('login/',views.login),
   path('verify_account/<int:id>/<str:token>/',views.verify_account),

   #Products API Urls
   path('all_products/',views.AllProductsList.as_view()),
   path('all_products_images/',views.AllProductImageList.as_view()),
   path('product_details/<int:id>',views.getProductDetails),
   path('categories/',views.CategoriesList.as_view()),
   path('main_categories/',views.MainCategoriesList.as_view()),
   path('sub_categories/',views.SubCategoriesList.as_view()),


   #Products AddToCart API Urls
   path('addtocart_productdetails/<str:slug>', views.addToCartDetailsPage),
   path('delete_addtocart/<str:slug>', views.deleteAddToCart),
   path('buynow/<str:slug>', views.buyNow),

   #Products Wishlist API Urls
   path('wishlist/', views.getWishlist),
   path('add_remove_wishlist/<int:id>', views.addRemoveWishlist),
   path('delete_wishlist_item/<int:id>', views.deleteWishlistItem),
   path('addtocart_wishlist_item/<int:id>', views.addWishlistToCart),

   #Contact Mail Send  API Urls
   path('mailsendContact', views.mailsendContact),

   #User's CartPage API Urls
   path('cart_page', views.cartPage),
   path('order', views.usersOrder),
]