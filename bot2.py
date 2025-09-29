from telegram.ext import Application, MessageHandler, filters

# توکن ربات
TOKEN = "484655148:AAFmEy4LuSu0oAQxVcUHeeNX9z3PXFBXeAE"

# تابعی که Chat ID گروه رو نشون میده
async def show_chat_id(update, context):
    chat_id = update.message.chat.id
    print("📌 Chat ID گروه:", chat_id)  # توی کنسول چاپ میشه
    await update.message.reply_text(f"Chat ID این گروه: {chat_id}")

def main():
    app = Application.builder().token(TOKEN).build()

    # هر پیامی که توی گروه بیاد → Chat ID رو برمی‌گردونه
    app.add_handler(MessageHandler(filters.ALL, show_chat_id))

    print("✅ ربات روشن شد! یه پیام توی گروه بفرست تا Chat ID رو بگیری ...")
    app.run_polling()

if __name__ == "__main__":
    main()

