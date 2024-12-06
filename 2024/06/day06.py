from utility import read_grid, read_writable_grid


def get_player_info( grid ):
    lines = len( grid )
    cols = len( grid[ 0 ] )

    pos = None
    direction = [ 0, 0 ]

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            symbol = grid[ line ][ col ]
            if symbol == '^':
                direction = [ -1, 0 ]
            elif symbol == '>':
                direction = [ 0, 1 ]
            elif symbol == 'v':
                direction = [ 1, 0 ]
            elif symbol == '<':
                direction = [ 0, -1 ]
            else:
                continue

            pos = [ line, col ]
            break

    return pos, direction


def get_next_direction( direction ):
    return [ direction[ 1 ], -direction[ 0 ] ]


def step1( path: str ):
    grid = read_grid( path )
    lines = len( grid )
    cols = len( grid[ 0 ] )

    pos, direction = get_player_info( grid )
    visited_positions = [ pos ]

    target_pos = [ pos[ 0 ] + direction[ 0 ], pos[ 1 ] + direction[ 1 ] ]

    while 0 <= target_pos[ 0 ] < lines and 0 <= target_pos[ 1 ] < cols:
        if grid[ target_pos[ 0 ] ][ target_pos[ 1 ] ] == '#':
            direction = get_next_direction( direction )
        else:
            pos = target_pos

            if pos not in visited_positions:
                visited_positions.append( pos )

        target_pos = [ pos[ 0 ] + direction[ 0 ], pos[ 1 ] + direction[ 1 ] ]

    print( f'Visited {len( visited_positions )} positions | {visited_positions}' )


def is_loop( grid, start_pos, start_direction ):
    lines = len( grid )
    cols = len( grid[ 0 ] )

    pos = start_pos
    direction = start_direction
    target_pos = [ pos[ 0 ] + direction[ 0 ], pos[ 1 ] + direction[ 1 ] ]
    known_combinations = [ [ pos, direction ] ]

    can_exit = True

    while 0 <= target_pos[ 0 ] < lines and 0 <= target_pos[ 1 ] < cols:
        if grid[ target_pos[ 0 ] ][ target_pos[ 1 ] ] == '#':
            direction = get_next_direction( direction )

            if [ pos, direction ] in known_combinations:
                can_exit = False
                break
            else:
                known_combinations.append( [ pos, direction ] )
        else:
            pos = target_pos

        target_pos = [ pos[ 0 ] + direction[ 0 ], pos[ 1 ] + direction[ 1 ] ]

    return not can_exit


def step2( path: str ):
    grid = read_writable_grid( path )
    lines = len( grid )
    cols = len( grid[ 0 ] )

    pos, direction = get_player_info( grid )
    looping_grids = 0

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            if [ line, col ] == pos:
                continue

            previous_val = grid[ line ][ col ]
            grid[ line ][ col ] = '#'

            if is_loop( grid, pos, direction ):
                looping_grids += 1

            grid[ line ][ col ] = previous_val

    print( f'{looping_grids} looping grids' )


step1( "input.txt" )
step2( "input.txt" )
