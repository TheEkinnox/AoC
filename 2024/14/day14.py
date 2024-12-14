from functools import reduce
from operator import mul
from os import remove
from os.path import exists

from utility import print_grid

EX_SIZE = [ 11, 7 ]
INPUT_SIZE = [ 101, 103 ]


class Robot:
    pos: list[ int, int ]
    vel: list[ int, int ]

    def __init__( self, pos, vel ):
        self.pos = pos
        self.vel = vel


def load_robots( path: str ):
    robots = [ ]

    with open( path, "r" ) as file:
        for line in file:
            line = line.strip()
            if len( line ) == 0:
                continue

            pos = line.split( ' ' )[ 0 ][ 2: ].split( ',' )
            pos = [ int( pos[ 0 ] ), int( pos[ 1 ] ) ]

            vel = line.split( ' ' )[ 1 ][ 2: ].split( ',' )
            vel = [ int( vel[ 0 ] ), int( vel[ 1 ] ) ]

            robots.append( Robot( pos, vel ) )

    return robots


def make_grid( robots, grid_size ):
    grid = [ ]
    for i in range( 0, grid_size[ 1 ] ):
        grid.append( [ ] )
        for j in range( 0, grid_size[ 0 ] ):
            grid[ i ].append( '.' )

    for robot in robots:
        val = grid[ robot.pos[ 1 ] ][ robot.pos[ 0 ] ]
        grid[ robot.pos[ 1 ] ][ robot.pos[ 0 ] ] = '1' if val == '.' else str( int( val ) + 1 )

    return grid


def draw_robots( robots, grid_size, block_title=None, out=None ):
    grid = make_grid( robots, grid_size )

    print_grid( grid, block_title, out )


def step1( path: str, grid_size=None, time=100 ):
    if grid_size is None:
        grid_size = EX_SIZE

    bots = load_robots( path )
    draw_robots( bots, grid_size )

    quadrants = [ 0, 0, 0, 0 ]

    for i in range( 0, len( bots ) ):
        bots[ i ].pos[ 0 ] = (bots[ i ].pos[ 0 ] + bots[ i ].vel[ 0 ] * time) % grid_size[ 0 ]
        bots[ i ].pos[ 1 ] = (bots[ i ].pos[ 1 ] + bots[ i ].vel[ 1 ] * time) % grid_size[ 1 ]

        if bots[ i ].pos[ 0 ] > grid_size[ 0 ] // 2:
            if bots[ i ].pos[ 1 ] > grid_size[ 1 ] // 2:
                quadrants[ 1 ] += 1
            elif bots[ i ].pos[ 1 ] < grid_size[ 1 ] // 2:
                quadrants[ 3 ] += 1
        elif bots[ i ].pos[ 0 ] < grid_size[ 0 ] // 2:
            if bots[ i ].pos[ 1 ] > grid_size[ 1 ] // 2:
                quadrants[ 0 ] += 1
            elif bots[ i ].pos[ 1 ] < grid_size[ 1 ] // 2:
                quadrants[ 2 ] += 1

    draw_robots( bots, grid_size )
    print( quadrants )

    print( f'Result: {reduce( mul, quadrants )}\n' )


def step2( path: str, grid_size=None, start_time=0, time=30000 ):
    if grid_size is None:
        grid_size = EX_SIZE

    bots = load_robots( path )

    if exists( "num_aligned_x.txt" ):
        remove( "num_aligned_x.txt" )

    if exists( "num_aligned_y.txt" ):
        remove( "num_aligned_y.txt" )

    max_aligned = [ 6, 8 ]

    for t in range( 1, time + 1 ):
        for i in range( 0, len( bots ) ):
            bots[ i ].pos[ 0 ] = (bots[ i ].pos[ 0 ] + bots[ i ].vel[ 0 ]) % grid_size[ 0 ]
            bots[ i ].pos[ 1 ] = (bots[ i ].pos[ 1 ] + bots[ i ].vel[ 1 ]) % grid_size[ 1 ]

        if t < start_time:
            continue

        grid = make_grid( bots, grid_size )

        cur_max_aligned = [ 0, 0 ]
        cur_aligned = [ 0, 0 ]

        for y in range( 0, grid_size[ 0 ] ):
            cur_aligned[ 0 ] = 0
            for x in range( grid_size[ 0 ] ):
                if grid[ y ][ x ] != '.':
                    cur_aligned[ 0 ] += 1
                else:
                    if cur_aligned[ 0 ] > cur_max_aligned[ 0 ]:
                        cur_max_aligned[ 0 ] = cur_aligned[ 0 ]

                    cur_aligned[ 0 ] = 0

        for x in range( 0, grid_size[ 0 ] ):
            cur_aligned[ 1 ] = 0
            for y in range( grid_size[ 1 ] ):
                if grid[ y ][ x ] != '.':
                    cur_aligned[ 1 ] += 1
                else:
                    if cur_aligned[ 1 ] > cur_max_aligned[ 1 ]:
                        cur_max_aligned[ 1 ] = cur_aligned[ 1 ]

                    cur_aligned[ 1 ] = 0

        if cur_max_aligned[ 0 ] >= max_aligned[ 0 ]:
            max_aligned[ 0 ] = cur_max_aligned[ 0 ]
            print_grid( grid, f'T={t} | max_x={cur_max_aligned[ 0 ]}', "num_aligned_x.txt" )

        if cur_max_aligned[ 1 ] >= max_aligned[ 1 ]:
            max_aligned[ 1 ] = cur_max_aligned[ 1 ]
            print_grid( grid, f'T={t} | max_y={cur_max_aligned[ 1 ]}', "num_aligned_y.txt" )


step1( "input.txt", INPUT_SIZE )
step2( "input.txt", INPUT_SIZE, 1586 )
