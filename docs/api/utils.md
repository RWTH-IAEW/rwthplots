# Utilities API

The `rwthplots.utils` module provides four helper functions, all re-exported
from the top-level `rwthplots` namespace:

```python
import rwthplots

rwthplots.save_figure(...)
rwthplots.context(...)
rwthplots.pick_colors(...)
rwthplots.check_accessibility(...)
```

## Figure export

::: rwthplots.utils.save_figure

## Style context

::: rwthplots.utils.context

## Colour selection

::: rwthplots.utils.pick_colors

## Accessibility

::: rwthplots.utils.check_accessibility

---

## CVD simulation background

`check_accessibility()` uses the **Viénot-Brettel-Mollon model** (1997/1999)
to simulate how a palette appears to observers with colour vision deficiency.

The simulation pipeline for each colour:

1. **sRGB → linear RGB** — remove gamma correction (IEC 61966-2-1).
2. **Linear RGB → LMS** — transform to the three cone types using the
   Hunt-Pointer-Estévez / Bradford D65 adaptation matrix.
3. **Apply CVD confusion matrix** — collapse the affected cone channel(s) to
   reproduce the confusion experienced by each CVD type.
4. **LMS → linear RGB** — invert the cone-space transform.
5. **Linear RGB → CIELAB** — convert to a perceptually uniform space.
6. **CIE 1976 ΔE** — measure Euclidean distance between simulated pairs.
   Pairs below the threshold are flagged as confusable.

The confusion matrices and sRGB constants are taken from the
[daltonize](https://github.com/joergdietrich/daltonize) project (MIT license),
which implements the same model.

| CVD type | Cone affected | Prevalence (males) |
|---|---|---|
| Deuteranopia | M (medium) | ~6 % |
| Protanopia | L (long) | ~2 % |
| Tritanopia | S (short) | ~0.003 % |
