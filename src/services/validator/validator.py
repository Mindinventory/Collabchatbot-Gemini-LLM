from utils.prompts import validator
from ..chains.commons import get_query_response


class ResponseValidator:
    def validate(self, chain_output: str, context: str, question: str):
        return get_query_response(
            query=chain_output,
            context=context,
            question=question,
            final_prompt=validator.VALIDATION_PROMPT,
        )
