from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# creating router object
router = DefaultRouter()

# register khoj the search viewsets with router
router.register('user', views.UserViewSet, basename='user')
# router.register('khoj', views.KhojSearchViewSet, basename='khoj')

urlpatterns = [
    path('', views.MY_ACCOUNNT_LOGIN, name='my_account_login'),
    path('account/register', views.REGISTER, name="handleregister"),
    path('account/login', views.LOGIN, name="handlelogin"),
    path('account/logout', views.LOGOUT, name="handlelogout"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('home', views.HOME, name="home"),

    path('search/', include(router.urls)),
]