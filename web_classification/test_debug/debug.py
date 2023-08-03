import os

os.chdir(addtion_incude_temp)
sys.path.append(os.getcwd())
exec_code = (
    connection_imports
    + f"""
from script import {debugging_tool.function}
{debugging_tool.function}(**{node_inputs_dict})
"""
)

exec(exec_code)