# Bloque 1: Inicialización del Entorno Profesional

Configuración inicial del proyecto GoSport ubicado en `C:\Users\nicol\.gemini\antigravity\scratch\GoSport` utilizando Django y Tailwind.

## User Review Required

> [!IMPORTANT]
> Se requiere confirmación antes de ejecutar los comandos de inicialización, creación de aplicaciones y configuración base de Django y Tailwind. ¿Estás de acuerdo con proceder con este primer bloque?

## Proposed Changes

### Entorno y Estructura de Proyecto

Inicializaremos el proyecto en el directorio scratch.
Se ejecutarán los siguientes comandos en secuencia para establecer la base:
1. Crear directorio del proyecto y entorno virtual.
2. Instalar dependencias básicas (`django`, `django-tailwind`, `django-browser-reload`, `Pillow`).
3. Iniciar el proyecto principal de Django `GoSport`.
4. Crear las apps requeridas: `core`, `usuarios`, `canchas`, `negocio`.

### Configuración inicial de Django y Tailwind
Modificaremos los archivos base generados para integrar Tailwind:
- Inicializaremos tailwind creando la app `theme`.
- Ajustaremos `GoSport/settings.py` para incluir las apps locales, de terceros, y configuraciones estáticas de Tailwind.

## Verification Plan

### Automated Tests
- Validaremos que el entorno virtual se activa correctamente.
- Validaremos que los comandos de `django-admin` funcionen sin errores.
- Verificaremos que la carpeta `theme` se cree exitosamente.

### Manual Verification
N/A para este primer bloque de solo configuración inicial de carpetas y archivos base.
