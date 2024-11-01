# edge-packet-allocator

## Simple version, without CPLEX, and more cost-efficient
This version is based on this heuristic scheme:
- get every cpu/memory stats from each worker node
- define each couple (cpu, memory) as an element in R²
- define limits (for exmaple, we choose 90% for cpu, and MAX_STORAGE - PACKET8_SIZE for memory)
- ... 
