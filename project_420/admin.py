from django.contrib import admin
from.models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("date", "strain_name", "grow_info", "strain_base", "strain_id", "flower_effect3", "user_rating", "flower_flavor", "flower_effect", "user_notes")
    search_fields = ("date", "strain_name", "grow_info", "strain_base", "strain_id", "user_rating", "user_notes", "first_name", "last_name", "email")
    list_filter = ("strain_name", "strain_id", "strain_base", "user_rating", "flower_effect")
    ordering = ("strain_name", "strain_base", "strain_id", "user_rating")
    readonly_fields = ()


admin.site.register(Form, FormAdmin)
