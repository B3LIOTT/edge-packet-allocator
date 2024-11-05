# edge-packet-allocator

## Simple version, without CPLEX, and more cost-efficient
This version is based on this heuristic scheme:
- get every cpu/memory stats from each worker node
- normalize cpu and memory (in [0, 1])
- define each couple (cpu, memory) as an element in R²
- define limits (for exmaple, we choose 90% for cpu, and (MAX_STORAGE - PACKET8_SIZE)% for memory)
- for each element under the limits, calculate a pseudo-distance which is an euclidian distance with a higher degree for cpu load, thus we add a non linearity for the cpu component
  If a add a packet on a worker node, storage will decrease in packet size. However cpu load will not increase linearly because if it is a very asked packet,
  it will increase explonentially.

This heuristic can be improved: the pseudo-distance must be chosen with justification, and not intuitively as we have done.
