from google.adk.sessions import InMemorySessionService,Session
import  uuid
from datetime import datetime

from app.models.init_session import InitSessionRequest, InitSessionResponse

session_service = InMemorySessionService()

async def create_session(request: InitSessionRequest)->InitSessionResponse:
   session_obj:Session = await session_service.create_session(
        app_name= "GoogleADK",
        user_id=request.user_id,
        session_id=str(uuid.uuid4()),
        state={
            "client_id": request.client_id,
            "user_id": request.user_id
        }
    )
   return InitSessionResponse(session_id=session_obj.id,created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

async def get_session_info(session_id:str,user_id:str):
    session_obj=await session_service.get_session(session_id=session_id,app_name= "GoogleADK",user_id=user_id)
    return session_obj.state