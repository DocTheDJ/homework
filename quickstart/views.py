from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from quickstart.parsing import parseData
from quickstart.apps import QuickstartConfig
from django.core.serializers import serialize
from . import utils

utils.register()

# Create your views here.
@api_view(['POST'])
def importData(request):
    print(parseData(request.data))
    return Response()

@api_view(['GET'])
def getAllData(request):
    return Response(apps.all_models.get(QuickstartConfig.name).keys())

@api_view(['GET'])
def detail(request, name):
    if name == None:
        return Response("Missing name", status=206)
    if (model := apps.all_models.get(QuickstartConfig.name).get(name)) != None:
        queryset = model.objects.all()
        ser_instance = utils.get_serializer_instace(name, data=queryset, many=True)
        if not ser_instance.is_valid():
            return Response(ser_instance.data)
        else:
            return Response(ser_instance)
    return Response(apps.all_models.get(QuickstartConfig.name).keys())

@api_view(['GET'])
def detailOne(request, name, id):
    if name == None:
        return Response("Missing name", status=206)
    if id == None:
        return Response("Missing id", status=206)
    if (model := apps.all_models.get(QuickstartConfig.name).get(name)) != None:
        queryset = model.objects.filter(id=id)
        ser_instance = utils.get_serializer_instace(name, data=queryset, many=True)
        if not ser_instance.is_valid():
            return Response(ser_instance.data)
        else:
            return Response(ser_instance)
    return Response(apps.all_models.get(QuickstartConfig.name).keys())