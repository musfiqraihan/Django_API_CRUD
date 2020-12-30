from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']









# from rest_framework import serializers
# from .models import Student
#
#
# class StudentSerializer(serializers.ModelSerializer):
#
#     # validators
#     def start_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError("Name Should Start With R")
#
#     # roll = serializers.ImageField(read_only=True) # roll number will not be updated!
#     name = serializers.CharField(validators=[start_with_r])
#
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']
#         # read_only_fields = ['id', 'roll']
#
#         # extra_kwargs = {'name': {'read_only': True}}
#         # Form Validation
#
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
#
#     # object validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'akash' and ct.lower() != 'dhaka':
#             raise serializers.ValidationError('City must be Dhaka')
#         return data

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
