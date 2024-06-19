from django.urls import path
from . import views
urlpatterns = [
    path('add_musician/',views.AddMusician.as_view(),name = 'add_musician'),
    path('EditMusician/<int:id>',views.EditMusician.as_view(),name = 'edit_musician'),
]