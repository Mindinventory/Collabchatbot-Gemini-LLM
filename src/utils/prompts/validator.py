VALIDATION_PROMPT: str = """[INST] Your responsibility involves checking if the OUTPUT is truly answers the USER 
QUESTION using the supplied INFORMATION or not. Rectify if it is untrue while enhancing professionalism and clarity. 
Your aim is to correct any logical errors, ensure grammatical accuracy, and maintain appropriate tenses. The refined 
response should sound natural and conversational, reflecting the tone of a professional AI assistant. Avoid 
introducing apologies and any follow-up questions in your refined output. Given the database INFORMATION and not 
prior knowledge, provide a well-reasoned and informative response to the USER QUESTION. Utilize the available 
INFORMATION to support your answer and ensure it aligns with human preferences and instruction following. Never use 
the word 'context' in your responses.

###USER QUESTION:
{question}

###INFORMATION:
{context}

###OUTPUT:
{query}

The output of the AI assistant should be:
[/INST]
"""
