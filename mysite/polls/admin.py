# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 修改的时候字段的展示
    # fields = ['pub_date', 'question_text', ]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)