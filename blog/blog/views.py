from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        sample_data = dict(username='sample', active_years_for=10)
        return Response(sample_data)
