# Investigación y Auditoría de Bases de Datos (SQL)

## Descripción del Proyecto
En este escenario, actué como analista de seguridad para investigar un posible incidente. El objetivo fue analizar registros de bases de datos utilizando consultas SQL para filtrar información crítica en las tablas `log_in_attempts` y `employees`.

## Objetivos Alcanzados
* **Detección de Anomalías:** Identificación de actividades de inicio de sesión sospechosas fuera del horario laboral (después de las 18:00 hrs).
* **Análisis Geográfico y Temporal:** Rastreo de intentos de inicio de sesión en fechas específicas (8 y 9 de mayo) y originados fuera del país principal de operaciones.
* **Gestión de Vulnerabilidades:** Segmentación de la base de datos de empleados utilizando operadores lógicos (`AND`, `OR`, `NOT`) para focalizar la instalación de parches de seguridad críticos en departamentos específicos, excluyendo áreas ya actualizadas (TI).

## Herramientas Utilizadas
* **SQL:** Operadores de filtrado avanzado (`LIKE`, `NOT LIKE`, `AND`, `OR`).
* **Python:** Script de automatización para extracción y visualización de logs (`analisis.py`).