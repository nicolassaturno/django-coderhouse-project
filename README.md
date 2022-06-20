# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/nicolassaturno/django-coderhouse-project

cd django-coderhouse-project

git checkout developer

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv venv
C:\>venv/Scripts/activate
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```



- Instalar las dependencias del proyecto
```bash

pip install -r requirements.txt
```

- Crear base de datos a partir de las migraciones
```bash
python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```


- Crear estáticos
```bash
python manage.py collectstatic
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
