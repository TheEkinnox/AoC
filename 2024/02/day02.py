def check_safety( dif: int, prev_dif: int ) -> bool:
    if abs( dif ) < 1 or abs( dif ) > 3:
        return False

    if prev_dif is not None and (dif > 0) != (prev_dif > 0):
        return False

    return True


def step1( path: str ):
    safe_count = 0
    with open( path, "r" ) as file:
        for line in file:
            if len( line ) == 0:
                return

            tokens = line.split( ' ' )
            prev_val = int( tokens[ 0 ] )
            prev_dif = None
            is_safe = True

            for i in range( 1, len( tokens ) ):
                cur_val = int( tokens[ i ] )
                dif = cur_val - prev_val
                prev_val = cur_val

                if not check_safety( dif, prev_dif ):
                    is_safe = False
                    break

                prev_dif = dif

            if is_safe:
                safe_count += 1

    print( "Safe count: " + str( safe_count ) )


def check_line( tokens, skip_index: int ):
    start_index = 1 if skip_index == 0 else 0
    prev_val = int( tokens[ start_index ] )
    prev_dif = None
    is_safe = True

    for i in range( start_index + 1, len( tokens ) ):
        if i == skip_index:
            continue

        cur_val = int( tokens[ i ] )
        dif = cur_val - prev_val
        prev_val = cur_val

        if not check_safety( dif, prev_dif ):
            is_safe = False
            break

        prev_dif = dif

    return is_safe


def step2( path: str ):
    safe_count = 0

    with open( path, "r" ) as file:
        for line in file:
            if len( line ) == 0:
                return

            tokens = line.split( ' ' )

            for i in range(-1, len(tokens)):
                if check_line(tokens, i):
                    safe_count += 1
                    break

    print( "Safe count: " + str( safe_count ) )


step1( "input.txt" )
step2( "input.txt" )
