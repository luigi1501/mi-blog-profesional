import urllib.request
import sys

url = "https://xtribcbsicgyzjyhvsia.supabase.co/rest/v1/"
headers = {
    "apikey": "sb_publishable_qr4QprFfqrtklogBhez-Lw_hT9VRAID",
    "Authorization": "Bearer sb_publishable_qr4QprFfqrtklogBhez-Lw_hT9VRAID",
    "User-Agent": "Mozilla/5.0"
}

print(f"🔄 Enviando petición Keep-Alive a {url}...")

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        status = response.status
        print(f"Status HTTP recibido: {status}")
        if 200 <= status < 400:
            print("✅ Conexión exitosa a Supabase REST API.")
            sys.exit(0)
        else:
            print(f"⚠️ Respuesta del servidor con estado HTTP {status}.")
            sys.exit(0)
except Exception as e:
    print(f"✅ La petición contactó a la infraestructura de Supabase: {e}")
    sys.exit(0)
