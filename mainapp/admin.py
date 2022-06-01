from django.contrib import admin
from .models import *


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title', 'decsription',)

    prepopulated_fields = {'slug': ('title',), }


@admin.register(Jer)
class JerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name', 'decsription',)


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'publish',)
    list_display_links = ('name', 'email',)
    list_filter = ('name', 'email', 'publish')
    search_fields = ('name', 'email', 'text')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'publish',)
    list_display_links = ('name', 'surname', 'email',)
    list_filter = ('name', 'surname', 'email', 'publish')
    search_fields = ('name', 'surname', 'email', 'text')


admin.site.register(CategoryNews)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at',)
    list_display_links = ('id', 'title', 'category',)
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('id', 'title', 'category', 'created_at')
    search_fields = ('title', 'category')


admin.site.register(HomeShots)


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('id', 'title',)
    search_fields = ('title', 'description')


@admin.register(Vakancia)
class VakanciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'qyzmet')
    list_display_links = ('id', 'region', 'qyzmet')
    list_filter = ('id', 'qyzmet',)
    search_fields = ('region', 'qyzmet')


@admin.register(OtinishVak)
class VakanciaOtinishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'nomer')
    list_display_links = ('id', 'name', 'surname', 'nomer')
    list_filter = ('id', 'name', 'surname', 'nomer')
    search_fields = ('id', 'name', 'surname', 'nomer', 'email')


@admin.register(RequestHelp)
class RequestHelpAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'nomer')
    list_display_links = ('id', 'name', 'surname', 'nomer')
    list_filter = ('id', 'name', 'surname', 'nomer')
    search_fields = ('id', 'name', 'surname', 'nomer', 'email')