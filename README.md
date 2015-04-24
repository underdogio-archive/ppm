PPM - Python Package Manager
============================

`ppm` is simply an extension of `pip` to include extra desired behavior.


# Added Behavior
## Requirements.txt Updating

When installing or uninstalling packages having the ability to update your
`requirements.txt` file in one shot.

```bash
ppm install --save ordereddict
```

Will add `ordereddict==1.1` to `requirements.txt`.

Conversely running:

```bash
ppm uninstall --save ordereddict
```

Will remove `ordereddict==1.1` from `requirements.txt`.
