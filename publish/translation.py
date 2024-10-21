from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'description1', 'description2', 'description3', 'sub_description1', 'sub_description2')

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Skills)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'description', 'sub_description', 'message', 'sub_message', 'comment')


@register(SubjectContact)
class SubjectContactTranslationOptions(TranslationOptions):
    fields = ('subject',)

@register(Autism)
class AutismTranslationOptions(TranslationOptions):
    fields = ('title', 'finance', 'description', 'startedDate')


@register(RareDiseases)
class RareDiseasesTranslationOptions(TranslationOptions):
    fields = ('title', 'finance', 'description', 'startedDate')


@register(Books)
class BooksTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Membership)
class MembershipTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(HonoursAwards)
class HonoursAwardsTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(TrainingConsulting)
class TrainingConsultingTranslationOptions(TranslationOptions):
    fields = ('description',)
