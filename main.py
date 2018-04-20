from microsoftbotframework import MsBot
from tasks import *

bot = MsBot(verify_jwt_signature=False)
bot.add_process(echo_response)

if __name__ == '__main__':
    bot.run()