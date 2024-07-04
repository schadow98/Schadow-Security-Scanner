class Dependency(object):
    def __init__(self, name, version=None, extra=None):
        self.name       = name
        self.version    = version
        self.extra      = extra
    
    def __str__(self) -> str:
        return f"Name: {self.name} - Version: {self.version} - Extra: {self.extra}"