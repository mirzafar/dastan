from django.contrib import admin
from main.models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class GradeAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    pass

class InfoAdmin(admin.ModelAdmin):
    pass

class SendMessageAdmin(admin.ModelAdmin):
    pass

class Category2Admin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Category2, Category2Admin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(SendMessage, SendMessageAdmin)