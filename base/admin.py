from django.contrib import admin
from .models import Todo_list, Water, Tiffin, Maid

# Register your models here.
admin.site.register(Water)
admin.site.register(Tiffin)
admin.site.register(Maid)
admin.site.register(Todo_list)
