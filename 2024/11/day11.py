from functools import cache

def blink( stones ):
    for i in range( 0, len( stones ) ):
        if stones[ i ] == '0':
            stones[ i ] = '1'
        elif len( stones[ i ] ) % 2 == 0:
            half_point = len( stones[ i ] ) // 2
            stones.append( str( int( stones[ i ][ half_point: ] ) ) )
            stones[ i ] = str( int( stones[ i ][ :half_point ] ) )
        else:
            stones[ i ] = str( int( stones[ i ] ) * 2024 )


def step1( path: str, blink_count = 25 ):
    with open( path, "r" ) as file:
        stones = file.read().strip( '\n' ).split( ' ' )

    for i in range( 0, blink_count ):
        blink( stones )

    print( f'Result: {len( stones )}\n' )

@cache
def get_stone_count( stone, blink_count, i = 0 ):
    if i == blink_count:
        return 1

    i += 1

    if stone == '0':
        return get_stone_count( '1', blink_count, i )
    elif len( stone ) % 2 == 0:
        half_point = len( stone ) // 2
        return get_stone_count( str( int( stone[ :half_point ] ) ), blink_count, i ) + get_stone_count( str( int( stone[ half_point: ] ) ), blink_count, i )
    else:
        return get_stone_count( str( int( stone ) * 2024 ), blink_count, i )


def step2( path: str, blink_count = 75 ):
    with open( path, "r" ) as file:
        stones = file.read().strip( '\n' ).split( ' ' )

    result = 0

    for stone in stones:
        result += get_stone_count(stone, blink_count)

    print( f'Result: {result}\n' )


step1( "input.txt" )
step2( "input.txt" )