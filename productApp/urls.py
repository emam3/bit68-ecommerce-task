from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productApp.views import createProductView, createCardItemView,createOrderView,getAllProducts, getCard, getUserOrders


router = DefaultRouter()
router.register('createProductView' , createProductView)
router.register('createCardItemView' , createCardItemView)
router.register('createOrderView' , createOrderView)
router.register('getAllProducts' , getAllProducts)
router.register('getCard' , getCard)
router.register('getUserOrders' , getUserOrders)

urlpatterns = [
    # path('loginUser/', loginUser.as_view()),
    path('' ,include(router.urls))
]