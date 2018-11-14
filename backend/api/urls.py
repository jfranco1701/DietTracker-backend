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
	url(r'^register', csrf_exempt(controllers.Register.as_view())),
	url(r'^weight/(?P<userid>[0-9]+)/((?P<startdate>\d{4}-\d{2}-\d{2})/(?P<enddate>\d{4}-\d{2}-\d{2})$)', csrf_exempt(controllers.WeightList.as_view())),
	url(r'^weight/(?P<pk>[0-9]+)', csrf_exempt(controllers.WeightDetail.as_view())),
    url(r'^weight', csrf_exempt(controllers.WeightList.as_view())),
	url(r'^foods/(?P<pk>[0-9]+)', csrf_exempt(controllers.FoodDetail.as_view())),
	url(r'^foods', csrf_exempt(controllers.FoodList.as_view())),
	url(r'^meals/(?P<pk>[0-9]+)', csrf_exempt(controllers.MealDetail.as_view())),
	url(r'^meals', csrf_exempt(controllers.MealList.as_view())),
    url(r'^users', csrf_exempt(controllers.UserList.as_view())),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^', include(router.urls)),
]
