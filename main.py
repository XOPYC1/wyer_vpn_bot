import telebot
from telebot import types

# ТОКЕН ТВОЕГО БОТА
BOT_TOKEN = "8440825170:AAGt9sCLhMhUnnUmkiieDCK8ApKTaKf6cPE"
bot = telebot.TeleBot(BOT_TOKEN)

# Ссылка на твой сайт Vercel
WEB_APP_URL = "https://wyer-vpn-bot.vercel.app"

# --- 1. НАСТРОЙКА КНОПКИ МЕНЮ (слева от поля ввода) ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопку меню
    web_app = types.WebAppInfo(url=WEB_APP_URL)
    
    # --- ИСПРАВЛЕНО: добавлено type='web_app' ---
    menu_button = types.MenuButtonWebApp(type='web_app', text="Открыть", web_app=web_app)
    # ---------------------------------------------
    
    # Устанавливаем кнопку
    bot.set_chat_menu_button(message.chat.id, menu_button)
    
    bot.send_message(message.chat.id, "👋 Привет! Нажми на синюю кнопку «Открыть» слева от поля ввода, чтобы зайти в личный кабинет.")

# --- 2. ОБРАБОТКА ДАННЫХ ИЗ MINI APP ---
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    
    if data == 'vpn_sweden':
        # Ссылка подписки для Швеции
        sub_link = 'v2raytun://install-config?url=http://77.91.84.106:2096/sub/ego95km8cmaejnni'
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="📥 Нажать для подключения", url=sub_link))
        bot.send_message(message.chat.id, "🇸🇪 Швеция: нажмите кнопку ниже, чтобы добавить конфиг в V2Raytun:", reply_markup=keyboard)
        
    elif data == 'vpn_usa':
        # Ссылка подписки для США
        sub_link = 'v2raytun://install-config?url=http://77.91.84.106:2096/sub/ego95km8cmaejnni'
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="📥 Нажать для подключения", url=sub_link))
        bot.send_message(message.chat.id, "🇺🇸 США: нажмите кнопку ниже, чтобы добавить конфиг в V2Raytun:", reply_markup=keyboard)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
