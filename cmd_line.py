import argparse

# My Command line parser
class cmd_line():

    def __init__(self):
        print("Cmd Line stuff...")
        parser = argparse.ArgumentParser(description='TIP General purpose program ...')
        parser.add_argument('-a', '--arg1', dest='arg1', help='Argument 1')
        parser.add_argument('-b', '--arg2', dest='arg2', help='Argument 2')
        parser.add_argument('-c', '--arg3', dest='arg3', help='Argument 3')
        parser.add_argument('-p', '--plc', dest='plc', help='library to attack PLCs')
        parser.add_argument('-w', '--wireless', dest='wireless', help='library to attack Wireless')

        args = parser.parse_args()
        print(args)

        # print("Arg1: ", args.arg1)
        # print("Arg2: ", args.arg2)
        # print("Arg3: ", args.arg3)

        self.arg1 = args.arg1
        self.arg2 = args.arg2
        self.arg3 = args.arg3
        self.plc = args.plc
        self.wireless = args.wireless

    def my_print(self):
        print("Arg1: ", self.arg1)
        print("Arg2: ", self.arg2)
        print("Arg3: ", self.arg3)
        print("PLC IP: ", self.plc)
