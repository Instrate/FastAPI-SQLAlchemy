from fastapi import BackgroundTasks, APIRouter
from fastapi.params import Depends

from database.session import get_db

notification_router = APIRouter(
    prefix='/user',
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

def write_notification(email: str, message: str = ""):
    with open('log.txt', 'w') as email_file:
        content = f'notification for {email}: {message}'
        email_file.write(content)

@notification_router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add(write_notification, email, message="some notification")
    return {"message: Notification sent in the background"}
