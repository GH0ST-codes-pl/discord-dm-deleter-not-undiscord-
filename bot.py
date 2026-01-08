"""
Discord DM Auto-Deleter Bot
Automatically deletes your messages from selected private Discord conversations

WARNING: Self-bots violate Discord Terms of Service.
Use at your own risk!
"""

import discord
import asyncio
import os
import random
from datetime import datetime
from colorama import Fore, Style, init
from config import Config

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class DMDeleterBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.delete_count = 0
        self.is_running = True
        
    def log(self, message, level="INFO"):
        """Colored logging with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if level == "SUCCESS":
            color = Fore.GREEN
            icon = "✓"
        elif level == "ERROR":
            color = Fore.RED
            icon = "✗"
        elif level == "WARNING":
            color = Fore.YELLOW
            icon = "⚠"
        else:  # INFO
            color = Fore.CYAN
            icon = "ℹ"
            
        print(f"{Fore.WHITE}[{timestamp}] {color}{icon} {message}{Style.RESET_ALL}")
    
    async def on_ready(self):
        """Event called when logged in"""
        self.log(f"Logged in as {self.user.name} (ID: {self.user.id})", "SUCCESS")
        
        # Display DM information
        dm_channels = [ch for ch in self.private_channels if isinstance(ch, discord.DMChannel)]
        self.log(f"Found {len(dm_channels)} private conversations", "INFO")
        
        # Check if Channel ID is configured
        if self.config.channel_id:
            channel = self.get_channel(self.config.channel_id)
            if channel:
                self.log(f"Monitoring channel: {channel.recipient.name if hasattr(channel, 'recipient') else 'Unknown'}", "INFO")
                
                # Display auto-delete status
                if self.config.auto_delete_enabled:
                    self.log("Auto-delete ENABLED - messages will be deleted in real-time", "SUCCESS")
                
                print(f"\n{Fore.YELLOW}{'='*60}")
                print(f"{Fore.YELLOW}Do you want to delete all existing messages? (y/n){Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{'='*60}\n")
                
                try:
                    choice = input(f"{Fore.CYAN}Choice (y/n): {Style.RESET_ALL}").lower().strip()
                    if choice in ['y', 'yes', 't', 'tak']:
                        # Ask for limit
                        limit_input = input(f"{Fore.CYAN}How many messages to delete? (Press Enter for ALL): {Style.RESET_ALL}").strip()
                        limit = int(limit_input) if limit_input.isdigit() else None
                        
                        # Ask for phrase
                        phrase = input(f"{Fore.CYAN}Delete only messages containing phrase? (Press Enter for NO FILTER): {Style.RESET_ALL}").strip()
                        phrase = phrase if phrase else None
                        
                        await self.delete_all_messages(channel, limit=limit, phrase=phrase)
                except Exception as e:
                    self.log(f"Error reading input: {e}", "ERROR")
            else:
                self.log(f"Channel with ID {self.config.channel_id} not found", "ERROR")
                self.log("Check if Channel ID is correct", "WARNING")
        else:
            self.log("No Channel ID in configuration. Set CHANNEL_ID in .env file", "WARNING")
            self.log("\nAvailable private conversations:", "INFO")
            for ch in dm_channels[:10]:  # Show max 10
                if hasattr(ch, 'recipient'):
                    print(f"  • {ch.recipient.name} - ID: {ch.id}")
        
        self.log("\nBot is running! Press Ctrl+C to exit.", "INFO")
    
    async def on_message(self, message):
        """Event called for every new message"""
        # Check if it's our message in the monitored channel
        if (self.config.auto_delete_enabled and 
            message.author.id == self.user.id and 
            message.channel.id == self.config.channel_id):
            
            try:
                # Random delay to mimic human behavior (0.8-2.5s)
                human_delay = random.uniform(0.8, 2.5)
                await asyncio.sleep(human_delay)
                await message.delete()
                self.delete_count += 1
                self.log(f"Deleted message (total: {self.delete_count})", "SUCCESS")
            except discord.errors.HTTPException as e:
                if e.status == 429:  # Rate limit
                    retry_after = e.retry_after if hasattr(e, 'retry_after') else 5
                    self.log(f"Rate limit! Waiting {retry_after}s...", "WARNING")
                    await asyncio.sleep(retry_after)
                    try:
                        await message.delete()
                        self.delete_count += 1
                    except:
                        self.log("Failed to delete message after retry", "ERROR")
                else:
                    self.log(f"HTTP Error: {e}", "ERROR")
            except Exception as e:
                self.log(f"Error deleting message: {e}", "ERROR")
    
    async def delete_all_messages(self, channel, limit=None, phrase=None):
        """Deletes user's messages from the channel with optional limit and phrase filter"""
        filter_info = f" containing '{phrase}'" if phrase else ""
        limit_info = f" (limit: {limit})" if limit else " (no limit)"
        self.log(f"Starting to delete historical messages{filter_info}{limit_info}...", "INFO")
        
        deleted = 0
        checked = 0
        
        try:
            # Iterate through all messages
            async for message in channel.history(limit=None):
                # Stop if limit reached
                if limit and deleted >= limit:
                    break
                    
                checked += 1
                if message.author.id == self.user.id:
                    # Check phrase filter if provided
                    if phrase and phrase.lower() not in message.content.lower():
                        continue
                        
                    try:
                        await message.delete()
                        deleted += 1
                        self.delete_count += 1
                        
                        if deleted % 10 == 0:
                            self.log(f"Deleted {deleted} messages...", "INFO")
                        
                        # Random delay to mimic human behavior (1.0-3.0s)
                        human_delay = random.uniform(1.0, 3.0)
                        await asyncio.sleep(human_delay)
                        
                    except discord.errors.HTTPException as e:
                        if e.status == 429:  # Rate limit
                            retry_after = e.retry_after if hasattr(e, 'retry_after') else 5
                            self.log(f"Rate limit! Waiting {retry_after}s...", "WARNING")
                            await asyncio.sleep(retry_after)
                        else:
                            self.log(f"HTTP Error while deleting: {e}", "ERROR")
                    except Exception as e:
                        self.log(f"Error: {e}", "ERROR")
            
            self.log(f"Completed! Checked {checked} messages, deleted {deleted}.", "SUCCESS")
            
        except Exception as e:
            self.log(f"Error fetching message history: {e}", "ERROR")

def main():
    """Main program function"""
    print(f"{Fore.RED}{'='*60}")
    print(f"{Fore.RED}    WARNING: SELF-BOT - VIOLATES DISCORD TOS!")
    print(f"{Fore.RED}    Using this tool may result in account ban!")
    print(f"{Fore.RED}{'='*60}\n{Style.RESET_ALL}")
    
    config = Config()
    
    if not config.user_token:
        print(f"{Fore.RED}ERROR: No USER_TOKEN in .env file{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Read README.md to learn how to obtain your token.{Style.RESET_ALL}")
        return
    
    # Create client for self-bot
    client = DMDeleterBot()
    
    try:
        print(f"{Fore.CYAN}Connecting to Discord...{Style.RESET_ALL}\n")
        # Run bot (user token, not bot token!)
        client.run(config.user_token)
    except discord.errors.LoginFailure:
        print(f"\n{Fore.RED}ERROR: Invalid user token!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Check if USER_TOKEN in .env file is correct.{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Shutting down bot...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Total deleted: {client.delete_count} messages{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
