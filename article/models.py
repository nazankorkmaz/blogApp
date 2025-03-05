from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar") #user silindiğinde onun yazdığı makaleleri de sil ve hazır olan user tablosuna article tablosunu bağla dedik

    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Kayıt Tarihi") # otomatik olarak atsın yani

    def __str__(self):  #listelendiği zaman articleler object3 falan diyeydi şimdi isimle sıralanıyor
        return self.title