# llm.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # load API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def human_readable_eta(driver_id, eta_minutes):
    """
    Use OpenAI GPT to generate a human-friendly delivery message
    """
    prompt = f"""
    A delivery driver with ID {driver_id} is on the way.
    The estimated arrival time is {eta_minutes:.2f} minutes.
    Write a short, friendly, and natural message to inform the customer.
    Keep it under 20 words.
    """

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=30,
            temperature=0.7
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        # fallback to static messages if API fails
        if eta_minutes < 3:
            return f"Driver {driver_id} is very close! Should arrive in a few minutes."
        elif eta_minutes < 10:
            return f"Driver {driver_id} is on the way. Estimated arrival: {round(eta_minutes)} minutes."
        else:
            return f"Driver {driver_id} might be delayed. ETA: {round(eta_minutes)} minutes."
