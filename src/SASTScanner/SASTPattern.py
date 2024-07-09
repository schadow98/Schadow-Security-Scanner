import json

class SASTPattern(object):
    """
    class for the injection pattern
    """
    def __init__(self, pattern: dict) -> None:
        self.pattern = pattern.get("pattern")
        if not self.pattern:
            raise Exception("SASTPattern is invalid Format: " + json.dumps(pattern, indent=2))
        self.name    = pattern.get("name", "Name not defined")
        self.message = pattern.get("message", "Message not defined")
        self.files   = pattern.get("files", [".py"])
        self.kinds   = pattern.get("kinds", ["src"])