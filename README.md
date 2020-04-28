# Super-Sorting-Algorithm

The super sort sorting algorithm proposed here is
based on the principle of selecting the sequence of already
sorted elements in a given unsorted list. These natural
sequences are then removed from the original list to form a
sublist. The original list is then traced backwards and the same
selection is performed. At the end of the forward and backward
passes, two sorted lists are obtained, which are merged to form
one intermediate list. The algorithm then partitions the original
unsorted list (containing the remaining elements after the
removal of the two sublists) from the middle, and recursively
applies the same sort on each left and right sublist. Each of
these recursive calls will then return two more lists, which will
be merged to form the second intermediate list. Finally, these
two lists will be merged again and will be returned as each
recursive call returns till we get one final sorted list. 
