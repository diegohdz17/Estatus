Descripción

Este proyecto implementa un servicio de Windows en Python que monitorea la conexión a internet y, en caso de caída, envía un correo electrónico automático de alerta.

El servicio se instala y administra con NSSM (Non-Sucking Service Manager).

Requisitos

Python

Se recomienda instalar la versión oficial desde python.org

Si tienes problemas con la versión de la Microsoft Store, puedes usar la versión portable (ZIP) desde la misma página:

Descarga el Windows embeddable package (64-bit).

Extrae en C:\Python313\ → ahí tendrás python.exe.

Librerías necesarias

Este script usa solo librerías estándar (smtplib, socket, email).

No necesitas instalar nada extra.

Cuenta de correo con contraseña de aplicación

Si usas Gmail → debes activar verificación en dos pasos y generar una App Password.

En Outlook/Yahoo → también requieren generar contraseña de aplicación.

NSSM

Descárgalo desde: https://nssm.cc/download

Extrae el ZIP y copia nssm.exe a una carpeta fija, por ejemplo:

C:\nssm\nssm.exe
Instalación del Servicio con NSSM

Abrir CMD o PowerShell como administrador.

Instalar el servicio:

C:\nssm\nssm.exe install MonitorInternet


Puedes configurar el servicio para que arranque automáticamente con Windows desde services.msc → Propiedades → Tipo de inicio → Automático.

Recuerda probar primero el script manualmente (python monitor_internet.py) para asegurarte de que el envío de correos funcione antes de instalarlo como servicio.


Eliminar servicio

C:\nssm\nssm.exe remove MonitorInternet

Carga del servicio.

<img width="539" height="281" alt="Captura_nssm" src="https://github.com/user-attachments/assets/0860dbdf-482d-4038-ad13-c0fca24bdee0" />

<img width="444" height="185" alt="CapturaCreado" src="https://github.com/user-attachments/assets/f689b63d-53ed-4dbd-bc83-9e6f020012a2" />

<img width="1013" height="738" alt="CapturaServicio" src="https://github.com/user-attachments/assets/b039dde8-682d-46d0-81b8-0672b12b34d4" />




**Resultados finales**
Aunque se pudo crear el servicio, no se pudieron enviar correos porque mi computadora no pudo activar la aplicacion debido a permisos de seguridad

