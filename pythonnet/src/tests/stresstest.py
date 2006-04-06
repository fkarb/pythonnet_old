# ===========================================================================
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
# ===========================================================================

"""Basic stress test."""

def main():


    import time
    start = time.clock()

    for i in range(2000):
        print i
        for name in (
            'test_module',
            'test_conversion',
            #'test_class',
            'test_interface',
            'test_enum',
            'test_field',
            'test_property',
            'test_indexer',
            'test_event',
            'test_method',
            #'test_delegate',
            'test_array',
            ):
            module = __import__(name)
            module.main()

    #import pdb; pdb.set_trace()

    stop = time.clock()
    took = str(stop - start)
    print 'Total Time: %s' % took

    import gc
    for i in gc.get_objects():
        print i

if __name__ == '__main__':
    main()


