from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import School, News, PPDBRegistration
from .forms import PPDBForm

# --- VIEW UTAMA ---
def home_view(request):
    """Halaman utama yang menampilkan profil sekolah & peta."""
    try:
        mitra_utama = School.objects.first() # Ambil sekolah pertama
    except School.DoesNotExist:
        mitra_utama = None

    context = {
        'sekolah': mitra_utama
    }
    return render(request, 'locator/home.html', context)

def school_data_api(request):
    """API untuk mengirim data sekolah ke Peta Leaflet."""
    schools = School.objects.all()
    
    features = []
    for school in schools:
        photo_url = None
        if school.photo:
            photo_url = request.build_absolute_uri(school.photo.url)
            
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [school.longitude, school.latitude]
            },
            "properties": {
                "name": school.name,
                "address": school.address,
                "description": school.description,
                "photo_url": photo_url,
                "phone": school.phone,
                # Hapus baris website jika belum migrasi, atau pakai getattr untuk aman
                "website": getattr(school, 'website', ''), 
            }
        })
    
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return JsonResponse(geojson_data)

# --- VIEW BERITA (YANG TADI ERROR) ---
def news_list(request):
    """Menampilkan daftar semua berita."""
    news = News.objects.all()
    return render(request, 'locator/news_list.html', {'news': news})

def news_detail(request, slug):
    """Menampilkan detail satu berita."""
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'locator/news_detail.html', {'news': news_item})

# --- VIEW AUTH (REGISTER) ---
def register_view(request):
    """Halaman pendaftaran akun user baru."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat! Silakan login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'locator/register.html', {'form': form})

# --- VIEW PPDB ONLINE ---
@login_required
def ppdb_dashboard(request):
    """Dashboard status pendaftaran user."""
    try:
        pendaftar = request.user.ppdbregistration
        # Jika sudah punya data pendaftaran, tampilkan status
        # Kita butuh template ppdb_status.html (nanti kita buat simpel aja)
        return render(request, 'locator/ppdb_status.html', {'pendaftar': pendaftar}) 
    except PPDBRegistration.DoesNotExist:
        # Jika belum daftar, arahkan ke form
        return redirect('ppdb_apply')

@login_required
def ppdb_apply(request):
    """Formulir pendaftaran PPDB."""
    # Cek jika sudah daftar, jangan kasih daftar lagi
    if hasattr(request.user, 'ppdbregistration'):
        return redirect('ppdb_dashboard')

    if request.method == 'POST':
        form = PPDBForm(request.POST)
        if form.is_valid():
            ppdb = form.save(commit=False)
            ppdb.user = request.user
            ppdb.save()
            return redirect('ppdb_success')
    else:
        form = PPDBForm()
    return render(request, 'locator/ppdb_form.html', {'form': form})

@login_required
def ppdb_success(request):
    """Halaman sukses setelah daftar."""
    return render(request, 'locator/ppdb_success.html')