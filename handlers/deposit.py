from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import load_json

async def handle_deposit(update, context):
    query = update.callback_query
    nominals = [10000, 15000, 20000, 50000]
    keyboard = [[InlineKeyboardButton(f"Rp{n:,}", callback_data=f"depo_{n}") for n in nominals]]
    keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data="back_to_menu")])
    
    await query.edit_message_text("💰 Pilih nominal deposit:", reply_markup=InlineKeyboardMarkup(keyboard))
  
