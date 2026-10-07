class Task:
    """Represents a single task with a title, priority, and completion status."""

    #class variable - shared across all instances
    VALID_PROPERTIES = ["low", "medium", "high"]

    def __init__(self, title, priority="medium"):
        self.title = title
        self.completed = False  #all tasks start as incomplete

         # Ensure priority level before setting it


