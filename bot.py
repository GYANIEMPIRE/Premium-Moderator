import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ Unauthorized")
        return

    await update.message.reply_text(
        "🤖 Premium Moderator Bot\n\n"
        "Commands:\n"
        "/id - Get your Telegram ID\n"
        "/setup - Setup information"
    )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 Your Telegram ID:\n{update.effective_user.id}"
    )


async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ Unauthorized")
        return

    await update.message.reply_text(
        "⚙️ Setup\n\n"
        "1. Add me as Channel Admin\n"
        "2. Give Ban Users permission\n"
        "3. Send the Channel ID\n\n"
        "Example:\n"
        "/channel -1001234567890"
    )


async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ Unauthorized")
        return

    if not context.args:
        await update.message.reply_text(
            "Use:\n/channel -1001234567890"
        )
        return

    channel_id = context.args[0]

    await update.message.reply_text(
        f"✅ Channel saved:\n{channel_id}\n\n"
        "Now the channel is ready for moderation setup.",
        parse_mode="Markdown"
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(CommandHandler("setup", setup))
    app.add_handler(CommandHandler("channel", channel))

    print("Bot is running...")
    app.run_polling()


if name == "main":
    main()
