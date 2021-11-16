from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from chat.models import Room
from onewayydrf.serializers import StudentSerializer
from onewayydrf.models import Student


class TestView(APIView):
    # def get(self, request, *args, **kwargs):
    #     sample_data = dict(username='sample', active_years_for=10)
    #     room_name = Room.objects.all()
    #     sample = room_name.values()
    #     # return Response(sample)
    #     return Response(dict(name_of_room=list(sample)))
    #     # return Response(sample_data)
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)