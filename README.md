# thelemic-tools
Algumas ferramentas básicas para o trabalho Thelemico

### Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
```
git clone https://github.com/tiagocordeiro/thelemic-tools.git
cd thelemic-tools
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

Cria usuário
```
python manage.py createsuperuser --username dev --email dev@foo.bar
```

Rode o projeto
```
python manage.py runserver
```
