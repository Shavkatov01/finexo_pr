from django.contrib import admin
from .models import Home, About, Service, WhyChoose, Customer, Team


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'photo', 'slide')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)



@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'text_title')
    list_display_links = ('title', 'text_title')
    list_filter = ('title', 'text_title')




@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)



@admin.register(WhyChoose)
class Why(admin.ModelAdmin):
    list_display = ('title', 'icons_title')
    list_display_links = ('title', 'icons_title')
    list_filter = ('title',)


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ('title', 'name', 'about')
    list_display_links = ('title', 'name')
    list_filter = ('name', )

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('title', 'person_name', 'person_business')
    list_display_links = ('title', 'person_name')
    list_filter = ('person_business',)

    



