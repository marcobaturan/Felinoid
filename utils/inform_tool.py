from utils.overlap_utils import overlap_sparse

def overlap_inform(*SDR_array, w):
    """Overlap inform
        Receive an undetermined number os lists.
        And compare in order by pairs of list
        starting by the first until end the list of arrays.
        The final step compares the extremes the list of arrays.
    """
    for index in range(len(SDR_array) - 1):
        first = SDR_array[index]
        second = SDR_array[index +1]
        percentage = overlap_sparse(array1=first,array2=second,w=w)
        print (f"The percentage between {index} and {index + 1} SDRs is {percentage}%.")

    percentage = overlap_sparse(array1=SDR_array[0], array2=SDR_array[-1], w=w)
    print(f"The percentage between first and last SDR is {percentage}%.")




