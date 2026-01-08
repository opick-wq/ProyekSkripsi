# Install dependencies
pip install -r requirements.txt

# Buat folder staticfiles_build jika belum ada
mkdir -p staticfiles_build

# Jalankan collectstatic
python3 manage.py collectstatic --noinput --clear

# Jalankan migrasi database (Membuat tabel)
python3 manage.py makemigrations
python3 manage.py migrate

# --- BAGIAN BARU: BUAT ADMIN OTOMATIS ---
# Perintah ini akan mengecek: Jika user 'admin' belum ada, maka buatkan.
# Username: admin
# Email: admin@example.com
# Password: admin123  (Bisa Anda ganti di sini)

python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"