import smtplib
import socket
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========== CONFIGURACIÓN ==========
SMTP_SERVER = "smtp.gmail.com"   # Servidor SMTP (ejemplo con Gmail)
SMTP_PORT = 587
EMAIL_USER = "diego100018@gmail.com"   # Cambia por tu correo
EMAIL_PASS = "#### #### ####"    # Usa una contraseña de aplicación (no la personal)
EMAIL_TO = "diego100018@gmail.com" # Destinatario de la alerta

CHECK_INTERVAL = 60  # Segundos entre verificaciones
TEST_HOST = "8.8.8.8" # Servidor a probar (Google DNS)
TEST_PORT = 53        # Puerto de DNS
TIMEOUT = 3           # Timeout en segundos
# ===================================

def hay_internet():
    """Intenta conectar al host definido, si funciona hay internet."""
    try:
        socket.setdefaulttimeout(TIMEOUT)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((TEST_HOST, TEST_PORT))
        return True
    except socket.error:
        return False

def enviar_alerta():
    """Envía un correo avisando que se cayó internet."""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO
        msg["Subject"] = "⚠ Alerta: Se cayó la conexión a internet"

        body = "El servicio detectó que la conexión a internet se ha caído."
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
        server.quit()

        print(" Alerta enviada por correo.")
    except Exception as e:
        print(f" Error enviando correo: {e}")

def main():
    print("Servicio de monitoreo iniciado...")
    while True:
        if not hay_internet():
            enviar_alerta()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
