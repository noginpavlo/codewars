# GoF Design Patterns and Their Fit in Python

## 🧱 Creational Patterns

| Pattern | Used in Python? | If not, why |
|----------|----------------|-------------|
| Singleton | ❌ | Modules or globals already serve this purpose |
| Factory Method | ✅ | – |
| Abstract Factory | ✅ | – |
| Builder | ✅ | – |
| Prototype | ⚠️ | `copy` / `deepcopy` already handle cloning |

---

## 🧩 Structural Patterns

| Pattern | Used in Python? | If not, why |
|----------|----------------|-------------|
| Adapter | ✅ | – |
| Bridge | ✅ | – |
| Composite | ✅ | – |
| Decorator | ✅ | Native language feature (`@decorator`) |
| Facade | ✅ | – |
| Flyweight | ⚠️ | Python’s memory model makes it rarely useful |
| Proxy | ✅ | – |

---

## ⚙️ Behavioral Patterns

| Pattern | Used in Python? | If not, why |
|----------|----------------|-------------|
| Chain of Responsibility | ✅ | – |
| Command | ✅ | – |
| Interpreter | ✅ | – |
| Iterator | ❌ | Built into the language |
| Mediator | ✅ | – |
| Memento | ✅ | – |
| Observer | ✅ | – |
| State | ✅ | – |
| Strategy | ✅ | – |
| Template Method | ⚠️ | Higher-order functions often replace it |
| Visitor | ⚠️ | Dynamic typing makes it less necessary |

