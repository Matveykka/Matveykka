import random
import random
import telebot

# Создаем бота, замените 'YOUR_API_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7337477267:AAGwbNNaOHzz5O9Q-1Yj6YkYnvygJJh2mH4')

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hp = random.randint(50, 100)

    def attack(self, opponent):
        if self.type == 'wizard':
            damage = random.randint(5, 15)
            print(f"{self.name} использует магическую атаку! Нанес {damage} урона.")
        else:  # warrior
            damage = random.randint(10, 20)
            print(f"{self.name} использует супер удар! Нанес {damage} урона.")

        opponent.hp -= damage

    def is_alive(self):
        return self.hp > 0

@bot.message_handler(commands=['start'])
def start_game(message):
    p1 = Pokemon("Покемон1", 'wizard')
    p2 = Pokemon("Покемон2", 'warrior')
    while p1.is_alive() and p2.is_alive():
        p1.attack(p2)
        if not p2.is_alive():
            bot.reply_to(message, f"{p2.name} проиграл!")
            break
        p2.attack(p1)
        if not p1.is_alive():
            bot.reply_to(message, f"{p1.name} проиграл!")

            @bot.message_handler(commands=['info'])

            if message.from_user.username in Pokemon.pokemons.keys():
                pok = Pokemon.pokemons[message.from_user.username]
            def send_welcome(message):
                bot.reply_to(message, """\
            
            """)

bot.polling()
