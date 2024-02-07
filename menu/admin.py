from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import MenuBy
# Register your models here.


admin.site.register(
    MenuBy,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

