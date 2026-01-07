# Discord DM Auto-Deleter 🗑️

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20termux-lightgrey.svg)

Automatically delete your messages from Discord private conversations (DMs) in real-time.

## ⚠️ CRITICAL WARNING

### 🚫 Discord Terms of Service Violation

**Self-bots (bots running on user accounts) are STRICTLY PROHIBITED by Discord's Terms of Service!**

Using this tool may result in:
- ❌ **PERMANENT account ban**
- ❌ Loss of access to all servers
- ❌ Loss of all friends and messages
- ❌ IP ban in severe cases

**USE AT YOUR OWN RISK!** This project is for **EDUCATIONAL PURPOSES ONLY**.

### 🔒 Token Security

- Your user token is **sensitive information** - treat it like a password
- **NEVER** share your token with anyone
- **NEVER** commit `.env` file to Git repositories
- Consider changing your Discord password after use (generates new token)

## ✨ Features

- ✅ **Real-time auto-delete** - Every new message is automatically deleted
- ✅ **Bulk delete** - Delete all historical messages from selected DM
- ✅ **Stealth mode** - Random delays (0.8-2.5s) mimic human behavior
- ✅ **Colorful console** - Timestamped logs with status indicators
- ✅ **Rate limit handling** - Automatic retry with exponential backoff
- ✅ **Cross-platform** - Works on Linux, Windows, macOS, Termux
- ✅ **Easy setup** - Automated setup scripts for all platforms

## 📋 Requirements

- **Python 3.8+**
- Discord account (will be used as self-bot)
- Internet connection

## 🚀 Quick Start

### Linux / macOS / Termux

```bash
# Clone or download the repository
cd discord-dm-auto-deleter-github

# Run automated setup
chmod +x setup.sh
./setup.sh

# Edit configuration
nano .env  # or vim, vi, etc.

# Activate virtual environment
source venv/bin/activate

# Run bot
python bot.py
```

### Windows

```cmd
REM Download and extract the repository
cd discord-dm-auto-deleter-github

REM Run automated setup
setup.bat

REM Edit configuration
notepad .env

REM Activate virtual environment
venv\Scripts\activate.bat

REM Run bot
python bot.py
```

## 📱 Platform-Specific Instructions

<details>
<summary><b>🐧 Linux</b></summary>

### Prerequisites

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

### Installation

```bash
./setup.sh
```

The script will:
1. Check Python version
2. Create virtual environment
3. Install dependencies
4. Create `.env` from template

</details>

<details>
<summary><b>🪟 Windows</b></summary>

### Prerequisites

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Restart terminal after installation

### Installation

```cmd
setup.bat
```

The script will:
1. Check Python version
2. Create virtual environment
3. Install dependencies
4. Create `.env` from template

**Troubleshooting:**
- If `python` not found, try `py` or `python3`
- Run as Administrator if permission errors occur

</details>

<details>
<summary><b>📱 Termux (Android)</b></summary>

### Prerequisites

```bash
# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install git (if cloning repo)
pkg install git
```

### Installation

```bash
# Clone repository (or download and extract)
git clone <repository-url>
cd discord-dm-auto-deleter-github

# Run setup script
chmod +x setup.sh
./setup.sh

# Edit configuration
nano .env
```

**Termux Notes:**
- No `sudo` needed in Termux
- Grant storage permission: `termux-setup-storage`
- Termux may sleep - use wake locks or keep app active

</details>

## 🔑 Getting Your User Token

### Method 1: Browser Developer Tools (Recommended)

1. Open Discord in browser: https://discord.com/app
2. Log in to your account
3. Press `F12` or `Ctrl+Shift+I` (open DevTools)
4. Go to **Network** tab
5. Press `F5` to reload page
6. In filter, type: `api`
7. Click any request to `discord.com/api`
8. In **Headers** tab, find **Request Headers**
9. Find line `authorization:` - the value is your token
10. **Copy the token** (without "authorization:")

### Method 2: Console Script

⚠️ **Warning:** Discord may detect token extraction attempts!

1. Open Discord in browser
2. Press `F12` and go to **Console** tab
3. Paste and execute:

```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

4. Copy the displayed token

## 🆔 Finding Channel ID

1. Enable **Developer Mode** in Discord:
   - Settings → Advanced → Developer Mode ✓
2. Right-click on **private conversation** in DM list
3. Select **Copy ID**
4. Paste ID into `.env` file

## ⚙️ Configuration

Edit `.env` file:

```env
USER_TOKEN=your_discord_user_token_here
CHANNEL_ID=123456789012345678
AUTO_DELETE_ENABLED=true
DELETE_DELAY=0.5
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `USER_TOKEN` | Your Discord account token | (required) |
| `CHANNEL_ID` | DM conversation ID to monitor | (required) |
| `AUTO_DELETE_ENABLED` | Enable real-time auto-delete | `true` |
| `DELETE_DELAY` | Legacy parameter (now uses random delays) | `0.5` |

