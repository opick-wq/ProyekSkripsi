# Install dependencies
pip install -r requirements.txt

# Buat folder staticfiles_build jika belum ada
mkdir -p staticfiles_build

# Jalankan collectstatic dan taruh hasilnya di staticfiles_build
# --noinput artinya jangan tanya "Yes/No", langsung timpa saja
# Gunakan python3 agar sesuai dengan pip yang digunakan
python3 manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python3 manage.py makemigrations
python3 manage.py migrate