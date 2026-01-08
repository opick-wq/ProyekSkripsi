from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    # --- Identitas Utama ---
    name = models.CharField(max_length=255, verbose_name="Nama Sekolah")
    
    # --- Aspek Lokator (Skripsi Soulthan) ---
    address = models.TextField(verbose_name="Alamat Lengkap")
    latitude = models.FloatField(help_text="Koordinat Lintang (Contoh: -6.502)")
    longitude = models.FloatField(help_text="Koordinat Bujur (Contoh: 106.704)")
    
    # --- Aspek Sistem Informasi (Skripsi Wulan) ---
    description = models.TextField(verbose_name="Profil Singkat Sekolah")
    vision = models.TextField(verbose_name="Visi", blank=True)
    mission = models.TextField(verbose_name="Misi", blank=True)
    
    # Kontak
    phone = models.CharField(max_length=20, blank=True, verbose_name="No. Telepon")
    email = models.EmailField(blank=True, verbose_name="Email")
    website = models.URLField(blank=True, verbose_name="Website Sekolah")
    # Aset Media
    photo = models.ImageField(upload_to='school_photos/', blank=True, null=True, verbose_name="Foto Gedung")
    headmaster_name = models.CharField(max_length=100, blank=True, verbose_name="Nama Kepala Sekolah")
    headmaster_photo = models.ImageField(upload_to='school_photos/', blank=True, null=True, verbose_name="Foto Kepala Sekolah")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Data Sekolah"
        verbose_name_plural = "Data Sekolah"


class News(models.Model):
    """
    Tabel untuk menyimpan Berita dan Kegiatan Sekolah.
    Fitur ini menjawab kebutuhan promosi dinamis.
    """
    title = models.CharField(max_length=200, verbose_name="Judul Berita")
    slug = models.SlugField(unique=True, help_text="Link unik (misal: kegiatan-maulid)")
    content = models.TextField(verbose_name="Isi Berita")
    image = models.ImageField(upload_to='news_photos/', verbose_name="Foto Kegiatan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Dibuat")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Penulis")

    class Meta:
        verbose_name = "Berita & Kegiatan"
        verbose_name_plural = "Berita & Kegiatan"
        ordering = ['-created_at'] # Urutkan dari yang terbaru

    def __str__(self):
        return self.title
    

class PPDBRegistration(models.Model):
    """
    Tabel untuk menyimpan data pendaftar PPDB (Booking Jadwal).
    """
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    
    # Hubungkan dengan akun User agar pendaftar bisa login
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Data Siswa
    full_name = models.CharField(max_length=150, verbose_name="Nama Lengkap Siswa")
    gender = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, verbose_name="Jenis Kelamin")
    birth_place = models.CharField(max_length=100, verbose_name="Tempat Lahir")
    birth_date = models.DateField(verbose_name="Tanggal Lahir")
    
    # Data Orang Tua
    parent_name = models.CharField(max_length=150, verbose_name="Nama Orang Tua/Wali")
    phone_number = models.CharField(max_length=20, verbose_name="No. WhatsApp")
    address = models.TextField(verbose_name="Alamat Rumah")
    
    # Booking Jadwal Datang
    booking_date = models.DateField(verbose_name="Rencana Datang ke Sekolah")
    
    # Status (Admin bisa ubah ini nanti)
    status = models.CharField(
        max_length=20, 
        default='Menunggu', 
        choices=[('Menunggu', 'Menunggu'), ('Diterima', 'Diterima'), ('Ditolak', 'Ditolak')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pendaftar PPDB"
        verbose_name_plural = "Data Pendaftar PPDB"

    def __str__(self):
        return f"{self.full_name} - {self.booking_date}"