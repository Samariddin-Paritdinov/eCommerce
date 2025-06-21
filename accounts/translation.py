from modeltranslation.translator import register, TranslationOptions

from accounts.models import User

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('bio',)


