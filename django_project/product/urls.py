from django.conf.urls import url

from . import views
app_name = 'product'
urlpatterns = [
    url(r'^cadastrar/', views.cadastrar, name="cadastrarProduto"),
    url(r'^list_products/$', views.list_products, name="listproducts"),
    url(r'^create_category/', views.create_category, name="create_category"),


]
