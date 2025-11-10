from dotenv import load_dotenv
from openai import AzureOpenAI
import os

load_dotenv()

try:
    endpoint = "https://demo-rag-res.openai.azure.com/"
    model_name = "gpt-5-mini"
    deployment = "gpt-5-mini"

    subscription_key = os.environ.get("SUBSCRIPTION_KEY")
    api_version = "2025-04-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key
    )
    
    user_prompt = input("Enter a question: ")
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Be concise and objective.",
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        max_completion_tokens=16384,
        model=deployment,
        n=3
    )

    print("Response: " + response.choices[0].message.content)

except Exception as ex:
    print(ex)