### Stealth Mode

Bot uses **randomized delays** to avoid detection:
- **Real-time delete**: 0.8 - 2.5 seconds (mimics human reaction)
- **Bulk delete**: 1.0 - 3.0 seconds (mimics manual deletion)

## 🎮 Usage

### Starting the Bot

```bash
# Activate virtual environment (if not already)
source venv/bin/activate  # Linux/Mac/Termux
venv\Scripts\activate.bat  # Windows

# Run bot
python bot.py
```

### What Happens

1. Bot logs into your Discord account
2. Displays account info and available DMs
3. Asks: **"Delete all existing messages? (y/n)"**
   - `y` - Deletes all old messages from DM
   - `n` - Skips bulk delete
4. Starts **real-time monitoring**
   - Every message you send in this DM will be auto-deleted

### Stopping the Bot

Press `Ctrl+C` - bot displays statistics and exits safely.

## 📊 Example Output

```
============================================================
    WARNING: SELF-BOT - VIOLATES DISCORD TOS!
    Using this tool may result in account ban!
============================================================

Connecting to Discord...

[10:30:45] ✓ Logged in as JohnDoe (ID: 123456789)
[10:30:45] ℹ Found 5 private conversations
[10:30:45] ℹ Monitoring channel: Alice
[10:30:45] ✓ Auto-delete ENABLED - messages will be deleted in real-time

============================================================
Do you want to delete all existing messages? (y/n)
============================================================

Choice: y
[10:30:50] ℹ Starting to delete historical messages...
[10:31:00] ℹ Deleted 10 messages...
[10:31:15] ℹ Deleted 20 messages...
[10:31:25] ✓ Completed! Deleted 25 messages.
[10:31:25] ℹ Bot is running! Press Ctrl+C to exit.

[10:32:10] ✓ Deleted message (total: 26)
[10:33:05] ✓ Deleted message (total: 27)
```

## 🛠️ Troubleshooting

### "ERROR: Invalid user token!"

- Check if token in `.env` is correct
- Token should not contain spaces or quotes
- Make sure you copied the entire token
- Try generating new token (change Discord password)

### "Channel with ID ... not found"

- Verify Channel ID is correct
- Ensure you have access to that channel
- Channel ID must be a number (no quotes in .env)

### "Rate limit! Waiting Xs..."

- This is normal - Discord limits operations
- Bot will automatically wait and retry
- For frequent rate limits, increase delays (edit bot.py)

### Bot won't connect

- Check internet connection
- Verify Discord is not down: https://discordstatus.com
- Try regenerating token (change password)

### Python not found (Windows)

- Reinstall Python with "Add to PATH" checked
- Try `py` or `python3` instead of `python`
- Restart terminal after Python installation

### Permission denied (Linux/Termux)

```bash
chmod +x setup.sh
chmod +x bot.py
```

## 📂 Project Structure

```
discord-dm-auto-deleter-github/
├── bot.py              # Main bot script
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── .env.example        # Configuration template
├── .gitignore          # Git ignore rules
├── setup.sh            # Linux/macOS/Termux setup
├── setup.bat           # Windows setup
├── LICENSE             # MIT License
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request

## � Support the Project

If you find this project helpful, consider supporting the developer:

[![Support on Tipply](https://img.shields.io/badge/Tipply-Support%20Me-orange?style=for-the-badge&logo=buy-me-a-coffee)](https://tipply.pl/@daily-shoty)

**Support via Tipply:** [https://tipply.pl/@daily-shoty](https://tipply.pl/@daily-shoty)

Your support helps maintain and improve this project! 🙏

## �📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## ⚖️ Disclaimer

This tool was created for **EDUCATIONAL PURPOSES ONLY**. The authors:

- ❌ Do **NOT** encourage use of self-bots
- ❌ Take **NO** responsibility for account bans
- ❌ Provide **NO** warranty or guarantees
- ❌ Offer **NO** support for banned accounts

**By using this software, you:**
- Understand the risks involved
- Accept full responsibility for consequences
- Will not hold authors liable for damages
- Are using at your own risk

## 🔗 Resources

- [Discord Developer Portal](https://discord.com/developers/docs)
- [discord.py-self Documentation](https://github.com/dolfies/discord.py-self)
- [Discord Terms of Service](https://discord.com/terms)

---

**Remember: Self-bots = ToS violation = Account ban risk!** 🚫

*Use responsibly and at your own risk.*
