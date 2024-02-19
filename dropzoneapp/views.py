from django.shortcuts import render
from django.views.generic import TemplateView   
from django.http import HttpResponse, JsonResponse,  Http404
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.http import FileResponse
from django.core.files.storage import default_storage
from django.views import View


"""def index(request):
    return HttpResponse("deneme")"""

class MainView(TemplateView):
    template_name = 'dropzoneapp/index.html'

def file_upload_view(request):
    print(request.FILES)
    return HttpResponse('upload')

from .models import UploadedFile

def file_upload_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # Dosyayı işle ve veritabanına kaydet
            new_file = UploadedFile(file=uploaded_file)
            new_file.save()

            # Başarılı yanıt
            return JsonResponse({'message': 'Dosya başarıyla yüklendi.'}, status=200)
        else:
            # Dosya yüklenmediğinde hata yanıtı
            return JsonResponse({'error': 'Dosya yüklenirken bir hata oluştu.'}, status=400)
    else:
        # POST isteği dışında gelen isteklere hata yanıtı
        return JsonResponse({'error': 'Geçersiz istek yöntemi.'}, status=405)


def file_list_view(request):
    files = UploadedFile.objects.all()  # models.py'deki modele göre
    return render(request, 'dropzoneapp/file_list.html', {'files': files})

def delete_file(request, file_id):
    file_to_delete = get_object_or_404(models.UploadedFile, id=file_id)
    file_to_delete.delete()
    return redirect('dropzoneapp:file_list')


    
def download_file(request, file_id):
    file_instance = get_object_or_404(UploadedFile, id=file_id)
    file_field_name = 'file'    # Dosya alanının adını temsil eden değişken
    print("idddddddddddddd",file_id)
    file_path = file_instance.file.path     # Dosya yolu oluştur
    print("Dosya yolu oluştur",file_path)

    response = FileResponse(file_path)
    print("fileeeee",file_path)
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
    return response


"""class FileDownloadView(View):
    def get(self, request, file_id):
        file_instance = get_object_or_404(UploadedFile, pk=file_id)
        print("isimmmm ",file_instance)
        try:
            # Dosyayı aç ve kullanıcıya gönder
            file_path = default_storage.path(file_instance.file.name)
            with open(file_path, 'rb') as file:
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
                print("BBBBBBBBBBB,",file_instance.file.name)
                return response
        except FileNotFoundError:
            raise Http404("Belirtilen dosya bulunamadı.")"""


