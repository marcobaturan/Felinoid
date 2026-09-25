
def overlap_sparse(array1, array2, w):
    """Overlap sparse.
        Function for calculate the percentage
        of overlap between two SDR
    """
    overlap = len(set(array1) & set(array2)) / w * 100
    return round(overlap)
