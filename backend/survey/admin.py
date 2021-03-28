from django.contrib import admin

from survey.models import Survey, Question, SurveyContent


class QuestionInline(admin.TabularInline):
    model = SurveyContent


class SurveyPanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'description')
    list_filter = ['start_date', 'end_date']
    fields = ['name', ('start_date', 'end_date'), 'description']
    inlines = [QuestionInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        return self.readonly_fields


class QuestionPanelAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type')
    list_filter = ['question_type']


admin.site.register(Survey, SurveyPanelAdmin)
admin.site.register(Question, QuestionPanelAdmin)