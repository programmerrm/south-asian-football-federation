from django.utils.html import format_html, strip_tags

# ====== TEXT PREVIEW ======
def short_text(obj, field_name, length=10):
    text = getattr(obj, field_name, "")
    if text:
        clean_text = strip_tags(text)
        return clean_text[:length] + "..."
    return "-"

# ====== IMAGE PREVIEW ======
def image_preview(obj, field_name, width=100):
    file_field = getattr(obj, field_name, None)
    if file_field and hasattr(file_field, "url"):
        return format_html(
            '<img src="{}" width="{}" style="object-fit:cover;"/>',
            file_field.url,
            width,
        )
    return "-"

# ====== VIDEO PREVIEW ======
def video_preview(obj, field_name):
    url = getattr(obj, field_name, None)
    if url:
        return format_html(
            '<a class="button" href="{}" target="_blank">View Video</a>', url
        )
    return "-"

# ======== VIEW BUTTON =============
def view_button(obj, url_prefix=None, text="View"):
    if obj.pk:
        prefix = url_prefix or obj._meta.app_label + "/" + obj._meta.model_name
        return format_html(
            '<a class="button" href="/admin/{}/{}/change/">{}</a>', prefix, obj.id, text
        )
    return "-"

# ======== EDIT BUTTON =============
def edit_button(obj, url_prefix=None, text="Edit"):
    if obj.pk:
        prefix = url_prefix or obj._meta.app_label + "/" + obj._meta.model_name
        return format_html(
            '<a class="button" href="/admin/{}/{}/change/">{}</a>', prefix, obj.id, text
        )
    return "-"

# ======== DELETE BUTTON =============
def delete_button(obj, url_prefix=None, text="Delete"):
    if obj.pk:
        prefix = url_prefix or obj._meta.app_label + "/" + obj._meta.model_name
        return format_html(
            '<a class="button button-delete" href="/admin/{}/{}/delete/">{}</a>',
            prefix,
            obj.id,
            text,
        )
    return "-"
