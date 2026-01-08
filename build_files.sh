# build_files.sh
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear
#hs
git update-index --chmod=+x build_files.sh
git commit -m "Make build script executable"
git push