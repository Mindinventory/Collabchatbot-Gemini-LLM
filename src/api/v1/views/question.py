from fastapi import APIRouter, Form
from pydantic import BaseModel
from services.responder.response_generator import ResponseGenerator
from enum import Enum

router = APIRouter(
    prefix="/question",
)

res_gen = ResponseGenerator()


class Intent(str, Enum):
    employee_profile = "employee_profile"
    team_info = "team_info"
    agenda_management = "agenda_management"


class UserQuery(BaseModel):
    user: str
    query: str
    intent: Intent


@router.post("/ask")
async def ask(user_query: UserQuery):
    intent = user_query.intent
    print(f"Intent: {user_query.intent}  |   Query: {user_query.query}")

    if intent == "employee_profile":
        return res_gen.employee_profile(user_query.user, user_query.query)
    elif intent == "team_info":
        return res_gen.team_info(user_query.user, user_query.query)
    elif intent == "agenda_management":
        return res_gen.agenda_management(user_query.user, user_query.query)
    else:
        return "Sorry, I am not trained to answer that yet. Can I help you with anything else?"
