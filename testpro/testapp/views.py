from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from testapp.models import User
from testapp.serializers import UserSerializers


class Register_User(APIView):

    def get(self,request,*args,**kwargs):
        query_set=User.objects.all()
        x=UserSerializers(query_set,many=True)
        return Response(x.data)

    def post(self,request,*args,**kwargs):
        print(request.data)
        x=UserSerializers(data=request.data)
        if x.is_valid(raise_exception=True):
            x.save()
            return Response(x.data,status=status.HTTP_200_OK)
        else:
            return Response(x.errors,status=status.HTTP_400_BAD_REQUEST)


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






