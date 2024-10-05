# edge-packet-allocator

## What is this?
This is a simple packet allocator that I developed for a FOG-Computing project.
The main node (which has this code snippet) receives packets from a video, which has to be stored in the FOG.
Hence, the main node has to choose which packet goes to which FOG node.
To do this, it gets CPU load and available storage from each FOG node and allocates packets by following this rule:
minimize the CPU load of each node subject to the constraint that the storage of each node is not exceeded.

In mathematical terms we have:

$min \sum_{i,j \in \Omega} x_{i,j} * c_j$

subject to:

$\sum_{j=1}^{n} x_{i,j} = 1$ for each $i \in \{1,2,...,m\}$

$\sum_{i=1}^{m} x_{i,j} * s_p \leq s_j$ for each $j \in \{1,2,...,n\}$

$x_{i,j} \in \{0,1\}$

where:
- $x_{i,j}$ is the decision variable that indicates if the packet $i$ goes to the node $j$
- $c_j$ is the CPU load of the node $j$
- s_p is the size of a packet
- $s_j$ is the storage of the node $j$
- $n$ is the number of nodes
- $m$ is the number of packets

## Usage
`git clone https://github.com/B3LIOTT/edge-packet-allocator.git`

`pip install -r requirements.txt`

`cd edge-packet-allocator`

`python .`
