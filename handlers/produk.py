from telegram import KeyboardButton, ReplyKeyboardMarkup
from database import load_json
from config import PRODUK_FILE

async def handle_list_produk(update, context):
    query = update.callback_query
    produk = load_json(PRODUK_FILE)
    msg = "*LIST PRODUK*\n"
    keyboard = []

    for pid, item in produk.items():
        stok = len(item.get("akun_list", [])) if item.get("akun_list") else item.get("stok", 0)
        status = f"Rp{item['harga']:,}" if stok > 0 else "SOLDOUT ❌"
        msg += f"{pid}. {item['nama']} - {status}\n"
        keyboard.append([KeyboardButton(f"{pid}" if stok > 0 else f"{pid} SOLD")])

    keyboard.append([KeyboardButton("🔙 Kembali")])
    await query.message.delete()
    await context.bot.send_message(
        chat_id=query.from_user.id, text=msg,
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
  
