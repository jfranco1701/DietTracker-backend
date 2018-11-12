from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
#from api.models import Breed, BREED_SIZES, RATING_VALUES
'''
class BreedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    size = serializers.ChoiceField(choices=BREED_SIZES)
    friendliness = serializers.ChoiceField(choices=RATING_VALUES)
    trainability = serializers.ChoiceField(choices=RATING_VALUES)
    sheddingamount = serializers.ChoiceField(choices=RATING_VALUES)
    exerciseneeds = serializers.ChoiceField(choices=RATING_VALUES)

    def create(self, validated_data):
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance
'''
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
