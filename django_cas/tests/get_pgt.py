from __future__ import print_function
# Run via bin/django shell --plain < get_pgt.py
# to pick up all the django environment
# Allows main test class to be independent of CAS implementation platform
# TODO: pass in iou - if cant take args write to file and read here
from __future__ import absolute_import
import atexit
from django_cas.models import PgtIOU

@atexit.register
def lookup_pgt():
    pgt = PgtIOU.objects.latest('created') 
    if pgt:
        print(pgt.tgt)
    else:
        print('FAIL')


