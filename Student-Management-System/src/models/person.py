"""Person: the abstract base class of the system (Abstraction + Encapsulation)."""

from abc import ABC, abstractmethod

from exceptions import ValidationError


class Person(ABC):
    """Abstract base class for every person in the system."""

    total_people_created = 0  # class (static) attribute shared by all objects

    def __init__(self, person_id, name, email, age):
        """Constructor: validation happens in the property setters."""
        self._person_id = person_id  # protected: never changes after creation
        self.name = name             # uses the name setter (validation)
        self.email = email           # uses the email setter (validation)
        self.age = age               # uses the age setter (validation)
        Person.total_people_created += 1

    # ---- encapsulated attributes (getters / setters with validation) ----
    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = str(value).strip()
        if not value or not all(ch.isalpha() or ch in " -'." for ch in value):
            raise ValidationError(
                "Name must not be empty and can only contain letters, "
                "spaces, hyphens, apostrophes and dots."
            )
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        value = str(value).strip()
        parts = value.split("@")
        if len(parts) != 2 or not parts[0] or "." not in parts[1] or " " in value:
            raise ValidationError("Email must look like name@example.com.")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValidationError("Age must be a whole number.")
        if not 16 <= value <= 100:
            raise ValidationError("Age must be between 16 and 100.")
        self._age = value

    # ---- abstract methods: every subclass MUST implement these ----
    @abstractmethod
    def get_role(self):
        """Return the role of the person (e.g. 'Student')."""

    @abstractmethod
    def get_summary(self):
        """Return a one-line summary of the person."""

    # ---- concrete method shared by all subclasses ----
    def introduce(self):
        """Uses the abstract methods -> the output depends on the real class."""
        return f"[{self.get_role()}] {self.get_summary()}"

    def __str__(self):
        return self.introduce()
