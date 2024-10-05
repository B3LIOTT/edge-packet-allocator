# edge-packet-allocator

## What is this?
This is a simple packet allocator that I developed for a FOG-Computing project.
The main node (which has this code snippet) receives packets from a video, which has to be stored in the FOG.
Hence, the main node has to choose which packet goes to which FOG node.
To do this, it gets CPU load and available storage from each FOG node and allocates packets by following this rule:
minimize the CPU load of each node subject to the constraint that the storage of each node is not exceeded.

In mathematical terms we have:

$min \sum_{i,j \in \omega} x_{i,j} * c_j$

subject to:

$\sum_{i=1}^{n} x_i * s_j \leq S$ for each $j \in \{1,2,...,n\}$

$x_{i,j} \in \{0,1\}$

where:
- $x_{i,j}$ is the decision variable that indicates if the packet $i$ goes to the node $j$
- $c_j$ is the CPU load of the node $j$
- $s_j$ is the storage of the node $j$
- $S$ is the storage limit
- $n$ is the number of nodes

## Usage
`git clone https://github.com/B3LIOTT/edge-packet-allocator.git`

`pip install -r requirements.txt`

`cd edge-packet-allocator`

`python .`
