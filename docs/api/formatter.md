# Formatter API

The `rwthplots.formatter` module provides figure sizing utilities.

`set_size()` converts a typographic point width — or a named journal/paper
preset — to a `(width_in, height_in)` tuple using the golden ratio for height.
This ensures figures embed in LaTeX documents at exactly the right size without
scaling, which would change the font size relative to the body text.

The conversion formula is:

```
width_in  = width_pt / 72.27
height_in = width_in × (√5 − 1) / 2 × (rows / cols)
```

All 18 named presets and their point widths are listed in
[Style Sheets — Size modifiers](../styles.md#size-modifiers-size).

::: rwthplots.formatter.set_size

::: rwthplots.formatter.list_presets
