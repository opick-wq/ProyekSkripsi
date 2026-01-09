# Install dependencies
pip install -r requirements.txt

# Buat folder output untuk static files
mkdir -p staticfiles_build

# Kumpulkan file static (CSS Admin) ke folder staticfiles_build
# Perintah ini yang "mengambil" CSS dari Django Admin
python3 manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python3 manage.py makemigrations
python3 manage.py migrate

# Buat Admin Otomatis (Hanya jika belum ada)
python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"