from utils.prompts import team_info, common
from .commons import parse_query_to_dict, get_query_response
from db.cache.caching import get_df_from_cache
from utils import constants
from db import context_manager as cm
from ..validator.validator import ResponseValidator

df = get_df_from_cache(constants.TEAM_INFO).drop(["projects_worked_in"], axis=1)


def response_chain(query: str):
    query_json = parse_query_to_dict(query=query, parser_prompt=team_info.QUERY_PARSER)
    print(query_json)
    context = get_context_from_query(query_json)
    query_response = get_query_response(
        query=query, context=context, final_prompt=team_info.FINAL_PROMPT_0_3
    )
    validated_response = ResponseValidator().validate(
        chain_output=query_response, context=context, question=query
    )
    return validated_response


def get_context_from_query(query_json):
    emp_name = None
    if query_json.get("employee_name", "na") != "na":
        emp_name = query_json.pop("employee_name")
    df_query = cm.specific_context_query(query_json=query_json)
    if df_query:
        res = df.query(cm.specific_context_query(query_json=query_json))
        if len(res) < 1:
            if (skill := query_json.get("skills", "na")) != "na":
                query_dict = {"skills": skill}
                res = df.query(cm.all_context_query(query_dict))
        if len(res) > 6:
            res = res.sample(5)
        print(res)
        if res.empty:
            context = "Couldn't find any relevant context"
        else:
            context = res.to_dict(orient="records")
            print(context)
        if emp_name:
            if isinstance(emp_name, str):
                emp_name = [emp_name]
            context.extend(
                df.loc[
                    df["full_name"].str.contains("|".join(emp_name), case=False)
                ].to_dict(orient="records")
            )
    else:
        context = "Couldn't find any relevant context"
        if emp_name:
            context = df.loc[
                df["employee_name"].str.contains(emp_name, case=False)
            ].to_dict(orient="records")

    return context
