from django.db import models

# Create your models here.
class Dropzonemodel(models.Model):
    upload = models.FileField(upload_to='media/')

    def __str__(self):
        return str(self.pk)
    


class UploadedFile(models.Model):
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name