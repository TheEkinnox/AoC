from math import isclose


def is_close( a: list, b: list ) -> bool:
    if len( a ) != len( b ):
        return False

    for i in range( 0, len( a ) ):
        if not isclose( a[ i ], b[ i ] ):
            return False

    return True
