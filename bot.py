from aiogram.utils import executor
from create_bot import dp, bot, admin_id
from handlers import client, admin, other
from db import sqlite_db


async def online(_):
    await bot.send_message(admin_id, 'i`m online 🫡')
    print(' - i`m online!')
    sqlite_db.sql_start()



client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)




executor.start_polling(dp, skip_updates=True, on_startup=online)

