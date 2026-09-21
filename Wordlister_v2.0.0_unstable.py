#!/usr/bin/env python3

import argparse
import os
import sys
import random
import time
from itertools import product

written_words = set()
speed = 0
eta = 0

class SpacedHelpFormatter( argparse.HelpFormatter ):
    def _format_action( self, action ):
        text = super()._format_action( action )
        return text + "\n\n"

def banner():
    print( """
                                          ,,                ,,                                 
`7MMF'     A     `7MF'                  `7MM  `7MMF'        db            mm                   
  `MA     ,MA     ,V                      MM    MM                        MM                   
   VM:   ,VVM:   ,V ,pW"Wq.`7Mb,od8  ,M""bMM    MM        `7MM  ,pP"Ybd mmMMmm .gP"Ya `7Mb,od8 
    MM.  M' MM.  M'6W'   `Wb MM' "',AP    MM    MM          MM  8I   `"   MM  ,M'   Yb  MM' "' 
    `MM A'  `MM A' 8M     M8 MM    8MI    MM    MM      ,   MM  `YMMMa.   MM  8M""""""  MM     
     :MM;    :MM;  YA.   ,A9 MM    `Mb    MM    MM     ,M   MM  L.   I8   MM  YM.    ,  MM     
      VF      VF    `Ybmd9'.JMML.   `Wbmd"MML..JMMmmmmMMM .JMML.M9mmmP'   `Mbmo`Mbmmd'.JMML.   
    
    
    
    
    
    
    Created by: arch-Fddr3                                  Copyright © 2026 until the end of times
    
    
    
    
    V2.0-tester
    
    
    
    """ )
def words_loader( input_value ):
    
    if os.path.isfile( input_value ):
        with open( input_value, "r", encoding = "utf-8", errors = "ignore" ) as f:
            words = [ line.strip() for line in f if line.strip() ]
    else:
        words = input_value.split()
    
    return words
    
def generator( words ):
    length = 1
    
    while True:
        for combo in product( words, repeat=length ):
            word = "".join(combo)
            yield word
        length += 1
    
    
def random_mixed( word ):
    return ''.join( c.upper() if random.choice([True, False]) else c.lower() for c in word )


def eta_updater( words_count, total_words, start_time, last_update_time, verbose, force = True  ):
    current_time = time.time()
    if force or (current_time - last_update_time >= 0.5):
        speed = words_count / ( current_time - start_time )
        eta = ( total_words - words_count ) / speed
        status = f"Words: {words_count}/{total_words} | ETA: {int(eta)}s"
        try:
            lines = os.get_terminal_size().lines
        except OSError:
            lines = 24
        if verbose:
            sys.stderr.write(f"\033[{lines};1H\033[K{status}\033[1;1H")
            sys.stderr.flush()
        else:
            print(f"\r{status}   ", end="", flush=True)
        return current_time
    return last_update_time
    
    
    
if __name__ == "__main__":
    
    parser=argparse.ArgumentParser(
        prog = "WordLister",
        description = "A program to create any wordlist from a range of letter to .txt",
        epilog = r"""Example: python3 wordlister.py -i "Lucas 1990 ! @ #" -n 10000 -o Lucas.txt -v -m""",
        formatter_class = SpacedHelpFormatter
    ) 
    parser.add_argument(
        "-i", "--input", type = str, required = True, 
        default = None, help = "Text, words or letter to create the wordlist from"
    )
    parser.add_argument(
        "-n", "--number", type = int,
        default = 10000, help = "Maximum number of words generated [default 10000]" 
    )
    parser.add_argument(
        "-o", "--output", type = str,
        default = "wordlister.txt", help = "Name of the output file"
    )
    parser.add_argument(
        "-v", "--verbose", action = "store_true",
        default = False, help = "See the words as they get generated"
    )
    case_group = parser.add_mutually_exclusive_group( required = True )
    case_group.add_argument(
        "-u", "--uppercase", action = "store_true",
        default = False, help = "Generate the words in all uppercase"
    )
    case_group.add_argument(
        "-l", "--lowercase", action = "store_true",
        default = False, help = "Generate the words in all lowercase"
    )
    case_group.add_argument(
        "-m", "--mixed", action = "store_true",
        default = False, help = "Generate the words in mixed uppercase and lowercase"
    )
    
    if len( sys.argv ) == 1:
        banner()
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    
    banner()
    
    words = words_loader( args.input )
    
    words_count = 0
    
    start_time = time.time()
    last_update_time = start_time
    start_clock = time.localtime()
    
    if args.lowercase:
        words = list(set([w.lower() for w in words]))
    elif args.uppercase:
        words = list(set([w.upper() for w in words]))
    else:
        words = list(set(words))
    
    with open( args.output, "w" ) as f:
        for word in generator( words ):
            if args.uppercase or args.lowercase:
                f.write( word + "\n" )
                words_count += 1
                if args.verbose:
                    print( word )
                last_update_time = eta_updater( words_count, args.number, start_time, last_update_time, args.verbose )
            elif args.mixed:
                options = [(c.lower(), c.upper()) if c.isalpha() else (c,) for c in word]
                
                for w in product(*options):
                    w_u = "".join(w)
                    if words_count >= args.number:
                            break
                    f.write( w_u + "\n" )
                    words_count += 1
                    if args.verbose:
                        print( w_u )
                    last_update_time = eta_updater( words_count, args.number, start_time, last_update_time, args.verbose )
            if words_count >= args.number:
                break
    if args.verbose:
        try:
            lines = os.get_terminal_size().lines
            print(f"\033[{lines};1H\033[K\n")
        except OSError:
            print()
    else:
        print()
    end_time = time.time()
    elapsed = end_time - start_time
            
if words_count >= args.number:
    print()
    print( f"Finished generating, generated { args.number } words in { int( elapsed//3600 )}h { int(( elapsed%3600)//60 )}m { int( elapsed%60 )}s" )

#slow restore past version of print eta
#fix verbose version of print eta
