from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from api.models import Weight, Food, Meal, MEAL_TYPES

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)
    last_name = serializers.CharField(required=True, max_length=50)
    first_name = serializers.CharField(required=True, max_length=50)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.last_name = validated_data['last_name']
        user.first_name = validated_data['first_name']
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser', 'is_staff', 'date_joined')

class WeightSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    userweight = serializers.IntegerField(required=True)
    weightdate = serializers.DateField(required=True)

    def create(self, validated_data):
        return Weight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userweight = validated_data.get('userweight', instance.userweight)
        instance.weightdate = validated_data.get('weightdate', instance.weightdate)
        instance.save()
        return instance

    class Meta:
        model = Weight
        fields = ('id', 'userid', 'userweight', 'weightdate', 'timestamp')

class FoodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        return Food.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Food
        fields = ('id', 'name', 'timestamp')

class MealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    userid = serializers.IntegerField(required=True)
    mealdate = serializers.DateField(required=True)
    mealtype = serializers.ChoiceField(required=True, choices=MEAL_TYPES)
    fooditem = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Food.objects.all())
    quantity = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Meal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userid = validated_data.get('userid', instance.userid)
        instance.mealdate = validated_data.get('mealdate', instance.mealdate)
        instance.mealtype = validated_data.get('mealtype', instance.mealtype)
        instance.fooditem = validated_data.get('fooditem', instance.fooditem)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    class Meta:
        model = Meal
        fields = ('id', 'userid', 'mealdate', 'mealtype', 'fooditem', 'quantity', 'timestamp')
