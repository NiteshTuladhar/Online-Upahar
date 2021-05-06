
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

   #Products Action API Urls
   path('wishlist/', views.getWishlist),
   path('add_remove_wishlist/<int:id>', views.addRemoveWishlist),
   path('delete_wishlist_item/<int:id>', views.deleteWishlistItem),

]