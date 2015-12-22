#!/usr/bin/env python

import random, time, string, logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)

while True:
    logging.debug(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)))
    print "logged a thing"
    time.sleep(30)
