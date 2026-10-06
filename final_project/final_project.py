import telebot
from logic import 

TOKEN = ""

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой помошник в экологии. Отправь мне фотографию или скажи из чего состоит предмет, а я отвечу куда отнести и что из переработанного сделают")

@bot.message_handler(commands=["Стекло"])
def send_message(message):
    bot.reply.to(message,"Стеклоприемник, там стекло переплавят и могут сделать посуду, вазы и тд.")

@bot.message_handler(commands=["пластик"])
def send_message(message):
    bot.reply.to(message,"Пластикоприемник, из него сделают новые игрушки, одежду, одноразовую посуду и тд.")

@bot.message_handler(commands=["Металл", "алюминий","железо"])
def send_message(message):
    bot.reply.to(message,"Металлоприемник, тут из его переплавят и дальше изготовят запчастидля автомобилей, велосипедов и др.")

@bot.message_handler(commands=["Опасные отходы","батарейки","электроника"])
def send_message(message):
    bot.reply.to(message,"Пункты сбора или мастерские по ремонту устройств.")
    


bot.polling()