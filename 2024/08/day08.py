from math import sqrt, isclose

from utility import read_grid, get_grid_size
from utility.math import is_close


def dist( a, b ):
    difference = [ b[ 0 ] - a[ 0 ], b[ 1 ] - a[ 1 ] ]
    return sqrt( (difference[ 0 ] * difference[ 0 ]) + (difference[ 1 ] * difference[ 1 ]) )


def direction( a, b ):
    distance = dist( a, b )
    return [ (b[ 0 ] - a[ 0 ]) / distance, (b[ 1 ] - a[ 1 ]) / distance ]


def get_antennas( grid ):
    antennas = [ ]

    lines, cols = get_grid_size( grid )

    for l in range( 0, lines ):
        for c in range( 0, cols ):
            if grid[ l ][ c ].isalnum():
                antennas.append( [ grid[ l ][ c ], [ l, c ] ] )

    return antennas


def is_anti_node( antennas, pos ):
    for antenna in antennas:
        if pos == antenna[ 1 ]:
            continue

        cur_dist = dist( pos, antenna[ 1 ] )
        cur_dir = direction( pos, antenna[ 1 ] )

        for other in antennas:
            if antenna[ 0 ] != other[ 0 ] or antenna[ 1 ] == other[ 1 ] or pos == other[ 1 ]:
                continue

            other_dist = dist( pos, other[ 1 ] )

            if isclose( other_dist, (cur_dist * 2) ) and is_close( cur_dir, direction( pos, other[ 1 ] ) ):
                return True


def step1( path: str ):
    grid = read_grid( path )

    anti_nodes = [ ]

    lines, cols = get_grid_size( grid )
    antennas = get_antennas( grid )

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            pos = [ line, col ]
            if not pos in anti_nodes and is_anti_node( antennas, pos ):
                anti_nodes.append( pos )

    print( f'Anti-node count: {len( anti_nodes )}' )


def is_anti_node_v2( antennas, pos ):
    for antenna in antennas:
        cur_dir = direction( pos, antenna[ 1 ] ) if pos != antenna[ 1 ] else None

        for other in antennas:
            if antenna[ 0 ] != other[ 0 ] or antenna[ 1 ] == other[ 1 ] or pos == other[ 1 ]:
                continue

            if cur_dir is None or is_close( cur_dir, direction( pos, other[ 1 ] ) ):
                return True


def step2( path: str ):
    grid = read_grid( path )

    anti_nodes = [ ]

    lines, cols = get_grid_size( grid )
    antennas = get_antennas( grid )

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            pos = [ line, col ]

            if not pos in anti_nodes and is_anti_node_v2( antennas, pos ):
                anti_nodes.append( pos )

    print( f'Anti-node count: {len( anti_nodes )}' )


step1( "input.txt" )
step2( "input.txt" )
