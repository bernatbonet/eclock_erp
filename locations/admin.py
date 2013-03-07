# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name', ]
    search_fields = ['name', ]


class EntryAdmin(admin.ModelAdmin):
    list_display = ('category_desc', 'name', )
    ordering = ['name', ]
    search_fields = ['name', ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
