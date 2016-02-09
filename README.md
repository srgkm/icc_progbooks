# Start

```sh
git clone https://github.com/srgkm/icc_progbooks
cd icc_progbooks
virtualenv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py pop_books
```
