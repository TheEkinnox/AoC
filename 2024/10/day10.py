from utility import get_grid_size, read_grid


class Node:
    pos = [ ]
    options = [ ]


def get_options( grid, pos ):
    val = str( int( grid[ pos[ 0 ] ][ pos[ 1 ] ] ) + 1 )

    if val == '10':
        return [ ]

    options = [ ]
    lines, cols = get_grid_size( grid )

    def try_add__node( target ):
        if grid[ target[ 0 ] ][ target[ 1 ] ] == val:
            node = Node()
            node.pos = target
            node.options = get_options( grid, target )
            options.append( node )

    if pos[ 0 ] > 0:
        try_add__node( [ pos[ 0 ] - 1, pos[ 1 ] ] )

    if pos[ 0 ] < lines - 1:
        try_add__node( [ pos[ 0 ] + 1, pos[ 1 ] ] )

    if pos[ 1 ] > 0:
        try_add__node( [ pos[ 0 ], pos[ 1 ] - 1 ] )

    if pos[ 1 ] < cols - 1:
        try_add__node( [ pos[ 0 ], pos[ 1 ] + 1 ] )

    return options


def get_trails( grid ):
    trails = [ ]

    lines, cols = get_grid_size( grid )

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            if grid[ line ][ col ] == '0':
                node = Node()
                node.pos = [ line, col ]
                node.options = get_options( grid, node.pos )

                trails.append( node )

    return trails


def check_path( grid, node, out, skip_duplicates = True ):
    val = grid[ node.pos[ 0 ] ][ node.pos[ 1 ] ]

    if val == '9':
        if (not skip_duplicates) or (not node.pos in out):
            out.append( node.pos )

        return True

    if len( node.options ) == 0:
        return False

    result = False

    for child in node.options:
        result |= check_path( grid, child, out, skip_duplicates )

    return result


def step1( path: str ):
    result = 0

    grid = read_grid( path )
    trails = get_trails( grid )

    for trail in trails:
        reachable_nines = [ ]
        check_path( grid, trail, reachable_nines )
        result += len( reachable_nines )

    print( f'Result: {result}\n' )


def step2( path: str ):
    grid = read_grid( path )
    trails = get_trails( grid )

    result = [ ]

    for trail in trails:
        check_path( grid, trail, result, False )

    print( f'Result: {len( result )}\n' )


step1( "input.txt" )
step2( "input.txt" )
