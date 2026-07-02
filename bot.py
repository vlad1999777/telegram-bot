from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8817575346:AAF9JrALOF-x3iSh0pKiRU3Z86QXKaNXbfE"
GROUP_ID = -1003777760609

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(
        chat_id=GROUP_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))

print("Bot started...")
app.run_polling()