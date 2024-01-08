from django.contrib import admin
from m33_messaging.chat.models import (Conversation,
                                        Message)

admin.site.register(Conversation)
admin.site.register(Message)

