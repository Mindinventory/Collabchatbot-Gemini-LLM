from db import context_manager as cm
from db.cache.caching import get_df_from_cache
from utils import constants
from utils.prompts import employee_profile as ep
from .commons import parse_query_to_dict, get_query_response
from ..validator.validator import ResponseValidator

df_all = get_df_from_cache(constants.EMPLOYEE_PROFILE)
if df_all is not None:
    df_all["total_leave_balance"] = df_all["total_leave_balance"].fillna(0)
    df_dev = df_all.drop(["total_leave_balance"], axis=1)


def response_chain(query: str, user: str):
    # if role == "dev":
    #     df = df_dev
    # else:
    #     df = df_all
    df = df_all
    query_json = parse_query_to_dict(query=query, parser_prompt=ep.QUERY_PARSER)
    print(query_json)
    context = get_context_from_query(user, df, query_json)
    query_response = get_query_response(
        query=query, context=context, final_prompt=ep.FINAL_PROMPT
    )
    validated_response = ResponseValidator().validate(
        chain_output=query_response, context=context, question=query
    )
    return validated_response


def get_context_from_query(user, df, query_json):
    df_query = cm.specific_context_query(query_json=query_json)
    if df_query:
        res = df.query(cm.specific_context_query(query_json=query_json))
        if len(res) < 1:
            res = df.query(cm.all_context_query(query_json=query_json))
        if len(res) > 5:
            res = res.sample(5)
        if res.empty:
            context = "Couldn't find any relevant context"
        else:
            context = res.to_dict(orient="records")
    else:
        context = df_all.loc[df["employee_code"] == user].to_dict(orient="records")
    return context
