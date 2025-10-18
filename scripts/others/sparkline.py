from __future__ import annotations
from math import isfinite
from typing import Iterable

def sparkline(
    seq: Iterable[float] | None, 
    *, 
    levels: str = "▁▂▃▅▆▇", 
    lo: float | None = None,
    hi: float | None = None,
    nan_char: str = "·"
) -> str:
    if not levels or len(levels) < 2:
        raise ValueError("levels must contain at least 2 ordered characters!")
    if seq is None:
        return ""

    xs = list(seq)

    finite_vals = [x for x in xs if x is not None and isfinite(x)]
    if not finite_vals:
        return "".join(nan_char for _ in xs)
    
    _lo = min(finite_vals) if lo is None else float(lo)
    _hi = max(finite_vals) if hi is None else float(hi)

    # Avoid divide-by-zero; collapse to middle glyph when flat
    flat = (_hi <= _lo)
    mid_idx = (len(levels) - 1) / 2

    out_chars: list[str] = []
    for v in xs:
        if v is None or not isfinite(v):
            out_chars.append(nan_char)
            continue
        if flat:
            k = round(mid_idx)
        else: 
            t = (float(v) - _lo) / (_hi - _lo)
            t = 0.0 if t < 0.0 else 1.0 if t > 1.0 else t
            k = round(t * (len(levels) - 1))
        out_chars.append(levels[int(k)])
    return "".join(out_chars)
