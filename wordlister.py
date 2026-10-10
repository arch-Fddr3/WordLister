#!/usr/bin/env python3

import json
import argparse
import os
import sys
import time
from itertools import product

update_time = 1.0
eta = 0
eta_config = True


class SpacedHelpFormatter( argparse.HelpFormatter ):
    def _format_action( self, action ):
        text = super()._format_action( action )
        return text + "\n\n"

def banner():
    print( r'''
                                          ,,                ,,                                 
`7MMF'     A     `7MF'                  `7MM  `7MMF'        db            mm                   
  `MA     ,MA     ,V                      MM    MM                        MM                   
   VM:   ,VVM:   ,V ,pW"Wq.`7Mb,od8  ,M""bMM    MM        `7MM  ,pP"Ybd mmMMmm .gP"Ya `7Mb,od8 
    MM.  M' MM.  M'6W'   `Wb MM' "',AP    MM    MM          MM  8I   `"   MM  ,M'   Yb  MM' "' 
    `MM A'  `MM A' 8M     M8 MM    8MI    MM    MM      ,   MM  `YMMMa.   MM  8M""""""  MM     
     :MM;    :MM;  YA.   ,A9 MM    `Mb    MM    MM     ,M   MM  L.   I8   MM  YM.    ,  MM     
      VF      VF    `Ybmd9'.JMML.   `Wbmd"MML..JMMmmmmMMM .JMML.M9mmmP'   `Mbmo`Mbmmd'.JMML. 
    
    
    
    
    
    
    Created by: arch-Fddr3                             Copyright © 2026 until the end of times
    
    
    
    
    v2.0.0
    
    
    
    ''' )

def config_loader():
    global eta_config
    global update_time
    default_data = {
                "eta_config": True,
                "update_time": 1.0 
    }
    
    if os.path.exists( "config.json" ):
        with open( "config.json", "r", encoding = "utf-8" ) as c:
            config = json.load( c )
            eta_config = config[ "eta_config" ]
            update_time = config[ "update_time" ]
    else:
        with open( "config.json", "x", encoding = "utf-8" ) as c:
            json.dump( default_data, c, indent = 4 )


def config_save():
    global eta_config
    
    with open( "config.json", "r", encoding = "utf-8" ) as s:
        config = json.load( s )
    
    config[ "eta_config" ] = eta_config
    config[ "update_time" ] = update_time
    
    with open( "config.json", "w", encoding = "utf-8" ) as s:
        json.dump( config, s, indent = 4 )
    


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
    
if __name__ == "__main__":
    parser=argparse.ArgumentParser(
        prog = "WordLister",
        description = "A program to create any wordlist from a range of letter to .txt",
        epilog = r"""Example: python3 wordlister.py -i "Lucas 1990 ! @ #" -n 10000 -o Lucas.txt -v -m""",
        formatter_class = SpacedHelpFormatter
    ) 
    parser.add_argument(
        "-i", "--input", type = str, required = True, 
        default = None, help = "text, words or letter to create the wordlist from"
    )
    parser.add_argument(
        "-n", "--number", type = int,
        default = 10000, help = "maximum number of words generated [default 10000]" 
    )
    parser.add_argument(
        "-o", "--output", type = str,
        default = "wordlister.txt", help = "name of the output file"
    )
    parser.add_argument(
        "-v", "--verbose", action = "store_true",
        default = False, help = "display the words as they get generated [WARNING: causes significant performance decrease]"
    )
    case_group = parser.add_mutually_exclusive_group( required = True )
    case_group.add_argument(
        "-u", "--uppercase", action = "store_true",
        default = False, help = "generate the words in all uppercase"
    )
    case_group.add_argument(
        "-l", "--lowercase", action = "store_true",
        default = False, help = "generate the words in all lowercase"
    )
    case_group.add_argument(
        "-m", "--mixed", action = "store_true",
        default = False, help = "generate the words in mixed uppercase and lowercase"
    )
    extra_options_group = parser.add_argument_group( "extra options" )
    eta_group = extra_options_group.add_mutually_exclusive_group()
    eta_group.add_argument(
        "--eta", action = "store_true",
        default = True, help = "enable ETA progress visualization"
    )
    eta_group.add_argument(
        "--no-eta", action = "store_false",
        default = True, help = "disable ETA progress visualization"
    )
    extra_options_group.add_argument(
        "--eta-update", type = float,
        default = 1.0, help = "select how much time pass between ETA updates"
    )
    extra_options_group.add_argument(
        "--save-config", action = "store_true",
        default = False, help = "save as active configuration"
    )
    if len( sys.argv ) == 1:
        banner()
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    
    banner()
    
    config_loader()
    
    if "--eta" in sys.argv:
        eta_config = True
    elif "--no-eta" in sys.argv:
        eta_config = False
        
    if eta_config and "--eta-update" in sys.argv:
        if args.eta_update != update_time:
            update_time = args.eta_update
    
    if args.save_config:
        config_save()
   
    words = words_loader( args.input )
    words_count = 0
    start_time = time.time()
    last_update_time = start_time
    start_clock = time.localtime()
    current_time = start_time
    
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
                elif not args.verbose and eta_config:
                    current_time = time.time()
                    if current_time - last_update_time >= update_time:
                        speed = words_count / ( current_time - start_time )
                        eta = ( args.number - words_count ) / speed
                        last_update_time = current_time
                        print( f"\rWords: {words_count}/{args.number} | ETA: {int(eta)}s  ", end="", flush=True )
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
                    elif not args.verbose and eta_config:
                        current_time = time.time()
                        if current_time - last_update_time >= update_time:
                            speed = words_count / ( current_time - start_time )
                            eta = ( args.number - words_count ) / speed
                            last_update_time = current_time
                            print( f"\rWords: {words_count}/{args.number} | ETA: {int(eta)}s  ", end="", flush=True )
            if words_count >= args.number:
                print( f"\rWords: { words_count }/{ args.number } | ETA: { int( eta )}s  ", end = "", flush = True )
                break
    end_time = time.time()
    elapsed = end_time - start_time
      
if words_count >= args.number:
    print()
    print( f"\nFinished generating, generated { args.number } words in { int( elapsed//3600 )}h { int(( elapsed%3600)//60 )}m { int( elapsed%60 )}s" )
