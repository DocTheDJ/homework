from django.urls import path
from .views import importData, getAllData, detail, detailOne

# no need to describe
urlpatterns = [
    path("import/", importData),
    path("models/", getAllData),
    path("detail/<str:name>/", detail),
    path("detail/<str:name>/<int:id>", detailOne)
]