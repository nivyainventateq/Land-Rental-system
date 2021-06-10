from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from testapp.models import User,Property


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    class Meta:
        model=User
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        address = validated_data.pop('address')
        phone = validated_data.pop('phone')
        city = validated_data.pop('city')
        aadhar = validated_data.pop('aadhar')
        roles_id=validated_data.pop('roles_id')
        user = User.objects.create(email=email,password=password,username=username,address=address,phone=phone,city=city,aadhar=aadhar,roles_id=roles_id)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.aadhar = validated_data.get('aadhar', instance.aadhar)
        instance.roles_id = validated_data.get('roles_id', instance.roles_id)
        instance.save()
        return instance


class PropertySerializers(serializers.ModelSerializer):

    class Meta:
        model=Property
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)
        user_id = validated_data['user_id']
        soil_id = validated_data['soil_id']
        water_id = validated_data['water_id']
        area = validated_data['area']
        city = validated_data['city']
        images = validated_data['images']
        price = validated_data['price']
        description = validated_data['description']
        x = Property.objects.create(user_id=user_id,soil_id=soil_id,water_id=water_id,area=area,city=city,images=images,price=price,description=description)
        x.save()
        return x

    def update(self, instance, validated_data):
        print(validated_data)
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.soil_id=validated_data.get('soil_id',instance.soil_id)
        instance.water_id=validated_data.get('water_id',instance.water_id)
        instance.area=validated_data.get('area',instance.area)
        instance.city=validated_data.get('city',instance.city)
        instance.images=validated_data.get('images',instance.images)
        instance.price=validated_data.get('price',instance.price)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256, required=True)
    password = serializers.CharField(required=True, min_length=5)

    class Meta:
        model = User


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    message = {'bad_token': ('Token is expired or invalid') }

    def validate(self, attr):
        self.token = attr['refresh']
        return attr

