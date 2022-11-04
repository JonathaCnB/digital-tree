import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


class Send(View):
    def get(self, *args, **kwargs):
        to = "5592992034133"
        message = "Olá, segue menssagem personalizada \n Parabéns!"
        sendWhatsApp(phoneNumber=to, message=message)
        return HttpResponse("Enviando Mensagem")


@method_decorator(csrf_exempt, name="dispatch")
class WebHook(View):
    def get(self, *args, **kwargs):
        VERIFY_TOKEN = settings.TOKEN_WEBHOOK
        mode = self.request.GET["hub.mode"]
        token = self.request.GET["hub.verify_token"]
        challenge = self.request.GET["hub.challenge"]
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        return HttpResponse("error", status=403)

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        return HttpResponse("success", status=200)


def sendWhatsApp(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phoneNumber,
        "type": "text",
        "text": {"body": message},
    }
    response = requests.post(
        settings.WHATSAPP_URL,
        headers=headers,
        json=payload,
    )
    ans = response.json()
    print(ans)
