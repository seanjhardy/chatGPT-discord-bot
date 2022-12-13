from revChatGPT.revChatGPT import AsyncChatbot as Chatbot
import json
from os import environ as env

async def handle_response(prompt) -> str:
    chatbot.refresh_session()
    response = await chatbot.get_chat_response(prompt, output="text")
    responseMessage = response['message']

    return responseMessage

config = {
    "session_token" : env['session_token']
}

chatbot = Chatbot(config, conversation_id=None)
