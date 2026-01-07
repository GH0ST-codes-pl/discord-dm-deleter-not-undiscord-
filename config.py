"""
Configuration module - environment variables management
"""

import os
from dotenv import load_dotenv

class Config:
    """Class storing bot configuration"""
    
    def __init__(self):
        # Load variables from .env
        load_dotenv()
        
        # Discord user token
        self.user_token = os.getenv("USER_TOKEN", "")
        
        # Channel ID to monitor
        channel_id_str = os.getenv("CHANNEL_ID", "")
        self.channel_id = int(channel_id_str) if channel_id_str else None
        
        # Enable auto-delete in real-time
        auto_delete_str = os.getenv("AUTO_DELETE_ENABLED", "true").lower()
        self.auto_delete_enabled = auto_delete_str in ["true", "1", "yes"]
        
        # Delay between message deletions (in seconds)
        # Note: This is no longer used as we now use random delays for stealth
        delay_str = os.getenv("DELETE_DELAY", "0.5")
        try:
            self.delete_delay = float(delay_str)
        except ValueError:
            self.delete_delay = 0.5
        
        # Enforce minimum delay value (to avoid rate limits)
        if self.delete_delay < 0.3:
            self.delete_delay = 0.3
