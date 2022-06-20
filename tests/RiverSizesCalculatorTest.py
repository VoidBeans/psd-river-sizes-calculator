from river_sizes_calculator import *

import unittest

class RiverSizesCalculatorTest(unittest.TestCase):
    def test_determineRiverSizes_1x10(self):
        matrix = [
            [1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
        ]

        riverSizes = determineRiverSizes(matrix)

        assert len(riverSizes) == 2
        assert all(x in [1, 3] for x in riverSizes)

    def test_determineRiverSizes_2x5(self):
        matrix = [
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1]
        ]

        riverSizes = determineRiverSizes(matrix)

        assert len(riverSizes) == 2
        assert all(x in [1, 4] for x in riverSizes)

    def test_determineRiverSizes_5x5(self):
        matrix = [
            [1, 0, 1, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1]
        ]

        riverSizes = determineRiverSizes(matrix)

        assert len(riverSizes) == 3
        assert all(x in [2, 2, 10] for x in riverSizes)

    def test_determineRiverSizes_jagged(self):
        matrix = [
            [1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1],
            [1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
        ]

        riverSizes = determineRiverSizes(matrix)

        assert len(riverSizes) == 5
        assert all(x in [3, 3, 5, 5, 6] for x in riverSizes)
