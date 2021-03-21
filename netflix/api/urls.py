from django.urls import path
from  .views import index, create,MovieUpdate,api_signup
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("login", obtain_auth_token),
    path("signup/", api_signup),
    path("post",create),
    path("list/", MovieUpdate.as_view())
]