import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token
BOT_TOKEN = "7673483122:AAGyk8HAfVJ6D0_xzgJZTtgnhyqpnwXx-2c"

# Folder containing your images
IMAGE_FOLDER = "images"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the user starts the bot."""
    await update.message.reply_text("Hi! Send /image to get a random image.")

async def send_random_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random image from the image folder."""
    try:
        # Get all image files in the folder
        image_files = [f for f in os.listdir("C:/Users/admin/Desktop/image") if f.endswith((".png", ".jpg", ".jpeg", ".jfif"))]
        
        if not image_files:
            await update.message.reply_text("No images available!")
            return

        # Pick a random image
        random_image = random.choice(image_files)
        image_path = os.path.join("C:/Users/admin/Desktop/image", random_image)

        # Send the image
        with open(image_path, "rb") as image:
            await update.message.reply_photo(image)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

def main():
    """Main function to start the bot."""
    # Create the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("image", send_random_image))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
