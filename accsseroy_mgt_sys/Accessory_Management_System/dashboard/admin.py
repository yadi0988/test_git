from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from . models import Category,Product,Order
 
admin.site.site_header="My Inventory Dashboard"
 
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['category']
    list_editable=['quantity']
     
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    mptt_level_indent = 15
     
 
     
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Category,CategoryAdmin)