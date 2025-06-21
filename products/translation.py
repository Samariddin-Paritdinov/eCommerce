from modeltranslation.translator import register, TranslationOptions
from products.models import (
    Product,
    ProductVariant,
    Category,
    Brand,
    Size,
    Color,
    Review,
    Comment,
)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(ProductVariant)
class ProductVariantTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Size)
class SizeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('review',)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)
