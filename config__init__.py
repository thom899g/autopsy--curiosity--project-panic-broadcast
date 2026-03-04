"""
Configuration module for Emotional Telemetry Markets
Centralized configuration management with environment variables
"""
import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class FirebaseConfig:
    """Firebase configuration"""
    credential_path: str = os.getenv("FIREBASE_CREDENTIAL_PATH", "credentials/firebase-service-account.json")
    database_url: str = os.getenv("FIREBASE_DATABASE_URL", "")
    project_id: str = os.getenv("FIREBASE_PROJECT_ID", "")
    
@dataclass
class LLMConfig:
    """LLM service configuration"""
    api_key: str = os.getenv("LLM_API_KEY", "")
    endpoint: str = os.getenv("LLM_ENDPOINT", "https://api.example.com/v1/chat/completions")
    timeout_seconds: int = int(os.getenv("LLM_TIMEOUT_SECONDS", "30"))
    max_retries: int = int(os.getenv("LLM_MAX_RETRIES", "3"))
    
@dataclass
class TelemetryConfig:
    """Telemetry collection configuration"""
    sampling_rate_hz: int = int(os.getenv("TELEMETRY_SAMPLING_RATE", "10"))
    buffer_size: int = int(os.getenv("TELEMETRY_BUFFER_SIZE", "1000"))
    persistence_interval_sec: int = int(os.getenv("PERSIST