from django.contrib import admin
from .models import *

# superuser admin oficio01

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'state', 'city')  
    list_display_links = ('name',)
    exclude = ('created_at', 'updated_at')
    search_fields = ('name', 'institution', 'state', 'city')

class ReceivedOLAdmin(admin.ModelAdmin):
    list_display = ('received_ol_number','received_in', 'authority', 'deadline') 
    list_display_links = ('received_ol_number', 'received_in')
    search_fields = ('received_ol_number','received_in', 'ol_date', 'ol_origin_id', 'authority', 'lawsuit_number', 'lawsuit_author', 'author_doc_number', 'lawsuit_accused', 'accused_doc_number', 'deadline', 'received_ol_number', 'answer_ol')      
    readonly_fields = ('received_ol_number', 'answer_ol')

class SentOLAdmin(admin.ModelAdmin):
    list_display = ('creation_date','sent_ol_number', 'authority') 
    list_display_links = ('creation_date','sent_ol_number')
    search_fields = (
    'creation_date', 
    'answer_to_ol', 
    'sent_ol_number', 
    'authority', 
    'lawsuit_number', 
    'lawsuit_author', 
    'author_doc_number', 
    'lawsuit_accused', 
    'accused_doc_number', 
    )      
    readonly_fields = ('sent_ol_number',)
    
admin.site.register(State)
admin.site.register(Authority, AuthorityAdmin)
admin.site.register(ReceivedOL, ReceivedOLAdmin)
admin.site.register(SentOL, SentOLAdmin)

