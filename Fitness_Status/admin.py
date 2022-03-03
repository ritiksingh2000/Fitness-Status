from django.contrib import admin
from .models import *

# HOME
class PostAdmin(admin.ModelAdmin):
    list_display = ("Video_Name", "Channel_Name", "Date")

class PostAdmin2(admin.ModelAdmin):
    list_display = ("Category",)

class PostAdmin3(admin.ModelAdmin):
    list_display = ("email","date")

class PostAdmin4(admin.ModelAdmin):
    list_display = ("Name","Subject","Date")

class PostAdmin5(admin.ModelAdmin):
    list_display = ("Channel_Name","Video_Name", "date")


admin.site.register(Healthtube, PostAdmin)
admin.site.register(VideoCategory, PostAdmin2)
admin.site.register(Subs, PostAdmin3)
admin.site.register(UserMessage, PostAdmin4)
admin.site.register(VideoSuggestion, PostAdmin5)

# ARTICLES
class PostAdmin6(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("category",)
    search_fields = ("title", "content")

class PostAdmin7(admin.ModelAdmin):
    list_display = ("category",)
admin.site.register(Categories, PostAdmin7)
admin.site.register(Article, PostAdmin6)
