import dataclasses


@dataclasses.dataclass
class Product:
    label: str = None
    quantity: int = None
    items: list[str] = None
    categories: list[str] = None
