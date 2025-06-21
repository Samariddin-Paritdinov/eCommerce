from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from products.models import *


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "is_active")
    list_display_links = ("id", "name", "brand")
    list_filter = ("is_active", "brand", "category")
    search_fields = ("name", "brand", "category")
    list_editable = ("is_active",)

    fieldsets = (
        (_("Main"), {
            'fields': ("brand", "category", "is_active")
        }),
        (_("Uzbek"), {
            'fields': ('name_uz', 'description_uz',)
        }),
        (_("English"), {
            'fields': ('name_en', 'description_en')
        }),
        (_("Russian"), {
            'fields': ('name_ru', 'description_ru')
        }))

    inlines = [ProductVariantInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo")
    list_display_links = ("id", "name")
    search_fields = ("name",)

    fieldsets = (
        (_("Main"), {
            'fields': ('logo',)
        }),
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)

    fieldsets = (
        (_("Main"), {
            'fields': ()
        }),
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }))


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)

    fieldsets = (
        (_("Main"), {
            'fields': ()
        }),
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }))


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)

    fieldsets = (
        (_("Main"), {
            'fields': ()
        }),
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }))


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "size", "color", "price")
    list_display_links = ("id", "name", "product")
    search_fields = ("product", "size", "color")

    fieldsets = (
        (_("Main"), {
            'fields': ('product', 'size', 'color', 'price')
        }),
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }))


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "user__email", "product__name", "review")
    list_display_links = ("id", "rating", "user__email")
    search_fields = ("user__email",)

    fieldsets = (
        (_("Main"), {
            'fields': ("rating", "user__email", "product__name",)
        }),
        (_("Uzbek"), {
            'fields': ('review_uz',)
        }),
        (_("English"), {
            'fields': ('review_en',)
        }),
        (_("Russian"), {
            'fields': ('review_ru',)
        }))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user__email", "product__name", "text")
    list_display_links = ("id", "user__email")
    search_fields = ("user__email",)

    fieldsets = (
        (_("Main"), {
            'fields': ("user__email", "product__name", "text", "parent")
        }),
        (_("Uzbek"), {
            'fields': ('text_uz',)
        }),
        (_("English"), {
            'fields': ('text_en',)
        }),
        (_("Russian"), {
            'fields': ('text_ru',)
        }))


