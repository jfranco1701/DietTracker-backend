from rest_framework import serializers
from api.models import Dog, Breed, BREED_SIZES, RATING_VALUES

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

class DogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    age = serializers.IntegerField(required=False)
    breed = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Breed.objects.all())
    gender = serializers.CharField(required=False, max_length=50)
    color = serializers.CharField(required=False, max_length=50)
    favoritetoy = serializers.CharField(required=False, max_length=100)
    favoritefood = serializers.CharField(required=False, max_length=100)

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.save()
        return instance
