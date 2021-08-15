import os
import yaml

from pathlib import Path
from typing import List
from dataclasses import dataclass


PHRASES = None
BASE_DIR = Path(os.path.abspath(os.path.curdir))


@dataclass
class Phrases:
    intermediate: List[List[str]]
    result: List[str]
    no_statistic: str
    already_choice: str
    not_enough_registered: str
    registered: str
    already_registered: str
    no_registered: str


def get_phrases() -> Phrases:
    global PHRASES

    if PHRASES is None:
        with open(BASE_DIR / 'phrases.yaml', 'r') as f:
            PHRASES = Phrases(**yaml.load(f.read(), Loader=yaml.Loader))
    return PHRASES
