from django.contrib import admin
from django.template.loader import render_to_string

from .models import ProductCategory, Product

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified', 'created')
    list_filter = ('modified', 'created')
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'picture', 'category', 'price', 'quantity',
        'modified', 'created'
        )

    def picture(self, obj):
        return render_to_string(
            'components/picture.html',
            {
                'image':obj.image
            }
        )

    list_filter = ('category', 'modified', 'created')
    # search_fields = ('name','description')
    # pass

# admin.site.register(ProductCategory, CategoryAdmin)
# admin.site.register(Product)
