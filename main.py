from telegram.ext import Application, CommandHandler, CallbackQueryHandler, filters, MessageHandler
from config import OWNER_ID
from handlers import menu, produk, deposit
import shutil # Untuk backup

async def backup_task(context):
    shutil.make_archive("backup_data", 'zip', "data_folder_kamu")
    await context.bot.send_document(chat_id=OWNER_ID, document=open("backup_data.zip", "rb"), caption="Daily Backup (4 Hourly)")

def main():
    app = Application.builder().token("TOKEN_BOT_KAMU").build()
    
    # Jalankan backup setiap 4 jam (14400 detik)
    app.job_queue.run_repeating(backup_task, interval=14400, first=10)

    # Handlers
    app.add_handler(CommandHandler("start", menu.send_main_menu_safe))
    app.add_handler(CallbackQueryHandler(produk.handle_list_produk, pattern="^list_produk$"))
    app.add_handler(CallbackQueryHandler(deposit.handle_deposit, pattern="^deposit$"))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
