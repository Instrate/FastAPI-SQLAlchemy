from .user import user_router
from .item import item_router
from .notifications import notification_router
from .websocket import websocket_router

#routers = (user_router, item_router, notification_router, websocket_router)
routers = (user_router, item_router, notification_router)