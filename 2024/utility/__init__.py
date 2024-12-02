def read_columns( path: str, count: int, separator: str ):
    columns = [ ]

    for i in range( 0, count ):
        columns.append( [ ] )

    with open( path, 'r' ) as file:
        for line in file:
            if len( line ) == 0:
                return

            tokens = line.split( separator, count - 1 )

            for i in range( 0, count ):
                columns[ i ].append( int( tokens[ i ] ) )

    return columns