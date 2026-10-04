import re

def analizar_trafico(archivo_log):
    """
    Analiza un archivo de captura de tcpdump para detectar puertos inalcanzables.
    """
    print("[*] Iniciando análisis de tráfico de red...\n")
    
    patron_icmp = re.compile(r'ICMP .* udp port (\d+) unreachable')
    patron_dns = re.compile(r'A\? ([a-zA-Z0-9.-]+)')
    
    with open(archivo_log, 'r') as file:
        for linea in file:
            if "unreachable" in linea:
                puerto_match = patron_icmp.search(linea)
                if puerto_match:
                    puerto = puerto_match.group(1)
                    print(f"[ALERTA CRÍTICA] Tráfico bloqueado detectado.")
                    print(f" -> Detalle: El puerto UDP {puerto} se encuentra inalcanzable.")
                    if puerto == "53":
                        print(" -> Diagnóstico: Falla en la resolución DNS. Posible ataque DoS o misconfiguración de Firewall.")
            
            elif "A?" in linea:
                dns_match = patron_dns.search(linea)
                if dns_match:
                    dominio = dns_match.group(1)
                    print(f"[INFO] Intento de resolución DNS detectado hacia: {dominio}")

if __name__ == "__main__":
    # Ejecuta el análisis sobre el log simulado
    analizar_trafico('captura_dns.log')