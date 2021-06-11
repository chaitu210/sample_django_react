## Steps to run the project

Setup virtualenv (optional)
```bash
virtualenv env
source env/bin/activate
```

Install dependencies for django & react

```bash
pip install -r requirements.txt
npm install
```

Run django server

```bash
python manage.py runserver
```

Run webpack compiler

```bash
npm run watch
```

Load Initial Data using fixures

```bash
python manage.py loaddata dashboard/fixtures/books.json
```

