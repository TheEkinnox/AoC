from utility import get_max


def build_map( path: str ) -> list[ int ]:
    with open( path, "r" ) as file:
        data = file.read()

    output = [ ]
    file_id = 0

    for i in range( 0, len( data ) ):
        if not data[ i ].isdigit():
            continue

        if i % 2 == 1:
            for j in range( 0, int( data[ i ] ) ):
                output.append( -1 )
        else:
            for j in range( 0, int( data[ i ] ) ):
                output.append( file_id )

            file_id += 1

    return output


def get_free_spot( data: list[ int ], offset = 0, limit = -1 ):
    for i in range( offset, (limit if limit >= 0 else len( data )) ):
        if data[ i ] < 0:
            return i

    return -1


def shrink_map( data: list[ int ] ):
    output = data.copy()

    free_spot = 0

    for i in range( 0, len( data ) ):
        index = len( data ) - i - 1

        if output[ index ] < 0:
            continue

        free_spot = get_free_spot( output, free_spot, index )

        if free_spot < 0 or free_spot >= index:
            break

        output[ free_spot ] = output[ index ]
        output[ index ] = -1

    assert (not has_holes( output ))

    return output


def has_holes( data ):
    free_spot = get_free_spot( data )

    if free_spot == -1:
        return False

    for i in range( free_spot, len( data ) ):
        if data[ i ] >= 0:
            return True

    return False


def step1( path: str ):
    result = 0

    base_map = build_map( path )

    shrunk_map = shrink_map( base_map )

    for i in range( 0, len( shrunk_map ) ):
        if shrunk_map[ i ] >= 0:
            result += i * shrunk_map[ i ]

    print( f'Result: {result}\n' )


def get_free_block( data, length, offset = 0, limit = -1 ):
    for i in range( offset, (limit if limit >= 0 else len( data )) ):
        if data[ i ] < 0:
            is_valid = True

            for j in range( 0, length ):
                if data[ i + j ] >= 0:
                    is_valid = False
                    i += j - 1
                    break

            if is_valid:
                return i

    return -1


def get_file( data, file_id, limit = -1 ) -> (int, int):
    limit = limit if limit >= 0 else len( data )

    file_start = -1
    file_length = 0

    for i in range( 0, limit ):
        index = limit - i - 1
        if data[ index ] == file_id:
            while i >= 0 and data[ index ] == file_id:
                file_length += 1
                index -= 1

            file_start = index + 1
            break

    return file_start, file_length


def shrink_map_v2( data: list[ int ] ):
    output = data.copy()

    free_spot = 0
    cur_id = get_max( output )
    file_start = -1

    while cur_id >= 0:
        file_start, file_length = get_file( output, cur_id, file_start )
        cur_id -= 1

        if file_start < 0:
            continue

        target = get_free_block( output, file_length, free_spot, file_start )

        if target < 0 or target > file_start:
            continue

        for i in range( 0, file_length ):
            output[ target + i ] = output[ file_start + i ]
            output[ file_start + i ] = -1

    return output


def step2( path: str ):
    result = 0

    base_map = build_map( path )

    shrunk_map = shrink_map_v2( base_map )

    for i in range( 0, len( shrunk_map ) ):
        if shrunk_map[ i ] >= 0:
            result += i * shrunk_map[ i ]

    print( f'Result: {result}\n' )


step1( "input.txt" )
step2( "input.txt" )
