import sqlite3
import pandas as pd

def analizar_logs_sospechosos(db_path):
    """
    Se conecta a la base de datos de seguridad y extrae intentos de 
    inicio de sesión fallidos fuera del horario laboral.
    """
    try:
        # Conexión a la base de datos (simulada)
        conn = sqlite3.connect(db_path)
        
        # Consulta SQL para detectar anomalías
        query = """
        SELECT event_id, username, login_time, ip_address, country 
        FROM log_in_attempts 
        WHERE login_time > '18:00:00' AND success = 0;
        """
        
        # Uso de pandas para formatear la salida de los logs
        df_alertas = pd.read_sql_query(query, conn)
        
        if not df_alertas.empty:
            print("[ALERTA] Se detectaron los siguientes intentos de acceso sospechosos:")
            print(df_alertas.to_string(index=False))
        else:
            print("[INFO] No se detectaron anomalías fuera del horario laboral.")
            
    except sqlite3.Error as error:
        print(f"[ERROR] Fallo al conectar con la base de datos: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # db_path = "security_logs.db"
    # analizar_logs_sospechosos(db_path)
    print("Script de auditoría inicializado. Esperando conexión a BD...")