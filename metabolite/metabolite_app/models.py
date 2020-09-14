from django.db import models

# Document model is created to save excel file
class Document(models.Model):
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document