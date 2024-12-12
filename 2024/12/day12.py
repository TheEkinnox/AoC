from bisect import insort

from utility import get_grid_size, read_grid


class Plot:
    plant: str
    pos: list
    adjacent: list
    horizontal_walls: list[ int ]
    vertical_walls: list[ int ]
    region: int

    def __init__( self, plant: str, pos: list ):
        self.plant = plant
        self.pos = pos
        self.adjacent = [ ]
        self.horizontal_walls = [ ]
        self.vertical_walls = [ ]
        self.region: int = -1


class Region:
    _index: int
    area: int
    perimeter: int
    price: int
    discount_price: int
    horizontals: dict[ int, list[ int ] ]
    verticals: dict[ int, list[ int ] ]

    def __init__( self, index ):
        self._index = index
        self.area = 0
        self.perimeter = 0
        self.price = 0
        self.horizontals = { }
        self.verticals = { }

    def add( self, plot, plots, lines, cols ):
        if plot.region >= 0:
            return

        plot.region = self._index
        self.area += 1
        self.perimeter += 4 - len( plot.adjacent )

        for neighbor_pos in plot.adjacent:
            idx = neighbor_pos[ 0 ] * cols + neighbor_pos[ 1 ]
            self.add( plots[ idx ], plots, lines, cols )

        for wall in plot.horizontal_walls:
            if wall not in self.horizontals:
                self.horizontals[ wall ] = [ plot.pos[ 1 ] ]
            else:
                insort( self.horizontals[ wall ], plot.pos[ 1 ] )

        for wall in plot.vertical_walls:
            if wall not in self.verticals:
                self.verticals[ wall ] = [ plot.pos[ 0 ] ]
            else:
                insort( self.verticals[ wall ], plot.pos[ 0 ] )

        self.price = self.perimeter * self.area

    def get_discount_price( self ):
        horizontal_count = 0

        for bucket in self.horizontals.values():
            prev_val = None

            for col in bucket:
                if prev_val is None or col != prev_val + 1:
                    horizontal_count += 1

                prev_val = col

        vertical_count = 0

        for bucket in self.verticals.values():
            prev_val = None

            for line in bucket:
                if prev_val is None or line != prev_val + 1:
                    vertical_count += 1

                prev_val = line

        return self.area * (horizontal_count + vertical_count)


def get_plots( grid ):
    lines, cols = get_grid_size( grid )

    plots = [ ]

    for line in range( 0, lines ):
        for col in range( 0, cols ):
            cur_type = grid[ line ][ col ]

            plot = Plot( cur_type, [ line, col ] )

            if line > 0 and grid[ line - 1 ][ col ] == cur_type:
                plot.adjacent.append( [ line - 1, col ] )
            else:
                plot.horizontal_walls.append( -line )

            if line < lines - 1 and grid[ line + 1 ][ col ] == cur_type:
                plot.adjacent.append( [ line + 1, col ] )
            else:
                plot.horizontal_walls.append( line + 1 )

            if col > 0 and grid[ line ][ col - 1 ] == cur_type:
                plot.adjacent.append( [ line, col - 1 ] )
            else:
                plot.vertical_walls.append( -col )

            if col < cols - 1 and grid[ line ][ col + 1 ] == cur_type:
                plot.adjacent.append( [ line, col + 1 ] )
            else:
                plot.vertical_walls.append( col + 1 )

            plots.append( plot )

    return plots


def get_regions( plots: list[ Plot ], grid ):
    regions = [ ]

    lines, cols = get_grid_size( grid )

    for plot in plots:
        if plot.region >= 0:
            continue

        region = Region( len( regions ) )

        region.add( plot, plots, lines, cols )

        regions.append( region )

    return regions


def step1( path: str ):
    result = 0

    grid = read_grid( path )
    regions = get_regions( get_plots( grid ), grid )

    for region in regions:
        result += region.price

    print( f'Result: {result}\n' )


def step2( path: str ):
    result = 0

    grid = read_grid( path )
    regions = get_regions( get_plots( grid ), grid )

    for region in regions:
        result += region.get_discount_price()

    print( f'Result: {result}\n' )


step1( "input.txt" )
step2( "input.txt" )
