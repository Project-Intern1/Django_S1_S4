import datetime

from django.contrib import admin



from .models import Choice, Question
# admin.site.register(Choice)
# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["question_text"]}),
        ("Date inf",{"fields":["time_pub"], "classes":["collapse"]}),

    ]
    inlines = [ChoiceInline]
    list_display = ["question_text","time_pub","was_published_recently"]

admin.site.register(Question, QuestionAdmin)

