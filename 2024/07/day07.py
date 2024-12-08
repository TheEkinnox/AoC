from itertools import product

from utility import read_bits


def add( a, b ):
    return a + b


def mult( a, b ):
    return a * b


def combine( a, b ):
    return int( f'{a}{b}' )


def process_line( line: str ) -> (int, list[ int ]):
    tokens = line.split( ':' )
    return int( tokens[ 0 ] ), list( map( int, tokens[ 1 ].strip().split( ' ' ) ) )


def step1( path: str ):
    valid_count = 0

    with open( path, "r" ) as file:
        operators = [ add, mult ]

        for line in file:
            if len( line ) == 0:
                continue

            expected_result, values = process_line( line )

            combinations = pow( len( operators ), len( values ) - 1 )

            for i in range( 0, combinations ):
                result = values[ 0 ]

                for j in range( 1, len( values ) ):
                    op = read_bits( i, j - 1, 1 )
                    result = operators[ op ]( result, values[ j ] )

                if result == expected_result:
                    valid_count += expected_result
                    break

    print( f'Valid entries sum: {valid_count}' )


def step2( path: str ):
    valid_sum = 0

    with open( path, "r" ) as file:
        operators = [ add, mult, combine ]

        for line in file:
            if len( line ) == 0:
                continue

            expected_result, values = process_line( line )

            combinations = product( operators, repeat = len( values ) - 1 )

            for combination in combinations:
                result = values[ 0 ]

                for i in range( 0, len( combination ) ):
                    result = combination[ i ]( result, values[ i + 1 ] )

                if result == expected_result:
                    valid_sum += expected_result
                    break

    print( f'Valid entries sum: {valid_sum}' )


step1( "input.txt" )
step2( "input.txt" )
