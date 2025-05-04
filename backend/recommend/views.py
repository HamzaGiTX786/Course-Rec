import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .usemodel import testmodel
from rest_framework.permissions import IsAuthenticated

from users.models import User, Conversation


@api_view(['GET'])
def test(request):
    return HttpResponse("Hello, world! This is the test view.")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommend_courses(request):
    user = request.user
    data = request.data
    prompt = data.get('prompt')
    conversation_id = data.get('conversation_id', None)
    created = False
    new_conversation = False

    if not prompt:
        return Response({"message": "Error! No prompt provided"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new conversation if no conversation is found for the user. 
    # Otherwise, get the conversation by ID.
    try:
        conversations = Conversation.objects.filter(userid_id=user.id)
        if conversations.count() == 0:  # No conversations found
            conversation = Conversation.objects.create(userid_id=user.id) # Create a new conversation
            created = True
            new_conversation = True
        else: # Conversations found
            if not conversation_id:  # Create a new conversation
                conversation = Conversation.objects.create(userid_id=user.id) # Create a new conversation
                created = True
                new_conversation = True
            else:
                conversation = conversations.get(conversationid=conversation_id) # Get the conversation by ID
    except ObjectDoesNotExist:
        return Response({"message": "Error retrieving conversation"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    response = testmodel(prompt).content # Get the answer of the prompt

    # Define file-writing logic
    def write_to_file(filepath, prompt, response):
        full_path = os.path.join(settings.BASE_DIR, "conversations", f"{filepath}.jsonl")
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            # Open the file in append mode (create if it doesn't exist)
            with open(full_path, 'a') as f:
                format_data = {"prompt": prompt, "completion": response}
                f.write(json.dumps(format_data) + "\n")
        except Exception as e:
            return str(e)
        return None

    # Handle file operations
    if not created: # old conversation
        filepath = conversation.filePath
    else: # new conversation
        filepath = str(user.id)+"_"+str(conversation.conversationid) # create the file with the user.id and conversation.conversationid
        conversation.filePath = filepath
        conversation.save()

    error = write_to_file(filepath, prompt, response)
    if error:
        return Response({"message": f"Error writing to file: {error}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({
                    "message": "Success", 
                    "data": response, 
                    "conversation_id": conversation.conversationid, 
                    "new_conversation": new_conversation
                    }, status=status.HTTP_200_OK)



