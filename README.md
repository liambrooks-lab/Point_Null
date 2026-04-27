# Root_Access

A top-down 2D Pygame/Pygbag browser game prototype.

## Controls

- `WASD`: move
- Left mouse button: shoot
- `E`: build a node when you have at least 10 scrap

## Local Run

```powershell
py -m pip install -r requirements.txt
py main.py
```

## Browser Build

```powershell
py -m pygbag --build .
```

The browser build is generated in `build/web`.

Sound effects are generated in code at runtime so the browser build does not
need external audio files.

## GitHub Pages

This repo includes a GitHub Actions workflow that builds with Pygbag and deploys
`build/web` to GitHub Pages.
