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
	url(r'^weight/(?P<userid>[0-9]+)/((?P<startdate>\d{4}-\d{2}-\d{2})/(?P<enddate>\d{4}-\d{2}-\d{2})$)', csrf_exempt(controllers.WeightList.as_view())),
	url(r'^weight/(?P<pk>[0-9]+)', csrf_exempt(controllers.WeightDetail.as_view())),
    url(r'^weight', csrf_exempt(controllers.WeightList.as_view())),
    url(r'^users', csrf_exempt(controllers.UserList.as_view())),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^', include(router.urls)),
]
