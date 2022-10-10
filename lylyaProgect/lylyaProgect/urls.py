from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from admin_panel.views import index_admin_panel
from getData.models import Products
from getData.views import indexData, loadAPI_product, PronuctsView, CategoryView, SubcategoryView, PurchaseList
from orders.views import AddOrder

router = SimpleRouter()

router.register('api/products', PronuctsView)
router.register('api/category', CategoryView)
router.register('api/subcategory', SubcategoryView)
# router.register('api/products_category', PurchaseList)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_panel/', index_admin_panel),
    path('update/', loadAPI_product),
    path('', indexData),
    path('api/order', AddOrder.as_view()),
    path('api/products_category', PurchaseList.as_view())
]

urlpatterns += router.urls
