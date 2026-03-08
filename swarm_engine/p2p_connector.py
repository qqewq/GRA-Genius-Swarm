import asyncio
import websockets
import json
from config import TELEGRAM_BOT_TOKEN

class P2PConnector:
    def __init__(self):
        self.clients = set()

    async def handler(self, websocket, path):
        self.clients.add(websocket)
        print(f"New peer connected. Total: {len(self.clients)}")
        try:
            async for message in websocket:
                data = json.loads(message)
                # Рассылка задачи всем пирам
                await asyncio.gather(
                    *[client.send(json.dumps({"task": data})) for client in self.clients if client != websocket],
                    return_exceptions=True
                )
        finally:
            self.clients.remove(websocket)

    async def start_server(self):
        server = await websockets.serve(self.handler, "localhost", 8765)
        print("🌐 P2P Server started on ws://localhost:8765")
        await server.wait_closed()

# Заглушка для Telegram
def send_telegram_update(message):
    if not TELEGRAM_BOT_TOKEN:
        return
    # Реализация отправки через aiohttp
    pass