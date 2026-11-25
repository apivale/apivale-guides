# APIVALE Engineering Guides & SDK Quickstarts

**English** | [简体中文](./README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Website](https://img.shields.io/badge/Gateway-apivale.com-6366f1.svg)](https://apivale.com/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
[![Pricing](https://img.shields.io/badge/Pricing-Pay%20As%20You%20Go-emerald.svg)](https://apivale.com/pricing?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)

Curated technical guides, SDK examples, and benchmark references for integrating **DeepSeek-V4.1 Flash**, **DeepSeek-V4 Pro**, **Qwen 3.8 Max**, **GLM-5.3 Flash**, and **Kimi K3** via [APIVALE](https://apivale.com/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides).

## 30-Second Quickstart (OpenAI SDK)

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://apivale.com/v1",
    api_key=os.environ["APIVALE_API_KEY"],
)

resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Hello from APIVALE!"}],
)
print(resp.choices[0].message.content)
```

See runnable examples in [`examples/python_openai_sdk.py`](./examples/python_openai_sdk.py) and [`examples/curl_quickstart.sh`](./examples/curl_quickstart.sh).

## Curated Technical Guides Index

### DeepSeek & High-Throughput Coding
- [DeepSeek V4.1 Flash API Guide: Pricing, Benchmarks & Setup](https://apivale.com/blog/deepseek-v4-flash-api-guide/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- [DeepSeek V4 Flash Vision API Guide](https://apivale.com/blog/deepseek-v4-flash-vision-api-guide/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- [Fixing Custom API Key Rate Limits in DeepSeek Harness](https://apivale.com/blog/deepseek-harness-custom-api-key-rate-limit-fix/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)

### Cursor, Claude Code & IDE Workflows
- [Cursor Pro vs Custom API Key: Cost & Flexibility Breakdown](https://apivale.com/blog/cursor-pro-vs-custom-api-key/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- [Qwen 3.8 Max as a Claude Code Alternative](https://apivale.com/blog/claude-code-opus-5-2-alternative-qwen-3-8-max/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- [Connect GLM-5.3 to Claude Code CLI & Cursor](https://apivale.com/blog/connect-glm-5-3-to-claude-code-cli-cursor/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)

### IoT & Edge Integrations
- [ESP32 MicroPython DeepSeek API Guide](https://apivale.com/blog/esp32-micropython-deepseek-api-guide/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)

## Links

- **Main Gateway**: [https://apivale.com](https://apivale.com/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- **Live Token Pricing**: [https://apivale.com/pricing](https://apivale.com/pricing?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)
- **All Engineering Articles**: [https://apivale.com/blog/](https://apivale.com/blog/?utm_source=github&utm_medium=guides&utm_campaign=apivale_guides)

## License

Released under the [MIT License](./LICENSE).
