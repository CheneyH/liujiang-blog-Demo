from django.contrib import admin
from .models import Question
from .models import Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('问卷问题', {'fields': ['question_text']}),
        ('时间与日期', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [(ChoiceInline)]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.sites.AdminSite.site_header = '投票站点管理界面'
admin.sites.AdminSite.site_title = '投票站点后台管理系统'
