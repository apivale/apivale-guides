"""Minimal OpenAI SDK example for APIVALE Gateway."""

import os
from openai import OpenAI


def main() -> None:
    api_key = os.getenv("APIVALE_API_KEY", "")
    if not api_key:
        raise ValueError("Set APIVALE_API_KEY before running.")

    client = OpenAI(base_url="https://apivale.com/v1", api_key=api_key)
    response = client.chat.completions.create(
        model="deepseek-v4.1-flash",
        messages=[{"role": "user", "content": "Reply with one sentence about APIVALE."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
