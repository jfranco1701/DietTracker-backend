from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api import controllers
from django.views.decorators.csrf import csrf_exempt

from controllers import WeightViewSet, MealViewSet, FavoriteViewSet

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

meal_list = MealViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
meal_detail = MealViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

favorite_list = FavoriteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

meal_totals = MealViewSet.as_view({
    'get': 'totals'
})

favorite_detail = FavoriteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    #url(r'^breeds', csrf_exempt(controllers.BreedList.as_view())),
	url(r'^register/', csrf_exempt(controllers.Register.as_view())),
    url('weights/(?P<pk>[0-9]+)/', weight_detail, name='weight-detail'),
    url('weights/', weight_list, name='weight-list'),
    url('meals/totals/', meal_totals, name='meal-totals'),
    url('meals/(?P<pk>[0-9]+)/', meal_detail, name='meal-detail'),
	url('meals/', meal_list, name='meal-list'),
    url('favorites/(?P<pk>[0-9]+)/', favorite_detail, name='favorite-detail'),
    url('favorites/', favorite_list, name='favorite-list'),
    url(r'^users', csrf_exempt(controllers.UserList.as_view())),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^', include(router.urls)),
]
