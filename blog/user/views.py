from .serializer import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


# Create your views here.

# Register Api
class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload': serializer.errors, 'status': 400, 'message': 'Something went Wrong'})
        serializer.save()
        #user=User.objects.get(username=serializer.data['username'])
        #token_obj,created = Token.objects.get_or_create(user=user)

        return Response({'payload':serializer.data,'status':201,'message':'User is Register Successfully'})


class Login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error':'Please provide both the password and username', 'status': 400})

        user = authenticate(request,username=username,password=password)

        if not user:
            return Response({'error': 'invalid Credential', 'status': 404})
        token_obj,created = Token.objects.get_or_create(user=user)

        return Response({"status": 200,'token':str(token_obj),
                         "massage": "your are successfully logged in"})


