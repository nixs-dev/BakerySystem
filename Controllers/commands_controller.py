from Controllers import product_controller

'''
Each key represents a operation. Its value is a list and the indexes represents the following information: 

	0 -> method responsible to execute the operation.
	1 -> amount of indexes that the method needs
	
'''
operations = {
}

def execute(command):
	args = command.split(" ")
	operation = args.pop(0)
	
	if operation not in operations.keys():
		return "Command not found!"
	
	if operations[operation][1] != len(args):
		return "Wrong number of arguments"
	
	if operations[operation][0](args):
		return "Success"
	else:
		return "Fail"
	