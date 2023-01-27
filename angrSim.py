#!/usr/bin/env python3

import angr,sys

# Define messages (states) we're looking for (or not)
success_msg = 'Access Granted'
fail_msg = 'Access Denied'

# Import the 'simple' binary that we created from our simple.c program
project = angr.Project('simple')
# Define the initial entry state of the program 
initial_state = project.factory.entry_state()
# Configure our simulation to use the entry state we obtained
simulation = project.factory.simgr(initial_state)



def is_successful(state):
    """ Determine what output a given state would yeild """
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return success_msg in stdout_output.decode('utf-8') # Return whether or not the current state has what we're looking for (success_msg)

def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return fail_msg in stdout_output.decode('utf-8') # Return whether or not the current state has fail_msg

# Start the concolic execution process - deine success/fail states (This is da Meat N' Potatoes!)
simulation.explore(find=is_successful, avoid=should_abort)

# Once the concolic execution has finished - see if we found success_msg (simulation.found)
if simulation.found:
    solution_state = simulation.found[0]
    binary_num = solution_state.posix.dumps(sys.stdin.fileno()) # b'<number>'
    # print string as integer
    decoded_num = int(binary_num.decode('utf-8')) 
    print("Found Solution: {}".format(decoded_num))
else:
    raise Exception('Could not find the password')