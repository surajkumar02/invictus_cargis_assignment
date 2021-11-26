from django.shortcuts import render
from rest_framework.views import APIView,Response

# Create your views here.

class ItemSort(APIView):
    def get(self,request):
        reverse=self.request.query_params.get('reverse')
        criteria=self.request.query_params.get('criteria')
        return Response(data={'data is here',reverse, criteria})

class Item(APIView):
    def get(self,request):
        id=self.request.query_params.get('id')
        location=self.request.query_params.get('location')
        if location:
            return Response(data={'Single item',id,location})

class ItemList(APIView):
    def get(self,request):
        userid=self.request.query_params.get('userid')
        status=self.request.query_params.get('status')
        if status:
            return Response(data={'Item List',userid,status})

class ItemRadius(APIView):
    def get(self,request):
        radius=self.request.query_params.get('radius')
        latitude=self.request.query_params.get('latitude')
        longitude=self.request.query_params.get('longitude')
        return Response(data={'Single item Radius',radius,latitude,longitude})

