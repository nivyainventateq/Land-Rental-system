from django.contrib.auth import authenticate
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.views import APIView
from testapp.models import User,Property
from testapp.serializers import UserSerializers, PropertySerializers, LoginSerializer
from rest_framework.authtoken.models import Token
from .exception import IncorrectData,IncorrectAuthCredentials


class Register_User(APIView):

    def get(self,request,*args,**kwargs):
        queryset=User.objects.all()
        serializer=UserSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            mail = EmailMessage("verify", 'hdgfhjdg', to=serializer.email)
            mail.send()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

register=Register_User.as_view()

class Register_User1(APIView):

    serializer_class=UserSerializers

    def get_objects(self,id):
        try:
            return User.objects.get(id=id)
        except:
            return Response(status=404)

    def get(self,request,id):
        x=self.get_objects(id)
        serializer=self.serializer_class(x)
        return Response(serializer.data)

    def put(self,request,id):
        print(request.data)
        x=self.get_objects(id)
        serializer=self.serializer_class(x,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        x=self.get_objects(id)
        x.delete()
        return Response(status=204)

register1=Register_User1.as_view()


class Property_Details(APIView):

    serializer_class = PropertySerializers

    def get(self,request,*args,**kwargs):
        queryset=Property.objects.all()
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

details=Property_Details.as_view()

class Property_Details1(APIView):

    serializer_class=PropertySerializers

    def get_objects(self,id):
        if (id==id):
            return User.objects.get(id=id)
        else:
            return Response(status=404)

    def get(self, request, id):
        x = self.get_objects(id)
        serializer = self.serializer_class(x)
        return Response(serializer.data)

    def put(self,request,id):
        x=self.get_objects(id)
        serializer=self.serializer_class(x,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        x=self.get_objects(id)
        x.delete()
        return Response(status=204)

details1=Property_Details1.as_view()


class Loginapi(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request,username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'Token':token.key,'user_id': user.pk, 'email': user.email},status=status.HTTP_200_OK)
            else:
                 raise IncorrectAuthCredentials(detail="Incorrect authentication credentials", code=401)
        else:
            raise IncorrectData(detail=serializer.errors, code=400)


loginapi = Loginapi.as_view()



class Logoutapi(APIView):

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"success": ("Successfully logged out.")},status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

logoutapi=Logoutapi.as_view()