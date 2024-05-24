# 🔎 Sistema Web de Cursos Virtuales

Esta aplicación permite al usuario poder registrar estudiantes, profesores y cursos 😎

## 📽️ Video de Funcionalidad del Sistema Web

Dale Click en el siguiente enlace para ver la presentación del sistema web -> https://youtu.be/YomPoQFtJJ4

## 📝 Funcionalidad del sistema web

El sistema web esta orientado a ser una plataforma de academia, este permite a los usuarios realizar el registro de estudiantes, profesores y cursos. Además, dentro del listado de cada módulo, se puede hacer una búsqueda de un registro en específico:

### 🏠 Vista de Inicio

`http://127.0.0.1:8000/`

> En este enlace se muestra la página de inicio del sistema web.

### 📚 Módulo de Curso

`http://127.0.0.1:8000/curso/`

> En este enlace se muestra un panel con 2 opciones:
>
> - **Registrar curso**: El usuario puede registrar un curso, mediante el siguiente enlace http://127.0.0.1:8000/curso/create/
> - **Listar cursos**: El usuaro puede ver la lista de cursos registrados, mediante el siguiente enlace http://127.0.0.1:8000/curso/list/

### 📚 Módulo de Estudiante

`http://127.0.0.1:8000/estudiante/`

> En este enlace se muestra un panel con 2 opciones:
>
> - **Registrar estudiante**: El usuario puede registrar un estudiante, mediante el siguiente enlace http://127.0.0.1:8000/estudiante/create/
> - **Listar estudiantes**: El usuario puede ver la lista de estudiantes registrados, mediante el siguiente enlace http://127.0.0.1:8000/estudiante/list/

### 📚 Módulo de Profesor

`http://127.0.0.1:8000/profesor/`

> En este enlace se muestra un panel con 2 opciones:
>
> - **Registrar profesor**: El usuario puede registrar un profesor, mediante el siguiente enlace http://127.0.0.1:8000/profesor/create/
> - **Listar profesores**: El usuario puede ver la lista de profesores registrados, mediante el siguiente enlace http://127.0.0.1:8000/profesor/list/

## 🛠️ Cuenta de SuperUsuario

Para acceder al panel de administrador, se utilizó las siguientes credenciales:

```bash
- Usuario: admin
- Contraseña: 123
```

## 🚀 Instalación

1. Clonar el repositorio

```bash
git clone
```

2. Crear un entorno virtual

```bash
python -m venv venv
```

3. Activar el entorno virtual

```bash
source .\venv\Scripts\activate
```

4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

5. Realizar las migraciones

```bash
python manage.py migrate
```

6. Crear un superusuario

```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor

```bash
python manage.py runserver
```

8. Acceder al sistema web

```bash
http://127.0.0.1:8000
```
