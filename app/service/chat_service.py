from datetime import datetime

from app.models.chat_history import ChatHistoryRequest, ChatMessage, ChatHistoryResponse
from app.models.chat_request import ChatRequest, ChatResponse
from app.service.adk.runner_service import run_query
from app.service.adk.session_service import get_ai_user_chat_history
import uuid


## prevalidation is missing (check for empty message, session id exists)
def exec_chat(request: ChatRequest) -> ChatResponse:
    ai_response= run_query(query=request.user_msg,session_id=request.session_id,user_id=request.user_id)
    return ChatResponse(msg_id=str(uuid.uuid4()), message=ai_response,created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


async def get_all_messages(request: ChatHistoryRequest):
    ai_user_history= await get_ai_user_chat_history(session_id=request.session_id, user_id=request.user_id)
    chat_history = []
    for role,message in ai_user_history: ## converting list of tuple to list of ChatMessage object
        chat_history.append(ChatMessage(role=role,message=message))

    return ChatHistoryResponse(messages=chat_history)