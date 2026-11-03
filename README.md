# Support Ticket Classification

A Python project exploring how language models can turn customer support messages into structured ticket data.

Given a ticket, the project is designed to produce:

- **Category:** technical, account, delivery, billing, or subscription
- **Sentiment:** positive, negative, or neutral
- **Urgency:** low, medium, or high
- **Summary:** a short description of the issue

It includes prompt-building tools, OpenAI-compatible API adapters, local Hugging Face inference utilities, Pydantic schemas, and evaluation experiments.

## Setup

```bash
python -m venv .venv
python -m pip install -r requirement.txt
```

Copy `.env.example` to `.env` and set the model and API values for the inference path you want to use. Keep API keys private; `.env` is excluded from Git.

> This project is a work in progress. It contains experimental modules and notebooks; a polished end-to-end command or deployed service is not yet included.
