import json
import os
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Define the path to the JSON data file
DATA_FILE = os.path.join(settings.BASE_DIR, 'actions', 'data.json')

# Ensure the directory exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

# Helper function to read JSON data
def read_json():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Helper function to write JSON data
def write_json(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# API to handle listing and creating actions
class ActionListCreateView(APIView):
    def get(self, request):
        actions = read_json()
        return Response(actions, status=status.HTTP_200_OK)

    def post(self, request):
        actions = read_json()
        new_id = max([a["id"] for a in actions], default=0) + 1  # Ensure unique ID
        new_action = {
            "id": new_id,
            "action": request.data.get("action"),
            "date": request.data.get("date"),
            "points": request.data.get("points")
        }
        actions.append(new_action)
        write_json(actions)
        return Response(new_action, status=status.HTTP_201_CREATED)

# API to handle retrieving, updating, and deleting actions
class ActionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        actions = read_json()
        action = next((a for a in actions if a["id"] == pk), None)
        if action:
            return Response(action, status=status.HTTP_200_OK)
        return Response({"error": "Action not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        actions = read_json()
        for action in actions:
            if action["id"] == pk:
                action["action"] = request.data.get("action", action["action"])
                action["date"] = request.data.get("date", action["date"])
                action["points"] = request.data.get("points", action["points"])
                write_json(actions)
                return Response(action, status=status.HTTP_200_OK)
        return Response({"error": "Action not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        actions = read_json()
        filtered_actions = [a for a in actions if a["id"] != pk]
        if len(filtered_actions) == len(actions):  # No deletion happened
            return Response({"error": "Action not found"}, status=status.HTTP_404_NOT_FOUND)
        write_json(filtered_actions)
        return Response({"message": "Action deleted"}, status=status.HTTP_204_NO_CONTENT)
