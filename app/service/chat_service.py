from app.models.chat_history import ChatHistoryRequest
from app.models.chat_request import ChatRequest
from app.service.agent_runner_service import exec_query

## prevalidation is missing (check for empty message, session id exists)
async def exec_chat(request: ChatRequest):
    return await exec_query(message=request.user_msg,session_id=request.session_id,user_id=request.user_id)


async def get_all_messages(request: ChatHistoryRequest):
    pass  ## we can either  fetch from adk session (events in session) or can pull from database