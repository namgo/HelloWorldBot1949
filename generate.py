import random
import os
import string
NUM_LINES = 30
FILENAME_LEN = 20
# these are not the complete
# set of x86_64 registers
registers = [
    'rax',
    'rbx',
    'rcx',
    'rdx',
    'rsi',
    'rdi',
    'rbp',
    'rsp'
]

# instruction name
# number of operands
# register position
# register is optional

instructions = [
    {
        'name': 'mov',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
    },
    {
        'name': 'and',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
    },
    {
        'name': 'or',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
    },
    {
        'name': 'xor',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
        
    },
    {
        'name': 'add',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
    },
    {
        'name': 'sub',
        'num_operands': 2,
        'register_pos_opt': 1,
        'register_pos_req': 0
    },
    {
        'name': 'inc',
        'num_operands': 1,
        'register_pos_opt': None,
        'register_pos_req': 0
    },
    {
        'name': 'dec',
        'num_operands': 1,
        'register_pos_opt': None,
        'register_pos_req': 0
    },
    {
        'name': 'syscall',
        'num_operands': 0,
        'register_pos_opt': None,
        'register_pos_req': None
    }
]

# if anyone has any ideas for
# extra system calls, let me know
syscalls = [
    {
        'address': '1',
        'name': 'write',
        'num_arguments': 4,
    },
    {
        'address': '60',
        'name': 'exit',
        'num_arguments': 0,
    }
]

# choose a number between 1 (write) and 60 (exit), and add the address of our "hello world"
# choices = [1, 60, 'message', 'messagelen']
choices =  list(range(1, 61))
choices.append('message')
choices.append('messagelen')


def choose_register_positon(instruction):
    choice = [None, None]
    req = instruction['register_pos_req']
    if req is not None:
        choice[req] = True
    opt = instruction['register_pos_opt']
    if opt is not None:
        choice[opt] = bool(random.randint(0,1))
    return choice
        

def call_with_operands(instruction):
    register_position = choose_register_positon(instruction)
    parts = [instruction['name']]
    if register_position[0]:
        parts.append(random.choice(registers))
    if register_position[1]:
        parts[1] += ','
        parts.append(random.choice(registers))
    elif register_position[1] is False:
        parts[1] += ','
        parts.append(str(random.choice(choices)))
    return parts
        

def generate_line():
    return ' '.join(call_with_operands(random.choice(instructions)))


def generate_asm():
    return '''
global _start
section .text
_start: 
{}
section .data
message: db "Hello World", 10
messagelen: equ $ - message
'''.format('\n'.join([generate_line() for i in range(0, NUM_LINES)]))

    ''' 
    filename = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(FILENAME_LEN)) + '.asm'
    with open(filename, 'w') as f:
        print('writing to {}'.format(filename))
        f.write(asm)
    '''
