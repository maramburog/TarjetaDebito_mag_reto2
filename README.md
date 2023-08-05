# Tarjeta de Débito OLTP App

Este proyecto es una aplicación de procesamiento de tarjetas de débito basada en clases de Python y el framework Peewee. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en las tablas de Usuario, Cuenta y Tarjeta.

## Características

- Interacción con base de datos SQLite a través de Peewee.
- Funciones CRUD para Usuario, Cuenta y Tarjeta.
- Ejemplo de cómo usar las funciones CRUD en el archivo `main.py`.
- Pruebas automatizadas utilizando pytest.

## Requisitos

- Python 3.x
- Peewee
- pytest

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Navega hasta la carpeta del proyecto en tu terminal.

### Configura el Entorno Virtual (Opcional, pero recomendado)

Crea un entorno virtual para aislar las dependencias del proyecto.

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
# Ejecuta main.py PARA INICIAR


# TEST with PYTEST
En "test_crud.py" edita el texto entre comillas dobles para el usuario a testear antes de cada corrida.
-----  user = create_user("test_user")
```bash
pytest tests/test_update_account.py

```
#OUTPUT RESULT FROM TEST
```bash
=========================================================================================== test session starts ===========================================================================================
platform darwin -- Python 3.9.0rc2, pytest-6.2.5, py-1.11.0, pluggy-1.2.0
rootdir: /Users/miguelaramburo/PycharmProjects/TarjetaDebito
collected 1 item                                                                                                                                                                                          

tests/test_crud.py .                                                                                                                                                                                [100%]

============================================================================================ 1 passed in 0.03s ============================================================================================
(venv) (base) miguelaramburo@MAGBook_pro TarjetaDebito % 
```