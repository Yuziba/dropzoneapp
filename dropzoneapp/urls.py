from django.urls import path
from . import views
from dropzoneapp.views import MainView

app_name = 'dropzoneapp'

urlpatterns = [
    path('', MainView.as_view(), name="index"),
    path('upload/', views.file_upload_view, name='file_upload'),
    path('file_list/', views.file_list_view, name='file_list'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('download_file/<int:file_id>/', views.download_file, name='download_file'),
    #path('file_download/<int:file_id>/', views.FileDownloadView.as_view(), name='file_download'),

]


