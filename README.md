# 🐍 Snake Water Gun Game

A simple, lightweight command-line implementation of the classic **Snake–Water–Gun** game (a variation of Rock-Paper-Scissors) built with Python.

---

## 🚀 Overview
This project is part of my Python foundations journey. It demonstrates the ability to translate real-world logic into code using mathematical shortcuts and clean program structure.

### Key Features:
* **AI Opponent:** Uses random generation for unpredictable gameplay.
* **Modular Logic:** Uses circular arithmetic to determine winners efficiently.
* **Clean Interface:** Simple character-based input for fast play.

---

## 🎮 Game Rules
The winner is decided based on the following interactions:

* **Snake vs. Water:** Snake drinks Water → **Snake wins**.
* **Water vs. Gun:** Water disables Gun → **Water wins**.
* **Gun vs. Snake:** Gun kills Snake → **Gun wins**.
* **Same choices:** It’s a **Draw**.

---

## 🧠 The "Circular" Logic
Instead of using 9 different `if-else` combinations, this game uses **Modular Arithmetic**.



Each option is mapped to a number:
* **Snake** = 0
* **Water** = 1
* **Gun** = 2

The winner is calculated using the formula:
```python
if computer == player:
    result = "Draw"
elif (computer - player) % 3 == 1:
    result = "You Lose"
else:
    result = "You Win"