# Pp7.2 – Modificacions lloc Web amb Framework Django

## Alumne
Jan García

---

## Descripció del projecte

En aquesta activitat s’ha desenvolupat un lloc web utilitzant el framework Django.

El projecte està basat en l’exercici Pp5.3 (Array multidimensional), on es treballava amb una estructura de dades de motos, fabricants i pilots. En aquesta pràctica, en lloc d’utilitzar un array en PHP, s’ha implementat una aplicació web amb base de dades relacional, models, relacions entre taules i un sistema CRUD complet.

---

# 1. Instal·lació de l’estructura del projecte (2.0 punts)

## 1.1 Creació de l’entorn virtual

S’ha creat un entorn virtual amb:

```bash
python -m venv venv
```
I posteriorment s’ha activat.

1.2 Instal·lació de Django
Amb l’entorn activat, s’ha instal·lat Django:
```bash
pip install django
```
Després s’ha generat el fitxer requirements.txt:
```bash
pip freeze > requirements.txt
```
Aquest fitxer permet replicar l’entorn en qualsevol altre equip mitjançant:
```bash
pip install -r requirements.txt
```
1.3 Creació del projecte i l’app
S’ha creat el projecte principal:
```bash
django-admin startproject motos_project
```
I després l’app:
```bash
python manage.py startapp motos
```
Posteriorment, s’ha afegit l’app motos al fitxer settings.py dins de INSTALLED_APPS.

# 2. Preparació dels models i relacions (2.0 punts)

A `motos/models.py` s’han creat tres models:

- **Fabricant**
- **Pilot**
- **Moto**

## 2.1 Relacions entre taules

El model `Moto` conté:

- Una relació **ForeignKey** amb `Fabricant` (una moto té un fabricant).
- Una relació **ManyToManyField** amb `Pilot` (una moto pot tenir diversos pilots i un pilot pot portar diverses motos).

Això compleix el requisit obligatori de tenir relacions entre taules.

Després de definir els models, s’han executat les migracions:

```bash
python manage.py makemigrations
python manage.py migrate
```
# 3. Configuració de l’administrador

A `motos/admin.py` s’han registrat els models perquè apareguin al panell d’administració de Django.

Posteriorment s’ha creat un superusuari:

```bash
python manage.py createsuperuser
```

I s’ha executat el servidor:

```bash
python manage.py runserver
```

Des del panell d’administració (`/admin`) es poden gestionar:

- Fabricants  
- Pilots  
- Motos  
- Usuaris i grups  

---

# 4. Implementació del CRUD (5.0 punts)

Per implementar el sistema CRUD complet s’han creat:

- Vistes (`views.py`)
- URL pròpies de l’app (`motos/urls.py`)
- Formularis (`forms.py`)
- Templates HTML

## 4.1 Configuració d’URLs

S’ha creat el fitxer `motos/urls.py` i s’ha inclòs al fitxer principal `motos_project/urls.py`.

## 4.2 Formularis

S’ha creat `motos/forms.py` utilitzant `ModelForm` per generar el formulari automàticament a partir del model `Moto`.

## 4.3 Vistes

A `views.py` s’han implementat les funcionalitats següents:

- Llistar motos (**Read**)  
- Crear moto (**Create**)  
- Editar moto (**Update**)  
- Eliminar moto (**Delete**)  

Això completa el CRUD:

- Create  
- Read  
- Update  
- Delete  

## 4.4 Templates

S’han creat dos templates dins:

```
motos/templates/motos/
```

- `llista.html`
- `form.html`

Després de crear les vistes i els templates, s’ha reiniciat el servidor i s’ha comprovat que la web funciona correctament.

# 5. Inserció de dades des de l’administrador (1.0 punt)

Des del panell d’administració de Django s’han creat:

- Fabricants  
- Pilots  
- Motos  

Un cop creades aquestes dades, el formulari permet seleccionar fabricant i pilots correctament.

També es pot comprovar que les motos creades apareixen a la pàgina principal del projecte.

---

# 6. Estils CSS

S’ha creat la carpeta d’estàtics:

```
motos/static/motos/css/
```

I dins s’ha afegit el fitxer:

```
styles.css
```

Aquest fitxer inclou els estils tant per a la llista de motos com per al formulari.

Els templates carreguen el CSS utilitzant:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'motos/css/styles.css' %}">
```

---

# 7. Publicació a GitHub (2.0 punts)

El projecte s’ha pujat a GitHub amb:

```bash
git init
git add .
git commit -m "Projecte Django motos amb CRUD complet"
git remote add origin (URL del repositori)
git push -u origin main
```

El repositori inclou:

- Projecte Django complet  
- App `motos`  
- `requirements.txt`  
- `README.md`  
- Fitxers estàtics  

No s’ha inclòs:

- Entorn virtual (`venv`)  
- Base de dades SQLite (`db.sqlite3`)  
---

# 8. Conclusió

En aquest projecte s’ha convertit un array multidimensional en una aplicació web completa amb:

- Base de dades relacional  
- Models amb relacions  
- Administració amb Django Admin  
- CRUD complet amb formularis  
- Templates personalitzats  
- Estils CSS propis  
- Publicació a GitHub  

El projecte compleix tots els requisits demanats a l’enunciat i funciona correctament.
