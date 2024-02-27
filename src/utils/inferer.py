import requests
import os
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_google_genai import GoogleGenerativeAI

google_api_key = os.getenv("GOOGLE_API_KEY")


def get_results(prompt: str):
    payload = {"prompt": prompt}
    print(payload)
    return requests.post(
        url=os.getenv("MODEL_ENDPOINT"), json=payload, timeout=60
    ).content


def load_local_model(
    n_ctx=8000,
    temperature=0.1,
    max_tokens=500,
    top_p=0.1,
    n_gpu_layers=40,
    n_threads=8,
    n_batch=512,
):
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    return LlamaCpp(
        model_path=os.getenv("MODEL_PATH"),
        n_ctx=n_ctx,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        n_gpu_layers=n_gpu_layers,
        n_threads=n_threads,
        n_batch=n_batch,
        callback_manager=callback_manager,
        verbose=False,
        streaming=False,
    )


llm = GoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=google_api_key,
    temperature=0.8,
    max_output_tokens=5000,
)


def get_local_model_inference(prompt: str):
    return llm.predict(prompt)
