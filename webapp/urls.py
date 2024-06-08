from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.homepage,name="home"),
    path('about/',views.aboutpage,name="about"),
    path('contact/',views.contactpage,name="contact"),
    path('product/',views.ourproduct,name="product"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('product_filter/<cat_name>/',views.product_filter,name="product_filter"),
    path('single_page/<int:prd_id>/',views.single_page,name="single_page"),
    path('login_pages/',views.login_pages,name="login_pages"),
    path('save_user/',views.save_user,name="save_user"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('delete_item/<int:p_id>/',views.delete_item,name="delete_item"),




]