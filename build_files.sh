# Install dependencies
pip install -r requirements.txt

# Buat folder staticfiles_build jika belum ada
mkdir -p staticfiles_build

# Jalankan collectstatic dan taruh hasilnya di staticfiles_build
# --noinput artinya jangan tanya "Yes/No", langsung timpa saja
python3.9 manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python3.9 manage.py makemigrations
python3.9 manage.py migrate