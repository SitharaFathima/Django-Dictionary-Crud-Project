from django.contrib import admin

from dictionary.models import Word, WordMeaning


class AdminWord(admin.ModelAdmin):
    list_display = ["word"]

admin.site.register(Word)


class AdminWordMeaning(admin.ModelAdmin):
    list_display = [ "word", "meaning", "priority"]

admin.site.register(WordMeaning, AdminWordMeaning)