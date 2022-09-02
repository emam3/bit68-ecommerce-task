from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usersApp.views import registerUser, loginUser

router = DefaultRouter()
router.register('userRegister' , registerUser)


urlpatterns = [
    path('loginUser/', loginUser.as_view()),
    path('' ,include(router.urls))
]