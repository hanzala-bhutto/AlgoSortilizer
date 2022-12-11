infoAlgo = {
    "Insertion Sort": {
        "Algorithm" : "Insertion Sort",
        "Time Complexity": "O(N^2)",
        "Space Complexity": "O(1)",
        "Stable": "Yes"
    },
    "Bubble Sort": {
        "Algorithm" : "Bubble Sort",
        "Time Complexity": "O(N^2)",
        "Space Complexity": "O(1)",
        "Stable": "Yes"
    },
    "Merge Sort": {
        "Algorithm" : "Merge Sort",
        "Time Complexity": "O(NlogN)",
        "Space Complexity": "O(N)",
        "Stable": "Yes"
    },
    "Heap Sort": {
        "Algorithm" : "Heap Sort",
        "Time Complexity": "O(NlogN)",
        "Space Complexity": "O(N)",
        "Stable": "No"
    },
    "Quick Sort": {
        "Algorithm" : "Quick Sort",
        "Time Complexity": "O(N^2)",
        "Space Complexity": "O(N)",
        "Stable": "No"
    },
    "Radix Sort": {
        "Algorithm" : "Radix Sort",
        "Time Complexity": "O(nd)",
        "Space Complexity": "O(n+d)",
        "Stable": "Yes"
    },
    "Bucket Sort": {
        "Algorithm" : "Bucket Sort",
        "Time Complexity": "O(n + k)",
        "Space Complexity": "O(N)",
        "Stable": "Yes"
    },
    "Count Sort": {
        "Algorithm" : "Count Sort",
        "Time Complexity": "O(n+k)",
        "Space Complexity": "O(k)",
        "Stable": "Yes"
    },
    "Quinsert Sort": {
        "Algorithm" : "Quinsert Sort",
        "Time Complexity": "O(N^2)",
        "Space Complexity": "O(N)",
        "Stable": "No"
    },
    "Range Query": {
        "Algorithm" : "Range Query",
        "Time Complexity": "O(N+K)",
        "Space Complexity": "O(N)",
        "Stable": "-"
    },
}

def infoAlgoMsg(sortingAlgoName):
    
    keys = list(infoAlgo[sortingAlgoName].keys())
    
    algoQ = keys[0]
    algoA = infoAlgo[sortingAlgoName]["Algorithm"]
    timeQ = keys[1]
    timeA = infoAlgo[sortingAlgoName]["Time Complexity"]
    spaceQ = keys[2]
    spaceA = infoAlgo[sortingAlgoName]["Space Complexity"]
    stableQ = keys[3]
    stableA = infoAlgo[sortingAlgoName]["Stable"]
    
    return f"{algoQ} : {algoA}\n{timeQ} : {timeA}\n{spaceQ} : {spaceA}\n{stableQ} : {stableA}"
