from src.model.equation import conic
import src.calculate.family
from loguru import logger


def main():
    ita = conic(
        coeff_y2=1,
        coeff_x2=1,
        coeff_xy=0,
        coeff_y=1,
        coeff_x=1,
        constant=1,
    )

    logger.info(ita.readable_equation())

    logger.success(src.calculate.family.is_circle(eq=ita))


if __name__ == "__main__":
    main()
