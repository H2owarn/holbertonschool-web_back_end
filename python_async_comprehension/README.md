# ⚙️ Python Async Generators Project

## 📚 Overview

This project focuses on advanced asynchronous programming techniques in Python. You’ll explore how to write asynchronous generators, leverage async comprehensions for elegant iteration, and apply type annotations to generator-based functions.

By the end of this project, you'll be able to confidently explain and use these features in production-quality code.

---

## 🎯 Learning Objectives

You’ll be able to:

- ✅ Write **asynchronous generators** using `async def` and `yield`.
- ✅ Use **async comprehensions** to iterate over asynchronous data sources.
- ✅ Type-annotate generator functions and async generators using `Generator`, `AsyncGenerator`, and related tools from `typing`.

---

## 🧪 Requirements

- Python 3.6+
- Familiarity with `async/await`, `asyncio`, and the `typing` module

---

## 🛠️ Quick Reference

### 🔁 Asynchronous Generator



```python
async def countdown(n: int):
    while n > 0:
        await asyncio.sleep(1)
        yield n
        n -= 1
