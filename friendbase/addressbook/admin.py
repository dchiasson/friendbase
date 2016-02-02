from friendbase.addressbook.models import Family, Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'is_birthday_soon')
    search_fields = ['first_name', 'last_name']
    list_filter = ['birthday']

admin.site.register(Person, PersonAdmin)
admin.site.register(Family)
