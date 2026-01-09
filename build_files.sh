# Install dependencies
pip install -r requirements.txt

# Pastikan folder staticfiles ada
mkdir -p staticfiles

# Kumpulkan file statis
# Perintah ini akan menyalin CSS admin ke folder 'staticfiles'
python3 manage.py collectstatic --noinput --clear

# Migrasi Database (Neon/PostgreSQL)
python3 manage.py makemigrations
python3 manage.py migrate

# Buat Admin Otomatis (Opsional)
python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"