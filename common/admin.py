from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from common.models import MediaFile, BlogPost


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "slug", "category", "published_date", "comment_count", "short_description", )
    prepopulated_fields = {"slug": ("title_en",)}
    search_fields = ("title", "category")
    list_filter = ("category", "published_date")
    readonly_fields = ("published_date",)

    fieldsets = (
        (_("Main"), {
            "fields": ("slug", "comment_count")
        }),
        (_("Uzbek"), {
            "fields": ("title_uz", "short_description_uz", "content_uz", "category_uz")
        }),
        (_("English"), {
            "fields": ("title_en", "short_description_en", "content_en", "category_en")
        }),
        (_("Russian"), {
            "fields": ("title_ru", "short_description_ru", "content_ru", "category_ru")
        }),
    )