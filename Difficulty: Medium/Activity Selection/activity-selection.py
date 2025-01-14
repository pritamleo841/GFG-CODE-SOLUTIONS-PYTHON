class Solution:
    def activitySelection(self, start, end):
        #code here.
        # Pair start and end days into an Activity array
        activities = [[s, e] for s, e in zip(start, end)]
        
        # Sort activities based on their end days
        activities.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 1  # The first activity is always selected
        last_end = activities[0][1]  # Track the end day of the last selected activity
        
        # Iterate through remaining activities
        for i in range(1, len(activities)):
            # If the current activity starts after or when the last one ends
            if activities[i][0] > last_end:
                count += 1
                last_end = activities[i][1]  # Update the end day of the last selected activity
        
        return count


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the end times
        end = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, end))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends