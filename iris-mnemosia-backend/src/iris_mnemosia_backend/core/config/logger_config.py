import logging


def logger_config(debug: bool) -> None:
    logging.basicConfig(
        level=(logging.DEBUG if debug else logging.INFO),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
