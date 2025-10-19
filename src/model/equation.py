import dataclasses


@dataclasses.dataclass
class conic:
    coeff_y2: float
    coeff_xy: float
    coeff_x2: float
    coeff_y: float
    coeff_x: float
    constant: float

    def readable_equation(self) -> str:
        return f"({self.coeff_y2})y^2 + ({self.coeff_xy})xy + ({self.coeff_x2})x^2 + ({self.coeff_y})y + ({self.coeff_x})x + ({self.constant})"
