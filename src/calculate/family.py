from src.model.equation import conic
from loguru import logger


def is_circle(eq: conic) -> bool:
    return eq.coeff_x2 == eq.coeff_y2 and eq.coeff_xy == 0
