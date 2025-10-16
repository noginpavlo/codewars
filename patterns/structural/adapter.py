"""
Adapter Pattern: 
allows incompatible classes to work together by converting the interface of an
existing class into one that the client expects. 
Use it when you want to integrate legacy code or third-party libraries without 
modifying them. Advantages: enables reuse, keeps code flexible, and supports 
the Open/Closed Principle.
"""
from abc import ABC, abstractmethod


# ==============================================================
# 1. Target Interface — what the client expects to work with
# ==============================================================

class MusicService(ABC):
    """Modern interface for playing music."""

    @abstractmethod
    def play_song(self, filename: str) -> None: ...


# ==============================================================
# 2. Adapted — existing or legacy class with a different interface
# ==============================================================

class LegacyAudioSystem:
    """Old library that uses a different method name."""

    def play_audio_file(self, filename: str) -> None:
        print(f"[Legacy system] Playing file: {filename}")


# ==============================================================
# 3. Adapter — bridges the Target and the Adapted
# ==============================================================

class LegacyAudioAdapter(MusicService):
    """Adapter that makes LegacyAudioSystem compatible with MusicService."""

    def __init__(self, legacy_system: LegacyAudioSystem) -> None:
        self.legacy_system = legacy_system

    def play_song(self, filename: str) -> None:
        # Translate 'play_song' → 'play_audio_file'
        self.legacy_system.play_audio_file(filename)


# ==============================================================
# 4. Client — uses the Target interface, unaware of the adapted
# ==============================================================

class MusicPlayerApp:
    """High-level component that expects a MusicService."""

    def __init__(self, service: MusicService) -> None:
        self.service = service

    def start_playback(self, filename: str) -> None:
        self.service.play_song(filename)


# ==============================================================
# Usage
# ==============================================================

legacy_player = LegacyAudioSystem()                # Adapted
adapter = LegacyAudioAdapter(legacy_player)        # Adapter wraps Adapted
app = MusicPlayerApp(adapter)                      # Client depends on Target interface

app.start_playback("dreamscape.mp3")
