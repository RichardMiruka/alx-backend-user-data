#!/usr/bin/env python3

import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
