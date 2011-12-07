import argparse

def fun_1():
    print 'This is function 1'

def fun_2():
    print 'This is function 2'

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='argparse example')
    parser.add_argument('-bool', action='store_true', default=False,
                        help='A boolean parameter, default to True')
    parser.add_argument('-data', help='Consume one parameter')
    parser.add_argument('-dint', type=int, 
                        help='Call function f_dint()')

    args = parser.parse_args()

    if args.bool:
        print 'Bool set to true.'

    print 'args.data = %s' % args.data

    if args.dint:
        fname = 'fun_%d' % args.dint
        print 'Trying to call %s()' % fname

        try:
            locals()[fname]()
        except KeyError, TypeError:
            print 'Function %s does not exist' % fname
