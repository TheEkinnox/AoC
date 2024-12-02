from utility import read_columns


def step1( columns ):
    for col in columns:
        col.sort()

    dist_sum = 0
    for i in range( 0, len( columns[ 0 ] ) ):
        dist_sum += abs( columns[ 0 ][ i ] - columns[ 1 ][ i ] )

    print( "Sum: " + str( dist_sum ) )


def step2( columns ):
    sim_sum = 0

    for val in columns[ 0 ]:
        sim_sum += val * columns[ 1 ].count( val )

    print( "Similarity: " + str( sim_sum ) )


cols = read_columns( "input.txt", 2, ' ' )

step1( cols )
step2( cols )
