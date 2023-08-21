from math import floor
from sys import stdout
from time import time, sleep


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

    if done == total:
        out("(!)")
    else:
        _string: str = ""
        timer = int((time() - int(time())) * len(symbols))
        if symbols == wave:
            for _wave in range(3):
                _string += symbols[(timer + len(symbols) + _wave % len(symbols)) % len(symbols)]
        else:
            _string += f" {symbols[timer]} "
        out(_string)


# make sure the import sleep in line #3
for i in range(5):
    print("\n")
    for j in range(1001):
        bar(j, 1000, 20, i + 1)
        sleep(0.002)
