from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import load_json
from config import OWNER_ID, SALDO_FILE, STATISTIK_FILE

async def send_main_menu(context, chat_id, user):
    saldo = load_json(SALDO_FILE)
    statistik = load_json(STATISTIK_FILE)
    s = saldo.get(str(user.id), 0)
    stat = statistik.get(str(user.id), {"jumlah": 0, "nominal": 0})

    text = (
        f"👋 Selamat datang di *Store Garfield*!\n\n"
        f"🧑 Nama: {user.full_name}\n"
        f"💰 Saldo: Rp{s:,}\n"
        f"📦 Transaksi: {stat['jumlah']}\n"
    )

    keyboard = [
        [InlineKeyboardButton("📋 List Produk", callback_data="list_produk"),
         InlineKeyboardButton("🛒 Stock", callback_data="cek_stok")],
        [InlineKeyboardButton("💰 Deposit Saldo", callback_data="deposit")],
        [InlineKeyboardButton("📖 Informasi Bot", callback_data="info_bot")],
        [InlineKeyboardButton("📝 Order Langsung", callback_data="direct_order")]
    ]
    if user.id == OWNER_ID:
        keyboard.append([InlineKeyboardButton("🛠 Admin Panel", callback_data="admin_panel")])

    await context.bot.send_message(
        chat_id=chat_id, text=text, 
        reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
    )
  
