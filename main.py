from math import floor
from sys import stdout
from time import time


def update_progress(done: int, total: int, bar_amount: int = 20, animation: int = 1):
    # Animations ↓
    wave = ['▁', '▃', '▅', '▇', '█', '▇', '▅', '▃']
    spin = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇']
    arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
    triangles = ['▲', '▶', '▼', '◀', '▲', '▶', '▼', '◀']
    line = ['|', '/', '—', '\\', '|', '/', '—', '\\']
    if animation == 1: symbols = wave.copy()
    elif animation == 2: symbols = spin.copy()
    elif animation == 3: symbols = arrows.copy()
    elif animation == 4: symbols = triangles.copy()
    else: symbols = line.copy()

    _string = ""
    if done != total:
        timer = int((time() - int(time())) * len(symbols))
        if animation == 1:
            for wave in range(3):
                _string += symbols[(timer + len(symbols) + wave % len(symbols)) % len(symbols)]
        else:
            _string += f" {symbols[timer]} "
    else:
        _string += "(!)"

    # Progress bar itself ↓
    _string += " "
    _value = floor(done / total * bar_amount)
    _string += "[" + "█" * _value + "-" * (bar_amount - _value) + "] "
    _string += f"{done}/{total} "
    _string += f"[{done / total * 100:.1f}%]"
    stdout.write(f"\r{_string}")
    stdout.flush()
