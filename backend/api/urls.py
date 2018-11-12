from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    #url(r'^breeds', csrf_exempt(controllers.BreedList.as_view())),
	url(r'^usercreate', csrf_exempt(controllers.UserCreate.as_view())),
    url(r'^users', csrf_exempt(controllers.UserList.as_view())),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^', include(router.urls)),
]
