from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ImagePrompts:
    prompt: str
    negative_prompt: str


class PngInfoSaver:
    def __init__(self):
        self._enabled = True

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        self._enabled = enabled

    def update_pnginfo(self, parameters: str, image_prompts: ImagePrompts) -> str:
        if not self._enabled:
            return parameters

        if image_prompts.prompt:
            parameters += f"\nTemplate: {image_prompts.prompt}"

        if image_prompts.negative_prompt:
            parameters += f"\nNegative Template: {image_prompts.negative_prompt}"

        return parameters
