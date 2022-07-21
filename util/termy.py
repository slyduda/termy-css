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