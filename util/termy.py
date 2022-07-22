def solve(puzzle:str, compare:str):
    LENGTH = len(puzzle)
    status = [0] * LENGTH
    
    # Check for correct guesses
    for index in range(LENGTH):
        if puzzle[index] == compare[index]:
            status[index] = 2
    
    # Check for present guesses
    for index in range(LENGTH):
        if status[index] == 2:
            continue

        matches = []
        for j in range(LENGTH):
            if compare[index] == compare[j]:
                matches.append(j) # Get all character indeces in the same guess
    
        present_matches = 0
        correct_matches = 0
        for j in range(len(matches)):
            i = matches[j]
            if status[i] == 2:
                correct_matches += 1
            if status[i] == 1:
                present_matches += 1
        
        char_count = 0
        for j in range(LENGTH):
            if compare[i] == puzzle[j]:
                char_count += 1

        if correct_matches + present_matches < char_count:
            status[i] = 1
        
    return status

key_dict = {
    "a" : "A",
    "b" : "B",
    "c" : "C",
    "d" : "D",
    "e" : "E",
    "f" : "F",
    "g" : "G",
    "h" : "H",
    "i" : "I",
    "j" : "J",
    "k" : "K",
    "l" : "L",
    "m" : "M",
    "n" : "N",
    "o" : "O",
    "p" : "P",
    "q" : "Q",
    "r" : "R",
    "s" : "S",
    "t" : "T",
    "u" : "U",
    "v" : "V",
    "w" : "W",
    "x" : "X",
    "y" : "Y",
    "z" : "Z",
    "ee": "ENTER",
    "dd": "DELETE"
}

key_coords = {
    "ee": (0, 0),
    "z" : (0, 3),
    "x" : (0, 5),
    "c" : (0, 7),
    "v" : (0, 9),
    "b" : (0,11),
    "n" : (0,13),
    "m" : (0,15),
    "dd": (0,17),
    "a" : (1, 1),
    "s" : (1, 3),
    "d" : (1, 5),
    "f" : (1, 7),
    "g" : (1, 9),
    "h" : (1,11),
    "j" : (1,13),
    "k" : (1,15),
    "l" : (1,17),
    "q" : (2, 0),
    "w" : (2, 2),
    "e" : (2, 4),
    "r" : (2, 6),
    "t" : (2, 8),
    "y" : (2,10),
    "u" : (2,12),
    "i" : (2,14),
    "o" : (2,16),
    "p" : (2,18),
}