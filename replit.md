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

## Deployment Configuration
- **Type**: Reserved VM (Background Worker)
- **Why**: This bot uses polling mode (not webhooks), which requires a persistent connection to Telegram's API. Autoscale deployments are designed for HTTP servers, not polling-based bots.
- **Run command**: `python bot.py`
- The bot will run continuously in the background when deployed

## Recent Changes
- **2025-10-10**: Deployment configuration fixed
  - Changed deployment type from Autoscale to Reserved VM (Background Worker)
  - Polling-based bots need persistent connections, which Reserved VM provides
  - Removed conflicting workflow instances to prevent API conflicts
  
- **2025-10-10**: Initial Replit setup
  - Fixed requirements.txt syntax error (removed extra dot from version)
  - Configured Python 3.11 environment
  - Removed hard-coded API token for security
  - Added API_TOKEN to secrets (requires valid Telegram bot token)
  - Created replit.md documentation
  - Configured workflow for console output
  - Added .gitignore for Python project

## Usage
The bot runs continuously and responds to Telegram messages. Users interact through Telegram app, not through a web interface.

## Troubleshooting
### Token is invalid error
If you see "Token is invalid!" error:
1. Go to Telegram and find @BotFather
2. Send `/mybots` and select your bot
3. Click "API Token" to view or regenerate your token
4. Update the API_TOKEN in Replit Secrets with the correct token
5. Restart the workflow

### Bot not responding
- Check that the workflow is running (green status)
- Verify the token is correct in Replit Secrets
- Check the console logs for error messages

## User Preferences
None configured yet - this is a fresh import.
