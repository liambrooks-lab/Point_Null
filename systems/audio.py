import math
import random
from array import array

import pygame


class AudioManager:
    """Small procedural sound system.

    Pygbag rejects common WAV files during web builds, so these short sounds are
    generated in memory instead of loaded from disk.
    """

    def __init__(self):
        self.enabled = False
        self.sounds = {}

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.pre_init(44100, -16, 1, 512)
                pygame.mixer.init()

            self.enabled = True
            self._create_sounds()
        except pygame.error:
            self.enabled = False

    def _create_sounds(self):
        self.sounds["shoot"] = self._make_tone(0.08, 660, 360, 0.16, "sine")
        self.sounds["hit"] = self._make_tone(0.10, 180, 80, 0.20, "noise")
        self.sounds["build"] = self._make_tone(0.22, 240, 700, 0.14, "sine")
        self.sounds["node_hit"] = self._make_tone(0.14, 140, 65, 0.16, "square")

    def _make_tone(self, duration, start_frequency, end_frequency, volume, wave):
        sample_rate = 44100
        sample_count = int(sample_rate * duration)
        samples = array("h")

        for index in range(sample_count):
            progress = index / max(1, sample_count - 1)
            time = index / sample_rate
            frequency = start_frequency + (end_frequency - start_frequency) * progress
            phase = 2 * math.pi * frequency * time

            if wave == "noise":
                value = random.uniform(-1.0, 1.0)
            elif wave == "square":
                value = 1.0 if math.sin(phase) >= 0 else -1.0
            else:
                value = math.sin(phase)

            attack = min(1.0, progress / 0.08)
            release = (1.0 - progress) ** 2.2
            envelope = attack * release
            samples.append(int(value * volume * envelope * 32767))

        return pygame.mixer.Sound(buffer=samples.tobytes())

    def play(self, name):
        if self.enabled and name in self.sounds:
            try:
                self.sounds[name].play()
            except pygame.error:
                pass
