from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import Resource
from gem5.simulate.simulator import Simulator

# obtain the components
# cache_hier = NoCache()
cache_hier = PrivateL1CacheHierarchy(l1d_size="32kB", l1i_size="32kB")
memory = SingleChannelDDR3_1600("1GiB")
proc = SimpleProcessor(cpu_type=CPUTypes.ATOMIC, num_cores=1)

# add them to the board
board = SimpleBoard(
    clk_freq = "3GHz",
    processor = proc,
    memory = memory,
    cache_hierarchy = cache_hier,
)

# set the workload
binary = Resource("x86-hello64-static")
board.set_se_binary_workload(binary)

# Setup the simulator and run
simulator = Simulator(board = board)
simulator.run()