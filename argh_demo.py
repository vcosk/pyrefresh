# pip install argh
# conda install argh
import argh

# argh_demo.py 1 --optional-arg 3 --other-optional-arg
# required_arg = 1, optional_arg = 3, other-optional-arg is True
@argh.arg('required_arg', help='Required Information')
@argh.arg('choice_arg', choices=['one', 'two', 'three'] , help='Required Choice Information')
@argh.arg('--optional_arg', '-o', help='Optional data')
def execute_task(required_arg, choice_arg, optional_arg = 1, other_optional_arg=False):
    # This shows up when used with -h switch
    """
    This is doc string
    """
    print((required_arg, type(required_arg)))
    print((choice_arg, type(choice_arg)))
    print((optional_arg, type(optional_arg)))
    print((other_optional_arg, type(other_optional_arg)))

def execute_another_task():
    print('Another task')

if __name__ == '__main__':
    # argh.dispatch_command(execute_task)
    argh.dispatch_commands([execute_task, execute_another_task])