"""ex_5_1.py"""
try:
    import argparse
    from src.ex_5_0 import line_count
except ImportError:
    import argparse
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    argument_parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    argument_parser.add_argument('infile',help='input the file name',nargs='?')
    args = argument_parser.parse_args()
    if args.infile:
        main(args.infile)
