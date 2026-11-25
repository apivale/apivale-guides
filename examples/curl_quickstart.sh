#!/usr/bin/env bash
set -euo pipefail

curl -sS https://apivale.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${APIVALE_API_KEY:?Set APIVALE_API_KEY first}" \
  -d '{
    "model": "deepseek-v4.1-flash",
    "messages": [{"role": "user", "content": "Hello from APIVALE!"}]
  }'
