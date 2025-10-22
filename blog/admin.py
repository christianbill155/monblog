from django.contrib import admin
from .models import Article, User, Category, Tag, Comment, Product

admin.site.register(Article)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Product)

# Register your models here.