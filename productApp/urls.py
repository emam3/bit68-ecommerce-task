from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productApp.views import createProductView, createcartItemView,createOrderView,getAllProducts, getcart, getUserOrders


router = DefaultRouter()
router.register('createProductView' , createProductView)
router.register('createCartItemView' , createcartItemView)
router.register('createOrderView' , createOrderView)
router.register('getAllProducts' , getAllProducts)
router.register('getCart' , getcart)
router.register('getUserOrders' , getUserOrders)

urlpatterns = [
    # path('loginUser/', loginUser.as_view()),
    path('' ,include(router.urls))
]