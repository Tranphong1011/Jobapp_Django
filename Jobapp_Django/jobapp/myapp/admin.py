from django.contrib import admin

from myapp.models import Author, JobPost, Location, Skills

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'date')
    list_filter = ('date', 'salary',)
    search_fields = ('title',)
    search_help_text = "Type the search keywords"
    # fields = (('title', 'description'), 'expiry')
    fieldsets = (
        ('Basic information', {'fields': ('title', 'description')}),

        ('More information', {'classes': ('collapse', 'wide'), 'fields': (('salary', 'expiry'), 'slug')}))


# admin.site.register(JobPost, JobAdmin)
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
