from django.contrib import admin
from .models import Slider, MainCategory, Category, SubCategory
# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    pass


class MainCategoryAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class SubCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Slider, SliderAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

