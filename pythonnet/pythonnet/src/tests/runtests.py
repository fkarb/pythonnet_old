"""Run all of the unit tests for this package."""

import time

test_modules = (
        'test_exceptions',
        'test_module',
        'test_conversion',
        'test_class',
        'test_interface',
        'test_enum',
        'test_field',
        'test_property',
        'test_indexer',
        'test_event',
        'test_method',
        'test_delegate',
        'test_array',
        'test_thread',
)


def main():

    start = time.clock()
    
    for name in test_modules:
        module = __import__(name)
        module.main()

    stop = time.clock()
    took = str(stop - start)
    print 'Total Time: %s' % took

if __name__ == '__main__':
    main()


