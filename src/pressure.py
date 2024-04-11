from random import randrange, randint
import logging
from time import sleep


def emit_gel(step):
    while True:
        liguid_value = randrange(50, 100) + randint(min(0, step), max(0, step))
        logging.info(f"Value: {liguid_value}")
        if liguid_value < 10 or liguid_value > 90:
            return GeneratorExit
        yield liguid_value
        sleep(0.1)


def valve():
    step = 1
    generator = emit_gel(step)
    try:
        while True:
            value = next(generator)
            if value < 20 or value > 80:
                generator.send(-step)
            else:
                generator.send(step)
    except StopIteration:
        logging.info("Generator closed by return GeneratorExit")


def main():
    logging.info("Working with generator started")
    valve()
    logging.info("Working with generator ended")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    main()
