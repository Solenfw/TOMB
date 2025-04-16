

from django.contrib import admin
from .models import Movie, UserAnswer


class UserAnswerInLine(admin.TabularInline):
    model = UserAnswer
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [UserAnswerInLine]


admin.site.register(Movie, MovieAdmin)