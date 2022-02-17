from django.shortcuts import render


# Create your views here.

def start(update, context):
    update.message.reply_text("Assalomu alaykum!")


def message_handler(update, context):
    pass


def recieved_photo(update, context):
    pass
