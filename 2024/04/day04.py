from utility import read_grid
from utility.crossword import *


def step1( path: str ):
    print( "Matches: " + str( count_matches( "XMAS", read_grid( path ) ) ) )


def step2( path: str ):
    print( "X-Matches: " + str( count_matches_cross( "MAS", read_grid( path ) ) ) )


step1( "input.txt" )
step2( "input.txt" )
