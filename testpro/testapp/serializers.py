from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from testapp.models import User, property


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])
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
        user = User.objects.create(email=email,username=username,address=address,phone=phone,city=city,aadhar=aadhar)
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
        instance.save()
        return instance


class property(serializers.ModelSerializer):
    class Meta:
        modle=property
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)

        user_id = validated_data.pop('user_id')
        area = validated_data.pop('area')
        city = validated_data.pop('city')
        images = validated_data.pop('images')
        price = validated_data.pop('price')
        description = validated_data.pop('description')
        type_of_soil = validated_data.pop('type_of_soil')
        water = validated_data.pop('water')
        property=property.objects.create(user_id=user_id,area=area,city=city,images=images,price=price,description=description,type_of_soil=type_of_soil,water=water)
        property.save()
