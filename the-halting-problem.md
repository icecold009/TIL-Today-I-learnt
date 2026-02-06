# The Halting Problem

The Halting Problem is a classic decision problem in computability theory: **Is it possible to write a program that can determine, for any other program and its input, whether that program will eventually stop (halt) or run forever?**

In 1936, Alan Turing proved that a general algorithm to solve this for all possible program-input pairs **cannot exist**.

---

### 🧠 The Proof by Contradiction

Turing used a clever "self-referential" logic to prove this. Imagine we *could* write a function called `halts(program, input)` that returns `True` if it stops and `False` if it loops forever.

Now, we create a "paradox" program called `Opposite`:
```python
def Opposite(program):
    if halts(program, program):
        while True: # If it halts, we loop forever
            pass
    else:
        return # If it loops forever, we halt
