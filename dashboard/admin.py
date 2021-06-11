from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'body_text', 'body_html', 'genre')

admin.site.register(Book, BookAdmin)