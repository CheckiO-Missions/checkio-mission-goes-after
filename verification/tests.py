"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['world', 'w', 'o'],
            "answer": True
        },
        {
            "input": ['world', 'w', 'r'],
            "answer": False
        },
        {
            "input": ['world', 'l', 'o'],
            "answer": False
        },
        {
            "input": ['panorama', 'a', 'n'],
            "answer": True
        },
        {
            "input": ['list', 'l', 'o'],
            "answer": False
        },
        {
            "input": ['', 'l', 'o'],
            "answer": False
        },
        {
            "input": ['list', 'l', 'l'],
            "answer": False
        },
    ],
    "Extra": [
        
        {
            "input": ['almaz', 'a', 'l'],
            "answer": True
        },
        
        {
            "input": ['almaz', 'm', 'a'],
            "answer": False
        },
        
        {
            "input": ['almaz', 'r', 'l'],
            "answer": False
        },
        
        {
            "input": ['almaz', 'p', 'p'],
            "answer": False
        },
    ]
}
