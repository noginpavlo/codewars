# Single Responsibility Principle (SRP)

- **Definition**: A class should have only one reason to change, meaning it should have a single, clearly defined responsibility.
- **Purpose**: Improves maintainability and cohesion by keeping classes focused on one task.
- **Violation Indicators**:
  - A class has unrelated or orthogonal methods.
  - The class must be modified for different, unrelated reasons.
  - Grouping of behaviors that don't belong together (often forming "God objects").

### 🚫 Example of SRP Violation

```python
class SystemMonitor:
    def load_activity(self):
        """Get the events from a source."""
    
    def identify_events(self):
        """Parse raw data into domain events."""
    
    def stream_events(self):
        """Send parsed events to an external agent."""
```

- Each method represents a separate responsibility (loading, parsing, streaming).
- Changing the way events are loaded or streamed affects the entire class.

### ✅ SRP-Compliant Design

Break the class into smaller, focused ones:

- `ActivityLoader`: Responsible for fetching data.
- `EventIdentifier`: Handles event parsing.
- `EventStreamer`: Streams events to consumers.

Each class:
- Is easier to test and maintain.
- Can evolve independently.
- Is reusable in different contexts.

> **Tip**: You don’t have to split responsibilities perfectly at the beginning. Start with a rough design, and use SRP to guide your refactoring as your understanding of responsibilities becomes clearer.

---

# Open/Closed Principle (OCP)

- **Definition**: Software entities (classes, modules, functions, etc.) should be:
  - **Open for extension**: You can add new behavior.
  - **Closed for modification**: You shouldn't have to change existing, working code.

### ✅ Purpose

- Makes the system adaptable to **new requirements** without the risk of breaking existing functionality.
- Encourages the use of **abstractions** and **polymorphism**.
- Promotes code stability and minimizes regression bugs.

### 🚫 Problem Example

In the previous `SystemMonitor` design, the class worked with concrete classes directly. Adding a new event type meant **modifying** the class, which violates OCP.

---

### ✅ Refactored Design for OCP

Introduce an **abstraction** via a base class (`Event`) and use **polymorphism** for extensibility.

```python
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

class UnknownEvent(Event):
    """An event type that couldn't be identified."""

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0 and
            event_data["after"]["session"] == 1
        )

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1 and
            event_data["after"]["session"] == 0
        )

class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)
```

### 🔍 Key Benefits

- `SystemMonitor.identify_event()` is now **closed** to modification.
- Adding new event types (e.g., `PasswordChangeEvent`) only requires creating a **new subclass** of `Event` that defines its `meets_condition()` method.
- Existing logic remains untouched and safe.

---

### 🧠 Design Insight

- The design relies on `Event.__subclasses__()` to dynamically discover event types. This makes the system highly **extensible**.
- You could use more advanced patterns (e.g. `abc` module, plugin registries), but the core idea remains the same.
- The **event class hierarchy is open**, while the **SystemMonitor logic is closed**.

> **OCP encourages extending behavior via new abstractions, not rewriting old ones.**

### 🧠 Final Thoughts on the Open/Closed Principle

- **Polymorphism is key** to effectively applying OCP.
  - Design abstractions that define a **polymorphic contract** clients can rely on.
  - Ensure subclasses **preserve the contract**, allowing new behaviors to be added safely.

- **Why OCP matters**:
  - Enhances **maintainability** by preventing ripple effects.
  - Without OCP, a single change can cause:
    - Widespread code modifications.
    - Unintended side effects or bugs in other parts of the system.

- **Trade-offs and limitations**:
  - Achieving **proper closure** (protection from change) requires well-designed abstractions.
  - Not all abstractions work equally well for every type of future requirement.
  - In practice, aim to **prioritize extensibility** for the parts of the system most likely to change.

> 🎯 **Design Tip**: Apply OCP where change is most expected or impactful. Be strategic about where you invest in extensibility.

---

**Summary**:
- OCP enables change through **extension**, not modification.
- Rely on **polymorphic abstractions** to encapsulate behavior.
- Protect the stability of your system by isolating changes and anticipating future growth areas.

