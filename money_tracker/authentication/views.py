from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


# Create your views here.
class RegisterView(APIView):
    authentication_classes = []

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status = HTTP_200_OK)


class LoginView(APIView):
    authentication_classes = []

    def post(self,request):

        req_email = request.data['email'] 
        req_password = request.data['password']
        user = User.objects.filter(email = req_email).first()
        if user is None:
            return Response({'error': "Please enter valid details"},status = HTTP_400_BAD_REQUEST)
        
        if not user.check_password(req_password):
            return Response({'error': "Authentication failed,password didn't match"},status = HTTP_400_BAD_REQUEST)
       
        
        token = get_tokens_for_user(user)
        print("user logged in")
        return Response(
        {
            'token': token,
            'email' : req_email,
            'user_id': user.id

        },
        status=HTTP_200_OK)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class info(APIView):
    def get(self,request):
        user_obj = User.objects.all()
        l = [{
            "id" : obj.id,
            "username" : obj.username,
            "income":obj.budget.income,
            "borrow" : obj.budget.borrow,
            "lend" : obj.budget.lend
        } for obj in user_obj]
        return Response(l,status=HTTP_200_OK)