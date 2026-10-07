# Proyecto: Auditoría de Controles de Acceso, Gestión de Riesgos y Prevención de Fuga de Datos

Este repositorio documenta la investigación de incidentes de seguridad, la evaluación de riesgos operativos y la implementación de controles de seguridad basados en marcos normativos. Los artefactos presentados demuestran capacidades en el análisis de vulnerabilidades, la mitigación de brechas y la gestión de identidades.

## 1. Análisis de Incidentes y Auditoría de Controles de Acceso

**Descripción del Incidente:**
El incidente de seguridad fue originado desde la IP 152.207.255.255 el 10/03/2023 a las 8:29:57 AM. El evento corresponde al contratista legal Robert Taylor Jr. (Usuario: Legal\Administrator), quien operó desde el dispositivo identificado como "Up2-NoGud".

**Vulnerabilidades Identificadas:**
*   **Autorización excesiva:** El contratista operaba con un nivel de autorización de "Admin". Todo el personal en el directorio compartía este mismo nivel de acceso, lo cual representa una violación directa al principio de menor privilegio.
*   **Fallas en el ciclo de vida de identidades:** La cuenta del contratista permaneció activa años después de la fecha de finalización de su contrato, estipulada para el 27/12/2019.

**Plan de Remediación:**
*   **Aplicación de Least Privilege (Privilegio mínimo):** Ajustar de inmediato los controles de autorización para garantizar que los empleados y contratistas cuenten únicamente con los permisos estrictamente necesarios para sus tareas. El acceso "Admin" debe quedar reservado de forma exclusiva para el personal de TI y Seguridad.
*   **Reestructuración del Offboarding:** Implementar un control administrativo riguroso que automatice la revocación de accesos y la desactivación de cuentas en el momento exacto en que un empleado o contratista finaliza su relación laboral.
*   **Auditorías regulares:** Ejecutar revisiones periódicas sobre los registros de acceso y el directorio activo para detectar, bloquear y eliminar cuentas abandonadas o inactivas.

---

## 2. Registro de Riesgos y Evaluación de Amenazas

**Contexto Operativo:**
El entorno de evaluación pertenece a una institución financiera que opera bajo un modelo de trabajo mixto, integrando a 120 empleados entre personal local y remoto. El nivel de exposición ante eventos de seguridad es elevado debido a configuraciones técnicas deficientes que exponen los datos, combinado con las estrictas regulaciones financieras de la industria y la ubicación costera de la sucursal, la cual amplifica el impacto potencial de desastres naturales.

**Matriz de Riesgos:**

| Activo | Riesgo(s) | Descripción | Probabilidad | Gravedad | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fondos | Fuga de registros financieros | Un servidor de bases de datos con copias de seguridad es accesible públicamente. | 3 | 3 | 9 |
| Fondos | Correo electrónico empresarial comprometido | Un empleado es engañado para compartir información confidencial. | 2 | 3 | 6 |
| Fondos | Base de datos de usuarios comprometida | Los datos de los clientes están mal encriptados. | 2 | 3 | 6 |
| Fondos | Robo | La caja fuerte del banco se deja abierta. | 1 | 3 | 3 |
| Fondos | Interrupción de la cadena de suministro | Retrasos en las entregas debido a desastres naturales. | 1 | 3 | 3 |

---

## 3. Prevención de Fuga de Datos y Alineación Normativa (NIST)

**Análisis de Exposición de Información:**
La brecha de seguridad se produjo a raíz de una falla administrativa en la cual un gerente no revocó los accesos a una carpeta de uso interno tras finalizar una reunión. Como consecuencia, un representante de ventas omitió la advertencia de confidencialidad y compartió accidentalmente el enlace de toda la carpeta con un socio comercial externo, en lugar de enviar exclusivamente el material promocional.

**Alineación con NIST SP 800-53:**
*   **Control AC-6 (Privilegio mínimo):** El incidente se aborda bajo el marco normativo AC-6, el cual dictamina que a los usuarios se les debe proporcionar el acceso y la autorización mínimos necesarios para completar una tarea. Este control es fundamental para evitar que los usuarios operen con niveles de privilegio superiores a los requeridos.

**Controles Compensatorios Propuestos:**
1.  **Revocación automatizada de permisos:** Configurar la revocación automática de acceso a la información tras un período de tiempo predefinido. Esto elimina la dependencia del factor humano, asegurando que las concesiones temporales (como las otorgadas para reuniones) se cancelen de manera oportuna.
2.  **Auditoría continua de accesos:** Implementar la auditoría regular de los privilegios de los usuarios. Esta práctica garantiza la identificación de permisos excesivos que hayan pasado desapercibidos, reduciendo de manera efectiva la ventana de oportunidad para filtraciones accidentales futuras.