def read_columns( path: str, count: int, separator: str ) -> list[ list[ int | None ] ]:
    columns = [ ]

    for i in range( 0, count ):
        columns.append( [ ] )

    with open( path, 'r' ) as file:
        for line in file:
            if len( line ) == 0:
                continue

            tokens = line.split( separator, count - 1 )

            for i in range( 0, count ):
                columns[ i ].append( int( tokens[ i ] ) )

    return columns


def read_grid( path: str ) -> list[ str ]:
    grid = [ ]
    cols = None

    with open( path, "r" ) as file:
        for line in file:
            line = line.removesuffix( "\n" )

            if len( line ) == 0:
                continue

            assert (cols is None or len( line ) == cols)
            cols = len( line )

            grid.append( line )

    return grid


def read_writable_grid( path: str ) -> list[ list[ str ] ]:
    grid = [ ]
    cols = None

    with open( path, "r" ) as file:
        for line in file:
            line = line.removesuffix( "\n" )

            if len( line ) == 0:
                continue

            assert (cols is None or len( line ) == cols)
            cols = len( line )

            grid.append( [ ] )

            for char in line:
                grid[ len( grid ) - 1 ].append( char )

    return grid


def read_bits( val, offset, count ):
    mask = (1 << count) - 1
    return (val >> offset) & mask
