from django.urls import path
from .api import UploadDocumentView, FilterMetabolitesView, RoundOffRetentionView, MeanRetentionView
from .views import home, tasks
urlpatterns = [
	path('', home, name='home'),
    path('tasks', tasks, name='tasks'),
    path('upload', UploadDocumentView.as_view(), name='upload'),
    path('filter_metabolites', FilterMetabolitesView.as_view(), name='task1'),
    path('roundoff_retention', RoundOffRetentionView.as_view(), name='task2'),
    path('mean_retention', MeanRetentionView.as_view(), name='task3'),
]