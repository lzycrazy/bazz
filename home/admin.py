from django.contrib import admin
from .models import Post,Table,Contact,Singup,Record,blog
# Register your models here.


admin.site.register(Post)
admin.site.register(Table)
admin.site.register(Contact)
admin.site.register(Singup)
admin.site.register(Record)




@admin.register(blog)
class Postadmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
    