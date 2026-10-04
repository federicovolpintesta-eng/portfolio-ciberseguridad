-- Recuperar intentos de inicio de sesión fallidos fuera del horario laboral
SELECT * FROM log_in_attempts WHERE login_time > '18:00:00' AND success = 0;

-- Recuperar intentos de inicio de sesión en fechas específicas (Ventana del incidente)
SELECT * FROM log_in_attempts WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

-- Recuperar intentos de inicio de sesión fuera de México (Anomalías geográficas)
SELECT * FROM log_in_attempts WHERE country NOT LIKE 'MEX%';

-- Recuperar empleados en Marketing ubicados en el edificio Este
SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'Este-%';

-- Recuperar equipos de Finanzas o Ventas que requieren actualización crítica
SELECT * FROM employees WHERE department = 'Ventas' OR department = 'Finanzas';

-- Recuperar todos los empleados que no pertenecen a TI (Exclusión de actualizados)
SELECT * FROM employees WHERE NOT department = 'Tecnología de la información';