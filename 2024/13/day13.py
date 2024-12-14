import re


class ClawMachine:
    a: tuple[ int, int ]
    b: tuple[ int, int ]
    prize: tuple[ int, int ]


def read_machines( path: str, prize_offset: int = 0 ) -> list[ ClawMachine ]:
    machines = [ ]

    with open( path, "r" ) as file:
        lines = file.readlines()

    for i in range( 0, len( lines ), 4 ):
        machine = ClawMachine()

        a = re.search( 'X[+=](\\d+), Y[+=](\\d+)', lines[ i ] )
        b = re.search( 'X[+=](\\d+), Y[+=](\\d+)', lines[ i + 1 ] )
        prize = re.search( '[xX][+=](\\d+), [yY][+=](\\d+)', lines[ i + 2 ] )

        machine.a = [ int( a[ 1 ] ), int( a[ 2 ] ) ]
        machine.b = [ int( b[ 1 ] ), int( b[ 2 ] ) ]
        machine.prize = [ int( prize[ 1 ] ) + prize_offset, int( prize[ 2 ] ) + prize_offset ]

        machines.append( machine )

    return machines


def get_cheapest_win( machine: ClawMachine ) -> int:
    a1, a2 = machine.a
    b1, b2 = machine.b
    c1, c2 = machine.prize

    b_count = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
    a_count = (c1 - b_count * b1) / a1

    if int( a_count ) == a_count and int( b_count ) == b_count:
        return int( 3 * a_count + b_count )

    return 0


def step1( path: str ):
    result = 0

    machines = read_machines( path )

    for machine in machines:
        result += get_cheapest_win( machine )

    print( f'Result: {result}\n' )


def step2( path: str ):
    result = 0

    machines = read_machines( path, 10000000000000 )

    for machine in machines:
        result += get_cheapest_win( machine )

    print( f'Result: {result}\n' )


step1( "input.txt" )
step2( "input.txt" )
