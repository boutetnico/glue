from diagonal import DiagonalAlgorithm
from horizontal import HorizontalAlgorithm
from horizontal_bottom import HorizontalBottomAlgorithm
from square import SquareAlgorithm
from square_ordered import SquareOrderedAlgorithm
from vertical import VerticalAlgorithm
from vertical_right import VerticalRightAlgorithm

algorithms = {'diagonal': DiagonalAlgorithm,
              'horizontal': HorizontalAlgorithm,
              'horizontal-bottom': HorizontalBottomAlgorithm,
              'square': SquareAlgorithm,
              'square-ordered': SquareOrderedAlgorithm,
              'vertical': VerticalAlgorithm,
              'vertical-right': VerticalRightAlgorithm}
