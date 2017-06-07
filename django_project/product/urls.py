from django.conf.urls import url

from . import views
app_name = 'product'
urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name="cadastrarProduto"),
    url(r'^list_products/$', views.list_products, name="listproducts"),
    url(r'^create_category/', views.create_category, name="create_category"),
    url(r'^edit_products/(?P<product_id>[0-9]+)/', views.edit_product, name="edit_product"),
    url(r'^delete_products/(?P<product_id>[0-9]+)/', views.delete_products, name="delete_products"),
    url(r'^create_sell/', views.sell_product, name="sellproduct"),
]
