import re


def step1( path: str ):
    with open( path, "r" ) as file:
        source = re.findall( "mul\\(\\d{1,3},\\d{1,3}\\)", file.read() )
        result = 0

        for mul in source:
            values = re.sub( "mul\\(|\\)", '', mul ).split( ',' )
            result += int( values[ 0 ] ) * int( values[ 1 ] )

        print( "Result: " + str( result ) )


def step2( path: str ):
    with open( path, "r" ) as file:
        source = re.findall( "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)", file.read() )
        should_skip = False
        result = 0

        for entry in source:
            operation = re.sub( "\\(.*\\)", '', entry )

            if operation == "mul" and not should_skip:
                tmp = re.sub( "mul\\(|\\)", '', entry )
                values = tmp.split( ',' )
                result += int( values[ 0 ] ) * int( values[ 1 ] )
            elif operation == "do":
                should_skip = False
            elif operation == "don't":
                should_skip = True

        print( "Result: " + str( result ) )


step1( "input.txt" )
step2( "input.txt" )
