# Análisis de Incidente y Respuesta (Framework NIST)

## Resumen del Incidente
La organización sufrió un ataque de Denegación de Servicio (DoS) provocado por una avalancha de paquetes ICMP entrantes. Esto causó que los servicios de la red interna dejaran de responder durante dos horas. La vulnerabilidad de origen fue un cortafuegos mal configurado.

## Aplicación del Marco de Ciberseguridad NIST

### 1. Identificar (Identify)
* **Tipo de ataque:** Denegación de Servicio (DoS) mediante inundación de pings ICMP.
* **Sistemas afectados:** Servicios de la red interna de la organización.
* **Vulnerabilidad:** Cortafuegos sin reglas estrictas de filtrado de tráfico entrante.

### 2. Proteger (Protect)
* Implementación de una regla en el cortafuegos para limitar la tasa (rate limit) de paquetes ICMP entrantes.
* Configuración de verificación de dirección IP de origen en el firewall para detectar y bloquear direcciones IP falsificadas.
* Establecimiento de auditorías periódicas de configuraciones de red.

### 3. Detectar (Detect)
* Instalación de software de supervisión de red para análisis continuo de tráfico y detección de anomalías.
* Despliegue de un sistema de Detección y Prevención de Intrusos (IDS/IPS) para filtrar tráfico ICMP basado en características sospechosas.

### 4. Responder (Respond)
* **Contención:** Aislamiento inmediato de los sistemas afectados bloqueando el tráfico ICMP en el firewall.
* **Neutralización:** Desconexión controlada de servicios no críticos para estabilizar el sistema principal.
* **Análisis:** Extracción de registros del IDS/IPS para determinar el origen, duración y características del incidente.

### 5. Recuperar (Recover)
* Restauración gradual del funcionamiento normal de los servicios no críticos tras la neutralización.
* Monitoreo de rendimiento post-incidente para garantizar la integridad de los datos y el flujo de tráfico legítimo sin interrupciones.