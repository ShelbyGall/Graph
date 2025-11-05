class Vertex:
    def __init__(self, label: str, data: dict=None):
        self.label = label
        self.data = data

    def get_label(self) -> str:
        return self.label
    
    def get_data(self) -> dict:
        return self.data
    
    def __str__(self) -> str:
        return f"{self.label}|{self.data}"
    
    def __repr__(self) -> str:
        return f"{self.label}|{self.data}"

