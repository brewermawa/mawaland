# Mawaland 🏕️

A Python idle civilization game built as a learning project. Start with a single villager, click your way to your first farmer, and watch your civilization grow automatically.

---

## Project Goals

- Learn and practice **Tkinter** (GUI development)
- Reinforce **OOP** with real object relationships
- Implement a **game loop** for the first time
- Work with **persistent state** across a running application

---

## MVP Scope

The MVP is intentionally minimal. One screen, one resource, one mechanic.

### Mechanics
- Click manually to collect **food**
- Reach **25 food** to buy a new **Mawapeep**
- New Mawapeeps are **unassigned** by default — you must manually assign them as Farmers
- Farmers produce food **automatically** over time
- Everything is visible on a **single screen** at all times

### Game Mechanics

**Food production**
- Each Mawapeep consumes **1 food/sec**
- Each Farmer produces **1 food/sec** (base)
- Net production = farmers - total mawapeeps
- Manual click always available: **+1 food per click**

**Mawapeep cost**
- First Mawapeep: **25 food**
- Each subsequent Mawapeep: **+10% over previous cost** (compounding)

**Farmer production upgrade**
- First upgrade cost: **100 food**
- Effect: **+10% production per farmer**
- Each subsequent upgrade costs **20% more than the previous**

---

### Out of MVP scope
- Technology tree
- Culture
- Multiple screens / navigation
- Save / load
- Additional resources
- Additional roles

---

## Architecture

### Classes

| Class | Type | Responsibility |
|---|---|---|
| `GameState` | dataclass | Holds all game state |
| `Mawapeep` | class | Individual villager object |
| `ResourcePanel` | tk.Frame | Displays food and production rate |
| `ActionPanel` | tk.Frame | Manual click button |
| `VillagerPanel` | tk.Frame | Shows mawapeeps, roles, buy button, assign button for idle mawapeeps |
| `GameEngine` | class | Orchestrates everything — window, panels, game loop |

### GameState members
- `food` — current food amount
- `food_per_sec` — food produced per second (automatic)
- `mawapeeps` — total villager count (int)
- `farmers` — list of `Mawapeep` objects assigned as farmers

### Mawapeep members
- `current_role` — current assigned role (`None` = unassigned)

### Key design decisions
- `GameState` is the single source of truth — panels read from it, never own data
- Panels receive a reference to `GameState` at instantiation
- `GameState` has no knowledge of the UI
- `GameEngine` creates the window, instantiates `GameState`, instantiates panels, and runs the game loop

---

## Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter (stdlib — no external dependencies for MVP)

---

## Roadmap

### MVP (current)
- Single villager
- Manual food collection
- Buy first farmer → automatic production

### Post-MVP (future)
- Additional roles (builder, researcher...)
- Additional resources (wood, stone...)
- Buildings that multiply production
- Technology tree
- Culture system
- Save / load game state
- Multiple screens for advanced systems
- Kivy port for mobile (long term)

---

## Naming Convention

True to the Mawa naming tradition:
- **Game:** Mawaland
- **Villagers:** Mawapeeps

---

*Personal learning project — not intended for distribution or monetization.*
