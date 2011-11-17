import cmd
import sys

class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'RL>> '

    def do_print(self, args):
        print 'You enter', args

    def do_exit(self, args):
        print 'Bye'
        sys.exit(0)

if __name__ == '__main__':
    console = Console()
    console.cmdloop()
