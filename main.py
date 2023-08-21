from math import floor
from sys import stdout
from time import time


def bar(done: int, total: int, bar_amount: int = 20, animation: int = 1):
    # Animations ↓
    wave = ['▁', '▃', '▅', '▇', '█', '▇', '▅', '▃']
    spin = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇']
    arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
    triangles = ['▲', '▶', '▼', '◀', '▲', '▶', '▼', '◀']
    line = ['/', '—', '\\', '/', '—', '\\']
    match animation:
        case 1: symbols = wave.copy()
        case 2: symbols = spin.copy()
        case 3: symbols = arrows.copy()
        case 4: symbols = triangles.copy()
        case 5: symbols = line.copy()
        case _: symbols = wave.copy()

    def out(string):
        # Progress bar itself ↓
        string += " "
        _value = floor(done / total * bar_amount)
        string += "[" + "█" * _value + "-" * (bar_amount - _value) + "] "
        string += f"{done}/{total} "
        string += f"[{done / total * 100:.1f}%]"
        stdout.write(f"\r{string}")
        stdout.flush()

    _string: str = ""
    if done == total:
        out(_string := "(!)")
        return
    timer = int((time() - int(time())) * len(symbols))
    if symbols == wave:
        for _wave in range(3):
            _string += symbols[(timer + len(symbols) + _wave % len(symbols)) % len(symbols)]
    else:
        _string += f" {symbols[timer]} "
    out(_string)
