from .models import Product
from .serializers import ProdcuctsSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.


@api_view(['GET'])
def search_products(request,name):
    if request.method == 'GET':  
        result = Product.objects.filter(Q(name__icontains = name)).order_by('price')
        property_serializer = ProdcuctsSerializer(result, many=True)
        return JsonResponse(property_serializer.data, safe=False)