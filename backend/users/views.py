import os
import json

from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from django.conf import settings
from .models import User, Conversation, ForgotPassword
from .serializers import UserRegistrationSerializer

def get_creds(request):
    """
    Helper function to extract credentials from request data.
    """
    data = request.data
    email = data.get('email')
    password = data.get('password')
    return email, password

@api_view(['GET'])
@permission_classes([AllowAny])
def refresh(request):
    """
    Handle token refreshing using refresh token stored in secure HTTP-only cookie.
    """
    refresh_token = request.COOKIES.get('refresh_token')
    if not refresh_token:
        return Response({'error': 'Refresh token is missing in cookie'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        refresh = RefreshToken(refresh_token)
        new_access_token = refresh.access_token

        return Response({
            'access_token': str(new_access_token),
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': 'Invalid refresh token', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Endpoint to fetch all users (admin use case, for example)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])  # Only authenticated users can access
def all_users(request):
    users = User.objects.all()
    user_data = [{'userid': user.userid, 'email': user.email} for user in users]
    return JsonResponse({'users': user_data})


# Endpoint to create a user
@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone can create an account
def create_user(request):
    """
    Create a new user using validated data from the serializer.
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint for user login and JWT token issuance
@api_view(['POST'])
@permission_classes([AllowAny])  # Anyone can attempt to log in
def login(request):
    """
    Authenticate user using email and password, and issue JWT tokens.
    """
    email, password = get_creds(request)

    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            user.last_login = timezone.now()
            user.refreshtoken = refresh_token
            user.save()
            # Create response
            response = JsonResponse({
                'message': 'Login successful',
                'access_token': access_token,  # Still sending access token in body
            }, status=status.HTTP_200_OK)

            # Set refresh token as HttpOnly cookie
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,  # HTTP-only flag
                secure=settings.SECURE_COOKIE,  # Use True if using HTTPS
                samesite='Strict',  # Adjust depending on your needs ('Lax' or 'None')
                max_age=7 * 24 * 60 * 60,  # 1 week
            )

            return response
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
# Endpoint to log out user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    """
    Logout user by deleting JWT tokens and refresh token cookie.
    """
    response = JsonResponse({'message': 'Logged out successfully'})
    response.delete_cookie('refresh_token')  # Delete refresh token cookie
    user = request.user
    user = User.objects.get(email=user.email)
    user.refreshtoken = None
    user.save()
    return response

# Endpoint to fetch user conversations
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_conversations(request):
    """
    Fetch all conversations for the authenticated user.
    """
    user = request.user
    data = request.data

    conversation_id = data.get('conversation_id')

    conversations = Conversation.objects.filter(userid_id=user.id)

    if conversations.count() == 0:
        return Response({'message': 'No conversations found'}, status=status.HTTP_404_NOT_FOUND)
    
    if conversation_id:
        conversation = conversations.get(conversationid=conversation_id)
        file_path = conversation.filePath

    file_path = os.path.join(settings.BASE_DIR, 'conversations', f"{user.id}_{conversation.conversationid}.jsonl")	

    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    
    return Response({'data': data}, status=status.HTTP_200_OK)

# Endpoint to get all conversation

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_conversations(request):
    """
    Fetch all conversations for the authenticated user.
    """
    user = request.user
    conversations = Conversation.objects.filter(userid_id=user.id)
    
    if conversations.count() == 0:
        return Response({'message': 'No conversations found'}, status=status.HTTP_404_NOT_FOUND)
    
    data = [{'conversation_id': conversation.conversationid, 'title': conversation.conversationName} for conversation in conversations]

    return Response({'data': data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rename_conversation(request):
    """
    Rename a conversation for the authenticated user.
    """
    user = request.user
    data = request.data

    conversation_id = data.get('conversation_id')
    new_name = data.get('new_name')

    if not conversation_id or not new_name:
        return Response({'message': 'Conversation ID and new name are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        conversation = Conversation.objects.get(userid_id=user.id, conversationid=conversation_id)
        conversation.conversationName = new_name
        conversation.save()
        return Response({'message': 'Conversation renamed successfully'}, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response({'message': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)

# TODO: 1. Implement endpoint to verify forgot password token
#. 2. Implement the email config to send the token to the user
@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if not email:
        return Response({'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
        forgot = ForgotPassword.objects.create(user=user)
        forgot.save()

        # Send the email with the token
        send_mail(
            subject='Your CourseRec Password Reset Code',
            message=f'Hello there,\n\nYour password reset code is: {forgot.token}\n\nIf you did not request this, please ignore this email.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'Error sending reset email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'message': 'Password reset code sent to your email'}, status=status.HTTP_200_OK)
    
