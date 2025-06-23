"""Class for introducing ASHSGamer students."""
class ASHSGamer:
    """Represents a student in the ASHSGamer class."""

    def __init__(self, contact, phone):
        """Initialize with contact details."""
        self.contact = contact
        self.phone = phone

    def introduce(self):
        """Return a contact details string."""
        return f"Send us your feedback at: {self.contact} or call us on: {self.phone}."

    def tell_name(self):
        """Return the student's name."""
        return "My name is: " + self.contact
