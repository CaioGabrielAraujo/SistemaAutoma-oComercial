from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views
app_name = 'product'
urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name="cadastrarProduto"),
    url(r'^list_products/$', views.list_products, name="listproducts"),
    url(r'^create_category/', views.create_category, name="createcategory"),
    url(r'^edit_products/(?P<product_id>[0-9]+)/', views.edit_product, name="edit_product"),
    url(r'^delete_products/(?P<product_id>[0-9]+)/', views.delete_products, name="delete_products"),
    url(r'^delete_category/(?P<product_id>[0-9]+)/', views.delete_category, name="deletecategory"),
    url(r'^delete_sell/(?P<product_id>[0-9]+)/', views.delete_sell, name="deletesell"),
    url(r'^create_sell/', views.sell_product, name="sellproduct"),
]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
