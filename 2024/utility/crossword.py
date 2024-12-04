type CrosswordGrid = list[ list[ str ] | str ]


def count_horizontal( word: str, grid: CrosswordGrid, line: int, col: int ) -> int:
    lines = len( grid )
    cols = len( grid[ line ] )

    if line < 0 or line >= lines or col < 0 or col >= cols:
        return 0

    found_matches = 2

    for i in range( 0, len( word ) ):
        if col + i >= cols or word[ i ] != grid[ line ][ col + i ]:
            found_matches -= 1
            break

    for i in range( 0, len( word ) ):
        if col - i < 0 or word[ i ] != grid[ line ][ col - i ]:
            found_matches -= 1
            break

    return found_matches


def count_vertical( word: str, grid: CrosswordGrid, line: int, col: int ) -> int:
    lines = len( grid )
    cols = len( grid[ 0 ] )

    if line < 0 or line >= lines or col < 0 or col >= cols:
        return 0

    found_matches = 2

    for i in range( 0, len( word ) ):
        if line + i >= lines or word[ i ] != grid[ line + i ][ col ]:
            found_matches -= 1
            break

    for i in range( 0, len( word ) ):
        if line - i < 0 or word[ i ] != grid[ line - i ][ col ]:
            found_matches -= 1
            break

    return found_matches


def count_diagonal( word: str, grid: CrosswordGrid, line: int, col: int, min_line: int = 0, max_line: int = -1, min_col: int = 0,
                    max_col: int = -1 ) -> int:
    min_line = max( min_line, 0 )
    max_line = min( max_line, len( grid ) - 1 ) if max_line >= 0 else len( grid ) - 1

    min_col = max( min_col, 0 )
    max_col = min( max_col, len( grid[ 0 ] ) - 1 ) if max_col >= 0 else len( grid[ 0 ] ) - 1

    assert (max_line >= min_line)
    assert (max_col >= min_col)

    if line < min_line or line > max_line or col < min_col or col > max_col:
        return 0

    found_matches = 4

    for i in range( 0, len( word ) ):
        if line + i > max_line or col + i > max_col or word[ i ] != grid[ line + i ][ col + i ]:
            found_matches -= 1
            break

    for i in range( 0, len( word ) ):
        if line + i > max_line or col - i < min_col or word[ i ] != grid[ line + i ][ col - i ]:
            found_matches -= 1
            break

    for i in range( 0, len( word ) ):
        if line - i < min_line or col - i < min_col or word[ i ] != grid[ line - i ][ col - i ]:
            found_matches -= 1
            break

    for i in range( 0, len( word ) ):
        if line - i < min_line or col + i > max_col or word[ i ] != grid[ line - i ][ col + i ]:
            found_matches -= 1
            break

    return found_matches


def check_cross( word: str, grid: CrosswordGrid, line: int, col: int ) -> bool:
    step = len( word ) - 1

    min_line = line
    max_line = line + step

    min_col = col
    max_col = col + step

    block_matches = 0

    if count_diagonal( word, grid, line, col, min_line, max_line, min_col, max_col ) > 0:
        block_matches += 1

    if count_diagonal( word, grid, line, col + step, min_line, max_line, min_col, max_col ) > 0:
        block_matches += 1

    if block_matches < 2 and count_diagonal( word, grid, line + step, col + step, min_line, max_line, min_col, max_col ) > 0:
        block_matches += 1

    if block_matches < 2 and count_diagonal( word, grid, line + step, col, min_line, max_line, min_col, max_col ) > 0:
        block_matches += 1

    return block_matches > 1


def count_matches( word: str, grid: CrosswordGrid ) -> int:
    lines = len( grid )
    cols = len( grid[ 0 ] )

    match_count = 0

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            match_count += count_horizontal( word, grid, line, col )

            match_count += count_vertical( word, grid, line, col )

            match_count += count_diagonal( word, grid, line, col )

    return match_count


def count_matches_cross( word: str, grid: CrosswordGrid ) -> int:
    lines = len( grid )
    cols = len( grid[ 0 ] )

    match_count = 0

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            if check_cross( word, grid, line, col ):
                match_count += 1

    return match_count
