import json
import re

from langchain.prompts import PromptTemplate

from utils.inferer import get_local_model_inference


def parse_query_to_dict(query, parser_prompt):
    prompt_template = PromptTemplate.from_template(parser_prompt)
    prompt = prompt_template.format(query=query)
    res = get_local_model_inference(prompt=prompt)
    print(f"res========================> {res}")
    matches = re.findall("({.*?})", res, flags=re.DOTALL)

    if len(matches) > 0:
        return json.loads(next(iter(matches)))
    else:
        return "Sorry, I didn't get it. Can I help you with anything else?"


def get_query_response(
    query: str, context: str = None, final_prompt: str = "", question: str = None
):
    prompt_template = PromptTemplate.from_template(final_prompt)
    inputs = {"query": query}
    if context is not None:
        inputs["context"] = context
    if question is not None:
        inputs["question"] = question
    prompt = prompt_template.format(**inputs)
    return get_local_model_inference(prompt=prompt)
