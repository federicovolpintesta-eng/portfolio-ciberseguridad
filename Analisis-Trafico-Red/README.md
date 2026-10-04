# Análisis de Tráfico de Red y Controles de Seguridad

## Descripción del Incidente
Se reportó una interrupción del servicio a las 1:24 p.m. donde los clientes recibían un mensaje de "puerto de destino inalcanzable" al intentar acceder al dominio `yummyrecipesforme.com`. Se realizó una investigación utilizando `tcpdump` para realizar sniffing de paquetes y diagnosticar el problema en la infraestructura.

## Análisis Técnico de Logs (tcpdump)
* **Protocolo y Puerto:** Se identificó tráfico UDP intentando contactar al servidor DNS para recuperar la dirección IP del dominio.
* **Diagnóstico:** Los registros mostraron mensajes de error ICMP indicando `udp port 53 unreachable` en respuesta a las consultas DNS (identificadas por la bandera `A?` y el ID de consulta `35084+`).
* **Conclusión:** El servidor DNS no está respondiendo. La causa subyacente apunta a una caída del servidor (posible ataque DoS exitoso) o a que el tráfico hacia el puerto 53 está siendo bloqueado por el firewall perimetral.

## Propuesta de Mitigación y Categorías de Control
Para prevenir y mitigar futuros incidentes de esta naturaleza, se recomienda la implementación de controles estructurados bajo el marco de defensa en profundidad:

1. **Controles Técnicos Preventivos:**
   * **Firewall:** Filtrado de tráfico anómalo para prevenir ataques de denegación de servicio que saturen el puerto 53.
   * **Privilegio Mínimo (Control Administrativo/Preventivo):** Asegurar que las reglas del firewall y del servidor DNS solo puedan ser modificadas por personal autorizado, reduciendo el riesgo de misconfiguraciones accidentales o maliciosas.

2. **Controles Técnicos Detectivos:**
   * **IDS/IPS:** Detección y prevención en tiempo real de tráfico anómalo (como inundaciones de solicitudes DNS) que coincida con firmas de ataques conocidos.

3. **Controles Físicos y Administrativos:**
   * **Planes de recuperación ante desastres (Correctivo):** Establecer redundancia de servidores DNS para garantizar la continuidad del negocio en caso de un ataque DoS efectivo.
   * **Gabinetes con cerradura (Físico/Preventivo):** Asegurar la integridad del hardware de red para evitar alteraciones físicas no autorizadas en el enrutamiento.