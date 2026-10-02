__doc__="""Here is the inform tools to analyze and control the performance of pattern learning and thinking of 
the organism. 
Tools:
- overlap_inform
- printStateTM
TODO:
Eventually we will separate the responsibilities of every type of tools respect the function in order to avoid
overloaded modules.
"""
from utils.overlap_utils import overlap_sparse

def overlap_inform(*SDR_array, w):
    """Overlap inform
        Receive an undetermined number os lists.
        And compare in order by pairs of list
        starting by the first until end the list of arrays.
        The final step compares the extremes the list of arrays.
    """
    total_percentage = 0
    for index in range(len(SDR_array) - 1):
        first = SDR_array[index]
        second = SDR_array[index +1]
        percentage = overlap_sparse(array1=first,array2=second,w=w)
        print (f"The percentage between {index} and {index + 1} SDRs is {percentage}%.")
        total_percentage += percentage
    average_overlap = total_percentage/len(SDR_array)
    percentage = overlap_sparse(array1=SDR_array[0], array2=SDR_array[-1], w=w)
    print(f"The percentage between first and last SDR is {percentage}%.")
    print(f"The average percentage overlap between patterns is {average_overlap} %.")

def printStateTM( tm ):
    # Useful for tracing internal states
    print("Active cells     " + formatBits(tm.getActiveCells()))
    print("Winner cells     " + formatBits(tm.getWinnerCells()))
    tm.activateDendrites(True)
    print("Predictive cells " + formatBits(tm.getPredictiveCells()))
    print("Anomaly", tm.anomaly * 100, "%")
    print("")

def formatBits(sdr):
          """
            Structure of output sdr dense bit rate for human reading.
          """
          s = ''
          for c in range(sdr.size):
            if c > 0 and c % 10 == 0:
              s += ' '
            s += str(sdr.dense.flatten()[c])
          s += ' '
          return s
