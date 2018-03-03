# DistributedSort

Simple environment for implementing and testing distributed sorting algorithms. It consists of master and worker nodes organized in star topology.


### Assumptions

1. Master is connected to K workers.
2. Master have space for K elements of data.
3. Each worker contains N elements and have space for 2\*N elements of data
4. Workers data is unsorted
5. There is no worker-to-worker direct communication. All goes through master.


### Classes

- Master -- master node containing other nodes
- Node -- regular node
- NMerge -- example of k-merge sort algorithm


### K-merge sort

The algorithm have following properties:
 - K sortings running in parallel
 - N\*K data transfers from worker to master
 - N\*K data transfers from master to worker
 - N\*K\*K data comparisons done in master

Because of space constrains every sort operation executed on master have to be done "in place" and every soritng done on worker requires at most space for N additional temporary elements.


### References

Online resources:
* https://en.wikipedia.org/wiki/Merge_algorithm
* https://en.wikipedia.org/wiki/External_sorting
* https://en.wikipedia.org/wiki/Sorting_algorithm
