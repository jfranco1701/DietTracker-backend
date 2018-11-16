from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api import controllers
from django.views.decorators.csrf import csrf_exempt

from controllers import WeightViewSet

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

weight_list = WeightViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
weight_detail = WeightViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    #url(r'^breeds', csrf_exempt(controllers.BreedList.as_view())),
	url(r'^register/', csrf_exempt(controllers.Register.as_view())),
	url('weights/', weight_list, name='weight-list'),
    url('weights/(?P<pk>[0-9]+)/', weight_detail, name='weight-detail'),
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
