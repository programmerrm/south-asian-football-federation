from django.contrib import admin

from configuration.models import (
    Logo, 
    Favicon, 
)
from configuration.utils.button.admin import (
    image_preview, 
    view_button, 
    edit_button, 
    delete_button,
)

# LOGO
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    # ===== LIST VIEW FIELDS =====
    list_display = (
        "id",
        "image_column",
        "alt",
        "width",
        "height",
        "view_button_column",
        "edit_button_column",
        "delete_button_column",
    )

    # ===== FIELD ORDERING INSIDE FROM =====
    fields = (
        "image",
        "alt",
        "width",
        "height",
    )

    # ===== Disable Add If Exists =====
    def has_add_permission(self, request):
        return not Logo.objects.exists()
    
    # ===== Image Preview Link =====
    def image_column(self, obj):
        return image_preview(obj, "image")
    
    # ===== View Button =====
    def view_button_column(self, obj):
        return view_button(obj)

    view_button_column.short_description = "View"

    # ===== Edit Button =====
    def edit_button_column(self, obj):
        return edit_button(obj)

    edit_button_column.short_description = "Edit"

    # ===== Delete Button =====
    def delete_button_column(self, obj):
        return delete_button(obj)

    delete_button_column.short_description = "Delete"

# FAVICON
@admin.register(Favicon)
class FaviconAdmin(admin.ModelAdmin):
    # ===== LIST VIEW FIELDS =====
    list_display = (
        "id",
        "view_button_column",
        "edit_button_column",
        "delete_button_column",
    )

    # ===== FIELD ORDERING INSIDE FROM =====
    fieldsets = (
        ("Browser", {
            "fields": ("favicon_ico", "favicon_16", "favicon_32"),
        }),
        ("Apple", {
            "fields": ("apple_touch_icon",),
        }),
        ("Android", {
            "fields": ("android_192", "android_512"),
        }),
        ("Microsoft", {
            "fields": ("ms_tile_icon",),
        }),
    )

    # ===== Disable Add If Exists =====
    def has_add_permission(self, request):
        return not Favicon.objects.exists()
    
    # ===== View Button =====
    def view_button_column(self, obj):
        return view_button(obj)
    
    view_button_column.short_description = "View"

    # ===== Edit Button =====
    def edit_button_column(self, obj):
        return edit_button(obj)

    edit_button_column.short_description = "Edit"

    # ===== Delete Button =====
    def delete_button_column(self, obj):
        return delete_button(obj)

    delete_button_column.short_description = "Delete"
