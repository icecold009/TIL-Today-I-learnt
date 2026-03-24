# Debugging with Breakpoints

A breakpoint pauses code execution at a specific line, letting you inspect variables, the call stack, and program state in real time — far more effective than scattering `print()` statements everywhere.

### How It Works

When the debugger hits a breakpoint, execution pauses before that line runs.
You can inspect all variables in scope, step through code line by line, and resume when ready. The debugger gives you a live window into your program's state at any moment.

---

### Breakpoint Types

**Line breakpoint**
Pauses at a specific line — the most common type.

**Conditional breakpoint**
Pauses only when a condition is true (e.g. `i == 50`). Useful in loops where you don't want to pause 1000 times.

**Logpoint**
Logs a message to the console without stopping execution — great for non-intrusive tracing.

**Exception breakpoint**
Pauses automatically whenever an exception is raised, even if it's caught.

---

### Using Breakpoints in VSCode

Click the gutter (left of line numbers) to set a red dot breakpoint, then press `F5` to start the debugger.

```
F5           → continue to next breakpoint
F10          → step over (next line, don't enter functions)
F11          → step into (go inside the function)
Shift + F11  → step out (finish function, return to caller)
```

For a conditional breakpoint — right-click the red dot → *Edit Breakpoint* → add your condition.

---

### Using `breakpoint()` in Python

Python 3.7+ ships with a built-in that drops you straight into **pdb** in the terminal:

```python
def calculate(x, y):
    result = x / y
    breakpoint()  # execution pauses here
    return result
```

Key pdb commands:

```
n   → next line
s   → step into function
c   → continue
p x → print variable x
q   → quit debugger
```

### References

- [VSCode Debugging Docs](https://code.visualstudio.com/docs/editor/debugging)
- [Python pdb Docs](https://docs.python.org/3/library/pdb.html)
