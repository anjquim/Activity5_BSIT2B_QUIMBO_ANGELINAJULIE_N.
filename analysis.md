## Analysis


1. A linked-list stack pushes and pops at the head because these operations take O(1) time. If the tail were used in a singly linked list, removing the last node would require traversing the entire list, resulting in O(n) time complexity. Using the head keeps stack operations efficient and follows the LIFO principle naturally.

2. An array queue must be circular so that freed positions at the beginning of the array can be reused after dequeues. Without a circular structure, the rear index would eventually reach the end of the array even when there are empty spots available. A circular queue allows both enqueue and dequeue operations to remain O(1) while using memory efficiently.

