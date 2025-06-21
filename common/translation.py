from modeltranslation.translator import register, TranslationOptions

from common.models import BlogPost


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content', 'category')
