# Bitácora de Inteligencia Artificial - Proyecto FunnyPet Store

**Asistente de IA utilizado:** Google Gemini  
**Proyecto:** Sistema de Gestión de Inventario FunnyPet (Hito 3 - Back End)

---

## Prompt 1: Implementación de Front-End y Arquitectura de Plantillas (Bootstrap 5 + DTL)

* **Rol (R):** Actúa como un desarrollador Full Stack senior especialista en Python, Django y diseño de interfaces responsivas con Bootstrap 5.
* **Tarea (T):** Crear una plantilla maestra (`base.html`) con herencia en Django Template Language (DTL) que incluya una barra de navegación dinámica, renderizado de mensajes flash (`SuccessMessageMixin`) y soporte para archivos estáticos (`custom.css` y logo institucional).
* **Contexto (C):** Estoy desarrollando una aplicación web en Django llamada "FunnyPet Store" conectada a MySQL para gestionar un catálogo de productos y categorías. Necesito unificar el diseño de las vistas CRUD (`lista_productos.html`, `detalle_producto.html`, `producto_form.html`) y ocultar botones administrativos cuando el usuario no haya iniciado sesión (`{% if user.is_authenticated %}`).
* **Formato (F):** Entrega el código HTML completo de `base.html` bien indentado, el código CSS correspondiente para efectos hover en tarjetas y una breve explicación de la estructura de carpetas para `static/`.

---

## Prompt 2: Depuración de Errores de Rutas Estáticas y Dependencias en Entorno Virtual

* **Rol (R):** Actúa como un ingeniero de soporte y depuración de software experto en entornos virtuales de Python, Django y Git.
* **Tarea (T):** Diagnosticar y solucionar un error `404 Not Found` al cargar el logotipo institucional en la barra de navegación y resolver excepciones `ModuleNotFoundError` (`dotenv` y `MySQLdb`) al levantar el servidor local.
* **Contexto (C):** Al ejecutar `python manage.py runserver` dentro de mi entorno virtual `.venv` en Windows, la terminal arroja errores por un atributo `src` mal cerrado en la etiqueta `<img>` de `base.html` y por librerías faltantes tras migrar las credenciales de MySQL a un archivo `.env` protegido en `.gitignore`.
* **Formato (F):** Proporciona la línea HTML exacta corregida, los comandos `pip install` necesarios para restaurar el entorno virtual y los comandos de Git para actualizar el repositorio remoto de forma segura.