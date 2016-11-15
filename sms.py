#Thanks To SeedTeam
import requests
import sys
import json
import re
import time
help_text = "\n\nScript ersal sms az API opilo.com by @imandaneshi\nhttps://github.com/SEEDTEAM/python-opilo-script\n\ntarze estefade:\n\npython3 opilo-sms.py send 09120000000 \"Matn morede nazar\"\n  Bara ie ersale SMS\n\npython3 opilo-sms.py credits\n  bara ie gereftane megdare etebar\n\n--json | -j\n baraie gereftane nataiej ba formate JSON\n\nTozihate bishtar\nhttps://goo.gl/zAmOtj\n\n"
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
opilo_number = "300000000000"
username = "********"
password = "********"
errors = {
    "401": "نام کاربری یا رمز عبور اشتباه است",
    "403": "سروریس وب شما فعال نیست.لطفا از پنل ارسال انبوه قسمت  وب سرویس را فعال کنید.",
    "503": "سرور های اپیلو در حال بروز رسانی هستند.",
    "5": "شماره خط وارد شده {} اشتباه است.".format(opilo_number),
    "6": "شماره دریافت کننده نامعتبر است.",
    "7": "اعتبار پیامکی شما به اتمام رسیده است.",
    "8": "خطای نامشخص در سیستم. لطفاً دوباره تلاش نمایید.",
    "9": "متن وارد شده نامعتبر است (طول متن بیش از حد مجاز است).",
}
def is_json():
    for k in sys.argv:
        if k.lower() == "--json" or k.lower() == "-j":
            return True
    return False
def send_sms(number, text, uid):
    data = {
        "username": username,
        "password": password,
        "defaults": {
            "from": opilo_number,
            "text": text,
        },
        "messages":[
            {
                "to": number,
                "uid": uid
            }
        ],
    }
    sms = requests.post(url = "http://bpanel.opilo.com/ws/api/v2/sms/send", json = data, headers={"CONTENT_TYPE":"application/json"})
    if sms.status_code != 200:
        if str(sms.status_code) in errors:
            print(errors[str(sms.status_code)])
            return
        else:
            print("ERROR :" + str(sms.status_code))
    jdat = json.loads(sms.text)
    print(jdat)
