from functools import cmp_to_key
from typing import TextIO

type Rules = list[ list[ str ] ]


def read_rules( file: TextIO ) -> Rules:
    rules = [ ]

    for line in file:
        if line.find( '|' ) == -1:
            break

        rules.append( line.strip().split( '|' ) )

    return rules


def check_entries( entries: list[ str ], rules: Rules ) -> bool:
    is_valid = True

    for rule in rules:
        first_index = entries.index( rule[ 0 ] ) if rule[ 0 ] in entries else -1
        sec_index = entries.index( rule[ 1 ] ) if rule[ 1 ] in entries else -1

        if first_index != -1 and sec_index != -1 and first_index > sec_index:
            is_valid = False
            break

    return is_valid


def step1( path: str ):
    with open( path, "r" ) as file:
        rules = read_rules( file )
        valid_entries = [ ]
        middle_sum = 0

        for line in file:
            if line.find( ',' ) == -1:
                continue

            entries = line.strip().split( ',' )

            if check_entries( entries, rules ):
                valid_entries.append( entries )
                middle_sum += int( entries[ len( entries ) // 2 ] )

        print( f'Sum: {middle_sum} | Valid entries: {valid_entries}' )


def step2( path: str ):
    with open( path, "r" ) as file:
        rules = read_rules( file )
        filtered_entries = [ ]
        middle_sum = 0

        def compare( left, right ):
            if left == right:
                return 0

            rule = [ left, right ] if [ left, right ] in rules else [ right, left ]
            rule_index = rules.index( rule ) if rule in rules else -1

            if rule_index == -1:
                return int( left ) - int( right )

            return -1 if rules[ rule_index ][ 0 ] == left else 1

        for line in file:
            if line.find( ',' ) == -1:
                continue

            entries = line.strip().split( ',' )

            if check_entries(entries, rules):
                continue

            entries.sort( key = cmp_to_key( compare ) )
            filtered_entries.append( entries )
            middle_sum += int( entries[ len( entries ) // 2 ] )

        print( f'Sum: {middle_sum} | Valid entries: {filtered_entries}' )


step1( "input.txt" )
step2( "input.txt" )
