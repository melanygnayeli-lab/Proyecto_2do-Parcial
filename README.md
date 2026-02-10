Sistema Bancario
Este proyecto consiste en el desarrollo de un Sistema Bancario de escritorio utilizando Python y PySide6. La aplicación fue desarrollada aplicando los principios de Programación Orientada a Objetos y una arquitectura organizada por capas para mantener el código estructurado y fácil de mantener.

El sistema permite registrar y gestionar transacciones bancarias junto con la información del cliente asociado. Se implementaron las operaciones básicas de un CRUD: crear, buscar, actualizar y eliminar registros.

Objetivo del Proyecto

El objetivo principal fue aplicar los conocimientos de:
Programación Orientada a Objetos
Arquitectura por capas
Conexión a base de datos
Diseño de interfaces gráficas con Qt Designer
Además, se buscó que el sistema sea funcional, organizado y fácil de escalar.

Estructura del Proyecto
El proyecto está dividido en varias carpetas:

DATOS
Aquí se maneja todo lo relacionado con la base de datos.
conexion.py: se encarga de establecer la conexión.
ServicioDAO.py: contiene las consultas SQL y las operaciones CRUD.

DOMINIO
Aquí se definen las clases que representan las entidades del sistema.
cliente.py: representa al cliente.
Servicio.py: representa la transacción bancaria.

SERVICIO
Contiene la lógica del negocio.
Servicio_Bancario.py: conecta la interfaz con la base de datos y gestiona las acciones de los botones.

UI
Contiene la ventana principal creada con Qt Designer.
vtnPrincipal.py: diseño de la interfaz gráfica.

main.py
Es el archivo principal que ejecuta la aplicación y muestra la ventana.

Funcionalidades
El sistema permite:

Buscar una transacción por código
Crear una nueva transacción
Actualizar información existente
Eliminar registros
Guardar datos
Limpiar los campos del formulario



Captura de pantalla 
ejecución
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/dc088515-a97f-48e0-a9ee-3eea7a621f6a" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/9aef1d4a-a329-4734-84e9-713e23d51240" />

Actualizar
<img width="1365" height="766" alt="image" src="https://github.com/user-attachments/assets/63bbd6e0-168a-45a4-af50-6c5d35133715" />
<img width="1365" height="766" alt="image" src="https://github.com/user-attachments/assets/2c5fe05d-96ae-4450-8985-44745dd74da4" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/0b1bc447-2f15-4702-ab49-ff5008476626" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/3093cd3e-edf2-4ad0-968d-c2a7d1afbd41" />

Eliminar
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/5571d717-9a7d-4c1a-afc0-f2a2bf93a9ed" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/aed90150-b1e1-4df1-afe9-31a839cbe69c" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/ff826c03-3def-4994-a629-4fca10a5efcc" />

Crear
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/b8b85cd7-01ef-479d-9a71-5e1aae1bd054" />

Validar
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/54aef14f-d8ee-49a6-b939-1b19336dca1d" />

A continuación, link del video

https://drive.google.com/file/d/17jd14Oo1_WKeJCLz2urPjtLDfhh1LhJq/view?usp=sharing











