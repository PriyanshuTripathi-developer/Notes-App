from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "pinned",
        "color",
        "archived",
        "trashed",
        "created_at",
        "updated_at",
        "reminder_at",
    )
    
    list_filter = (
        "pinned",
        "color",
        "archived",
        "trashed",
        "created_at",
    )

    search_fields = ("title", "content", "user__username")

    list_display_links = ("id", "title")

    list_editable = ("pinned", "color", "archived", "trashed")

    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Note Info", {
            "fields": ("user", "title", "content", "color")
        }),
        ("Status", {
            "fields": ("pinned", "archived", "trashed")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
        ("Reminder", {
            "fields": ("reminder_at",)
        }),
    )

