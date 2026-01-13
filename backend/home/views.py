from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# from SOT import fetch_movies_list

class MovieList(APIView):
    def get(self, request):
        dummy = [
            {
                "id": "001",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
            {
                "id": "002",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
            {
                "id": "003",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
            {
                "id": "004",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
            {
                "id": "005",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
            {
                "id": "006",
                "title": "Night Of the Living Dead",
                "duration": "1h 32 mins",
                "size": "1.2GB",
                "thumbnail": "https://archive.org/images/notfound.png",
            },
        ]
        return Response({"results": dummy})
