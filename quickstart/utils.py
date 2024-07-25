from . import models
from . import serializers
from django.apps import apps
from quickstart.apps import QuickstartConfig
from rest_framework import serializers as rsSerializers

serializer_registry = {}

def register_serializer(model_class, serializer_class):
    serializer_registry[model_class.__name__] = serializer_class

def register():
    register_serializer(models.AttributeName, serializers.AttributeNameSerializer)
    register_serializer(models.AttributeValue, serializers.AttributeValueSerializer)
    register_serializer(models.Attribute, serializers.AttributeSerializer)
    register_serializer(models.Image, serializers.ImageSerializer)
    register_serializer(models.ProductAttributes, serializers.ProductAttributesSerializer)
    register_serializer(models.ProductImage, serializers.ProductImageSerializer)
    register_serializer(models.Product, serializers.ProductSerializer)
    register_serializer(models.Catalog, serializers.CatalogSerializer)

def get_serializer_instace(model_name, *args, **kwargs) -> rsSerializers.ModelSerializer:
    model_class = apps.get_model(app_label=QuickstartConfig.name, model_name=model_name)
    serializer_class = serializer_registry.get(model_class.__name__)
    if serializer_class:
        return serializer_class(*args, **kwargs)
    else:
        return ValueError(f"Serializer not found for model {model_name}")