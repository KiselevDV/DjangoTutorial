from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    inlines = [ChoiceInline]
    fieldsets = [
        (None, {
            'fields': ('question_text',)
        }),
        ('Date information', {
            'fields': ('pub_date',)
        })
    ]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']
