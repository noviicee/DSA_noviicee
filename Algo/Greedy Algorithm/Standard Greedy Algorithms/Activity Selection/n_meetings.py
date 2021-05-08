"""
Description:

There is one meeting room in a firm.
There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room
Assume only one meeting can be held in the meeting room at a particular time.
Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
"""


def maximumMeetings(n, start, end):
    """
    Function to find the maximum number of meetings that can
    be performed in a meeting room.
    """
    c = 1  # first activity is always selected?

    i = 0
    # print(i)

    arr = []
    for k in range(n):
        arr.append([start[k], end[k]])

    Activity = arr

    Activity.sort(key=lambda x: x[1])
    """
	Sort jobs according to finish time."""

    # return list(Activity)

    """
	the main logic"""
    i = 0
    for j in range(1, n):
        if Activity[j][0] > Activity[i][1]:
            c += 1
            i = j
    print("Maximum no of meetings:", end=' ')
    return(c)


"""
Test-Cases"""
print(maximumMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
print(maximumMeetings(8, [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924], [
      112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))


"""
Driver Code"""
if __name__ == "__main__":
    n = int(input("Enter the size of the arrays: "))
    print("Enter the elements for the first array:")
    start = [int(ele) for ele in input().split()]
    print("Enter the elements for the second array:")
    end = [int(ele) for ele in input().split()]

    """
	provide space-separated inputs"""

    print(maximumMeetings(n, start, end))
