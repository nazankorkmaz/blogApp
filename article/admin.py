from django.contrib import admin

# Register your models here.
from .models import Article

#admin.site.register(Article) #admin paneline article kaydeder ve gösterir

# yukardaki geneldi şimdi zamanı falan da sıralanmada gözüksün diye decarator kullanıp içinde classla özelleştiricez

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display=["title","author","created_date"]
    list_display_links =["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta: #article ile articleadmini bağlar
        model = Article