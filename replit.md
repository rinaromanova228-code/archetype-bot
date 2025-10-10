# SoulMap MED - Telegram Bot

## Overview
SoulMap MED is a Telegram bot that helps users discover their psychological archetype through a 12-question personality test. The bot provides personalized mental health and psychosomatic recommendations based on 6 medical archetypes.

## Project Architecture
- **Language**: Python 3.11
- **Framework**: aiogram 2.25.1 (Telegram Bot API library)
- **Type**: Console application (Telegram bot, no web interface)
- **Entry point**: `bot.py`

## Key Features
- 12-question psychological assessment
- 6 archetype profiles (Шизоид, Психастеник, Эпилептоид, Истероид, Неврастеник, Депрессивный)
- Personalized nervous system and psychosomatic insights
- Mental hygiene recommendations
- Partner archetype compatibility information

## Environment Configuration
- **API_TOKEN**: Telegram Bot API token (REQUIRED - must be configured in Replit Secrets)
- The bot uses `os.getenv("API_TOKEN")` to access the token securely
- Without a valid API_TOKEN, the bot will fail to start

## How It Works
1. User starts the bot with `/start` command
2. Bot asks 12 questions with multiple choice answers (A-F)
3. Bot calculates primary archetype based on answers
4. Bot provides detailed profile including:
   - Nervous system characteristics
   - Psychosomatic tendencies
   - Mental hygiene practices
   - Recovery strategies
   - Triggers to avoid
   - Compatible partner archetype

## Dependencies
- `aiogram==2.25.1` - Telegram Bot framework
- `pillow` - Image processing library (for potential future features)

## Recent Changes
- **2025-10-10**: Initial Replit setup
  - Fixed requirements.txt syntax error (removed extra dot from version)
  - Configured Python 3.11 environment
  - Added API_TOKEN to secrets
  - Created replit.md documentation

## Usage
The bot runs continuously and responds to Telegram messages. Users interact through Telegram app, not through a web interface.

## User Preferences
None configured yet - this is a fresh import.
