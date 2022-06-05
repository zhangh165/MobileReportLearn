# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from products.models import  Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
import json

@api_view(['POST'])
def api_home(request,*args,**kwargs):
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    # JsonResponse request type is application/json
    # HttpReponse response type is text/html for default
    # HttpResponse(data,headers=['content-type','application/json']) to convert to json
    data = request.data
    serializer = ProductSerializer(data=request.data)
    # serializer 也可以验证数据
    # 更像是一个repo层的加强版
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response(data)

# Create your views here.
