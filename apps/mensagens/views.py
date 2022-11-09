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
        if "object" in data and "entry" in data:
            if data["object"] == "whatsapp_business_account":
                try:
                    for entry in data["entry"]:
                        phoneNumber = entry["changes"][0]["value"]["metadata"][
                            "display_phone_number"
                        ]
                        phoneID = entry["changes"][0]["value"]["metadata"][
                            "phone_number_id"
                        ]
                        profileName = entry["changes"][0]["value"]["contacts"][0][
                            "profile"
                        ]["name"]
                        whatsAppId = entry["changes"][0]["value"]["contacts"][0][
                            "wa_id"
                        ]
                        fromId = entry["changes"][0]["value"]["messages"][0]["from"]
                        messageId = entry["changes"][0]["value"]["messages"][0]["id"]
                        timestamp = entry["changes"][0]["value"]["messages"][0][
                            "timestamp"
                        ]
                        text = entry["changes"][0]["value"]["messages"][0]["text"][
                            "body"
                        ]
                        phone_number = "5592992034133"
                        message = f"RE:{text} was received"
                        sendWhatsApp(phone_number, message)
                except Exception as e:
                    print(e)
        return HttpResponse("success", status=200)


def sendWhatsApp(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN_PERMANENT}
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
