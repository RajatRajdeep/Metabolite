from django.urls import path
from .api import UploadDocumentView
from .views import home
urlpatterns = [
	path('', home, name='home'),
    path('upload', UploadDocumentView.as_view(), name='upload'),
]