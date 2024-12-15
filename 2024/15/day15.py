from utility import read_writable_grid, get_grid_size, print_grid


class Terrain:
    player: list[ int ]
    grid: list[ list[ chr ] ]

    def __init__( self, grid ):
        self.grid = grid

        lines, cols = get_grid_size( grid )

        for line in range( 0, lines ):
            for col in range( 0, cols ):
                if grid[ line ][ col ] == '@':
                    self.player = [ line, col ]
                    return

        assert False  # "No player in the grid"


def get_direction( char: chr ):
    if char == '<':
        return [ 0, -1 ]
    elif char == '>':
        return [ 0, 1 ]
    elif char == '^':
        return [ -1, 0 ]
    elif char == 'V' or char == 'v':
        return [ 1, 0 ]


def parse_input( path: str ) -> (Terrain, list[ chr ]):
    terrain = Terrain( read_writable_grid( path ) )
    moves = [ ]

    lines, cols = get_grid_size( terrain.grid )

    with open( path, "r" ) as file:
        cur_line = 0

        for line in file:
            if cur_line < lines:
                cur_line += 1
                continue

            line = line.strip()

            if len( line ) == 0:
                continue

            for c in line:
                moves.append( c )

    return terrain, moves


def do_move( terrain: Terrain, origin: list[ int ], target: list[ int ] ):
    c = terrain.grid[ origin[ 0 ] ][ origin[ 1 ] ]
    terrain.grid[ target[ 0 ] ][ target[ 1 ] ] = c
    terrain.grid[ origin[ 0 ] ][ origin[ 1 ] ] = '.'

    if c == '@':
        terrain.player = target


def try_move( terrain: Terrain, move, origin=None ):
    move_dir = get_direction( move )

    if origin is None:
        origin = terrain.player

    target = [ origin[ 0 ] + move_dir[ 0 ], origin[ 1 ] + move_dir[ 1 ] ]
    target_char = terrain.grid[ target[ 0 ] ][ target[ 1 ] ]

    if target_char == '.':
        do_move( terrain, origin, target )
        return True

    if target_char == '#':
        return False

    if target_char == 'O':
        if try_move( terrain, move, target ):
            do_move( terrain, origin, target )
            return True

    return False


def sum_box_pos( grid ):
    lines, cols = get_grid_size( grid )
    sum = 0

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            if grid[ line ][ col ] == 'O' or grid[ line ][ col ] == '[':
                sum += line * 100 + col

    return sum


def step1( path: str ):
    terrain, moves = parse_input( path )

    for move in moves:
        try_move( terrain, move )

    print( f'Result: {sum_box_pos( terrain.grid )}\n' )


def upscale_terrain( terrain ):
    scaled = [ ]

    lines, cols = get_grid_size( terrain.grid )

    for line in range( 0, lines ):
        scaled.append( [ ] )
        for col in range( 0, cols ):
            base = terrain.grid[ line ][ col ]
            if base == 'O':
                scaled[ line ] += [ '[', ']' ]
            elif base == '#':
                scaled[ line ] += [ '#', '#' ]
            else:
                scaled[ line ] += [ base, '.' ]

    terrain.grid = scaled
    terrain.player = [ terrain.player[ 0 ], terrain.player[ 1 ] * 2 ]
    return terrain


def can_move( terrain: Terrain, move_dir, origin=None ):
    if origin is None:
        origin = terrain.player

    target = [ origin[ 0 ] + move_dir[ 0 ], origin[ 1 ] + move_dir[ 1 ] ]
    target_char = terrain.grid[ target[ 0 ] ][ target[ 1 ] ]

    if target_char == '.':
        return True

    if target_char == '#':
        return False

    if target_char == 'O':
        return can_move( terrain, move_dir, target )
    elif target_char == '[' or target_char == ']':
        offset = 1 if target_char == '[' else -1
        neighbor = [ target[ 0 ], target[ 1 ] + offset ]

        return can_move( terrain, move_dir, target ) and (neighbor == origin or can_move( terrain, move_dir, neighbor ))

    return False


def try_move_v2( terrain: Terrain, move, origin=None ):
    move_dir = get_direction( move )

    if origin is None:
        origin = terrain.player

    target = [ origin[ 0 ] + move_dir[ 0 ], origin[ 1 ] + move_dir[ 1 ] ]
    target_char = terrain.grid[ target[ 0 ] ][ target[ 1 ] ]

    if target_char == '.':
        do_move( terrain, origin, target )
        return True

    if target_char == '#':
        return False

    if target_char == 'O':
        if try_move_v2( terrain, move, target ):
            do_move( terrain, origin, target )
            return True
    elif target_char == '[' or target_char == ']':
        offset = 1 if target_char == '[' else -1
        neighbor = [ target[ 0 ], target[ 1 ] + offset ]

        if can_move( terrain, move_dir, origin ):
            try_move_v2( terrain, move, neighbor )
            try_move_v2( terrain, move, target )
            do_move( terrain, origin, target )
            return True

    return False


def step2( path: str ):
    terrain, moves = parse_input( path )

    upscale_terrain( terrain )

    for move in moves:
        try_move_v2( terrain, move )

    print( f'Result: {sum_box_pos( terrain.grid )}\n' )


step1( "input.txt" )
step2( "input.txt" )
