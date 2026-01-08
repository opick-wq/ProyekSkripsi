from django.contrib import admin
from .models import School, News, PPDBRegistration

# Admin untuk Sekolah (sudah ada)
admin.site.register(School)

# Admin untuk Berita
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)} # Otomatis isi slug dari judul

# Admin untuk PPDB (Bisa lihat daftar pendaftar)
@admin.register(PPDBRegistration)
class PPDBAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'parent_name', 'phone_number', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('full_name', 'parent_name')