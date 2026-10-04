# Evaluación de Riesgos y Hardening de Sistemas

## Objetivo
Reporte de evaluación de riesgos centrado en la implementación de controles de seguridad compensatorios para mitigar vulnerabilidades críticas en la infraestructura corporativa, con especial foco en el control de accesos y la seguridad perimetral.

## Controles Implementados y Justificación Técnica

### 1. Configuración de Reglas Estrictas de Firewall (Filtrado de red)
* **Mitigación:** Previene la exfiltración de datos y bloquea el tráfico no autorizado.
* **Implementación:** Despliegue de Listas de Control de Acceso (ACLs) y filtrado de puertos. Las reglas se auditan de forma continua y se revisan al menos una vez al mes o ante cualquier cambio topológico en la red.

### 2. Autenticación Multifactor (MFA)
* **Mitigación:** Soluciona vulnerabilidades críticas relacionadas con contraseñas débiles o cuentas compartidas por empleados.
* **Implementación:** Exigencia obligatoria de dos o más factores de autenticación (ej. credencial + código temporal) en cada intento de inicio de sesión, bloqueando el acceso a atacantes que hayan comprometido contraseñas de primer nivel.

### 3. Gestión de Identidades y Accesos (IAM) 
* **Mitigación:** Elimina el riesgo de credenciales por defecto en administradores de bases de datos y previene el uso compartido de cuentas.
* **Implementación:** Establecimiento de políticas de contraseñas seguras, forzando la rotación de credenciales de fábrica. Creación de cuentas individuales auditables para cada empleado y ejecución de auditorías de acceso periódicas (ej. trimestrales) para garantizar el cumplimiento.