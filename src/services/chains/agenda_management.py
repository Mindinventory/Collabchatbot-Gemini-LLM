from utils.prompts import agenda_management, common
from .commons import get_query_response
from db.cache.caching import get_df_from_cache
from utils import constants
from db import context_manager as cm
from ..validator.validator import ResponseValidator

df = get_df_from_cache(constants.AGENDA_MANAGEMENT)


def response_chain(query: str, user: str):
    print(user)
    context = get_context_from_query(user)
    query_response = get_query_response(
        query=query, context=context, final_prompt=agenda_management.FINAL_PROMPT
    )
    validated_response = ResponseValidator().validate(
        chain_output=query_response, context=context, question=query
    )
    return validated_response


def get_context_from_query(user):
    res = df.loc[df["employee_code"].str.match(user, case=False)]
    if not res.empty:
        context = res.to_dict(orient="records")
    else:
        context = "Could not find any relevant records"
    print(context)
    return context
