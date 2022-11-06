from django.http import HttpResponse
from django.shortcuts import render
from .models import UserData as UserModel
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .email.email_service import EmailService
from .email.email_msg import EmailMessage
from rest_framework import status


class UserCreation(APIView):
    """ User Store Section Using Ui """
    @staticmethod
    def get(request):
        return render(request, "index.html")

    @staticmethod
    def post(request):
        user_form = UserSerializer(data=request.POST)
        if user_form.is_valid():
            obj = user_form.save()
            emsg = EmailMessage()
            emsg.to = [request.POST['email_id']]
            emsg.subject = "Registration"
            emsg.user = obj
            mail = EmailService.send(emsg, obj)
            if mail == 1:
                return HttpResponse("Please check your email for Verification...")
        return render(request, "index.html",
                      {"error": {d: user_form.errors[d][0].title() for d in user_form.errors.keys()}})


class UserCreationAPI(APIView):
    """ User Store Section Using Api"""
    @staticmethod
    def get(request):
        user_form = UserModel.objects.all()
        serialize_form = UserSerializer(user_form, many=True)
        return Response(serialize_form.data)

    @staticmethod
    def post(request):
        user_form = UserSerializer(data=request.data)
        if user_form.is_valid():
            obj = user_form.save()
            emsg = EmailMessage()
            emsg.to = [request.data['email_id']]
            emsg.subject = "Registration"
            emsg.user = obj
            mail = EmailService.send(emsg, obj)
            if mail == 1:
                return Response({
                    'sucess': "Please check your mail for verification..."
                }, status=status.HTTP_200_OK)
        return Response(user_form.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerification(APIView):
    """ Email verification section """
    @staticmethod
    def get(request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            user.active = True
            user.save()

        except UserModel.DoesNotExist:
            return Response({"message": "User not found."}, status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return HttpResponse("<h1>Something went wrong...</h1>")

        return render(request, "email_validation.html", {"user": user})

#End of code...