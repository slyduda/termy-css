import shutil
import sys
import os
import random

WORD = None
try:
    WORD = sys.argv[1]
except:
    pass

color = {
    0: 'mg',
    1: 'y',
    2: 'g'
}

def split(word):
    return [char.lower() for char in word]

ALPHABET = [
  'Q',
  'W',
  'E',
  'R',
  'T',
  'Y',
  'U',
  'I',
  'O',
  'P',
  'A',
  'S',
  'D',
  'F',
  'G',
  'H',
  'J',
  'K',
  'L',
  'Z',
  'X',
  'C',
  'V',
  'B',
  'N',
  'M'
]

# Get all words from 4 Letter Word File
text_file = open("constants/4LW.txt", "r")
data = text_file.read()
words = data.split()

# If a word wasn't supplied select a random 4 letter word
if not WORD:
    WORD = random.choice(words).lower()
puzzle = split(WORD)

# Change some stuff in the pre.html file
with open('src/selector.html', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('{{ }}', WORD)
filedata = filedata.replace('selector.css', 'index.css')

with open('dist/index.html', 'w') as file:
  file.write(filedata)
  
# use copyfile()
shutil.copyfile('src/selector.css','dist/index.css')

# Open the new style file
f = open("src/index.css", "a")


# Termy algorithms
word_characters = []

for word in words:
    c = split(word)
    if len(c) != 4:
        print("A WORD IS NOT 4 LETTERS")
        exit()
    word_characters.append(c)

char = word_characters[0]

TOO_LONG_COUNT = 0
reps = 0
for word in word_characters:
    for i in range(4):
        if TOO_LONG_COUNT > 200:
            f.truncate(f.tell() - 2)
            f.write(" { display: flex; }\n\n")
            reps += 1
            TOO_LONG_COUNT = 0

        f.write("#i%s__%s-1:checked ~ #i%s__%s-2:checked ~ #i%s__%s-3:checked ~ #i%s__%s-4:checked ~ #lee_%s-5,\n" % (word[0], i + 1, word[1], i + 1, word[2], i + 1, word[3], i + 1, i + 1 ))
        TOO_LONG_COUNT += 1

f.truncate(f.tell() - 2)
f.write(" { display: flex; }\n\n")
reps += 1
print(reps)


for word in word_characters:
    status = [0,0,0,0]
    # Check for correct guesses
    for index in range(4):
        if puzzle[index] == word[index]:
            status[index] = 2
    # Check for present guesses
    for index in range(4):
        if status[index] == 2:
            continue

        matches = []
        for j in range(4):
            if word[index] == word[j]:
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
        for j in range(4):
            if word[i] == puzzle[j]:
                char_count += 1

        if correct_matches + present_matches < char_count:
            status[i] = 1

    #is__1-1:checked ~ #it__1-2:checked ~ #ia__1-3:checked ~ #ir__1-4:checked ~ #iee_1-5:checked ~ #r__1-1 { border: none; background: var(--green) !important; }
    #is__1-1:checked ~ #it__1-2:checked ~ #ia__1-3:checked ~ #ir__1-4:checked ~ #iee_1-5:checked ~ #r__1-2 { border: none; background: var(--yellow) !important; }
    #is__1-1:checked ~ #it__1-2:checked ~ #ia__1-3:checked ~ #ir__1-4:checked ~ #iee_1-5:checked ~ #r__1-3 { border: none; background: var(--gray) !important; }
    #is__1-1:checked ~ #it__1-2:checked ~ #ia__1-3:checked ~ #ir__1-4:checked ~ #iee_1-5:checked ~ #r__1-4 { border: none; background: var(--yellow) !important; }

    f.write("/* %s %s %s %s */\n" % (word[0], word[1], word[2], word[3]))
    if status[0]:
        f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #r__1-1 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[0]] ))
        f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #r__2-1 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[0]] ))
        f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #r__3-1 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[0]] ))
        f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #r__4-1 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[0]] ))
    
    if status[1]:
        f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #r__1-2 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[1]] ))
        f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #r__2-2 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[1]] ))
        f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #r__3-2 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[1]] ))
        f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #r__4-2 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[1]] ))

    if status[2]:
        f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #r__1-3 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[2]] ))
        f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #r__2-3 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[2]] ))
        f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #r__3-3 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[2]] ))
        f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #r__4-3 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[2]] ))
    
    if status[3]:
        f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #r__1-4 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[3]] ))
        f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #r__2-4 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[3]] ))    
        f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #r__3-4 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[3]] ))
        f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #r__4-4 { background: var(--%s) !important; }\n" % (word[0], word[1], word[2], word[3], color[status[3]] ))

    f.write("\n")

# If the keyboard is absent
for letter in ALPHABET:
    l = letter.lower()
    if l in puzzle:
        continue
    f.write("#i%s__1-1:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__1-2:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__1-3:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__1-4:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, l))

    f.write("#i%s__2-1:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__2-2:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__2-3:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__2-4:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, l))

    f.write("#i%s__3-1:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__3-2:checked ~ #iee_3-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__3-3:checked ~ #iee_3-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__3-4:checked ~ #iee_3-5:checked ~ .kb__%s,\n" % (l, l))

    f.write("#i%s__4-1:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__4-2:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__4-3:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, l))
    f.write("#i%s__4-4:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, l))

f.truncate(f.tell() - 2)
f.write(" { background: var(--dg); }\n\n")

# If the keyboard is present
for letter in ALPHABET:
    l = letter.lower()
    if l not in puzzle:
        continue
    i = 0
    for p in puzzle:
        i += 1
        if p == l:
            continue
        f.write("#i%s__1-%s:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__2-%s:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__3-%s:checked ~ #iee_3-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__4-%s:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, i, l))


f.truncate(f.tell() - 2)
f.write(" { background: var(--y); }\n\n")

# If the key is correct
for letter in ALPHABET:
    l = letter.lower()
    if l not in puzzle:
        continue
    i = 0
    for p in puzzle:
        i += 1
        if p != l:
            continue
        f.write("#i%s__1-%s:checked ~ #iee_1-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__2-%s:checked ~ #iee_2-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__3-%s:checked ~ #iee_3-5:checked ~ .kb__%s,\n" % (l, i, l))
        f.write("#i%s__4-%s:checked ~ #iee_4-5:checked ~ .kb__%s,\n" % (l, i, l))

f.truncate(f.tell() - 2)
f.write(" { background: var(--g); }\n\n")

f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #p___w { animation-name: timer; animation-duration: 8s; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))
f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #p___w { animation-name: timer; animation-duration: 8s; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))    
f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #p___w { animation-name: timer; animation-duration: 8s; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))
f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #p___w { animation-name: timer; animation-duration: 8s; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))

f.write("\n")

f.write("#i%s__1-1:checked ~ #i%s__1-2:checked ~ #i%s__1-3:checked ~ #i%s__1-4:checked ~ #iee_1-5:checked ~ #spacer { padding-bottom: 3600px; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))
f.write("#i%s__2-1:checked ~ #i%s__2-2:checked ~ #i%s__2-3:checked ~ #i%s__2-4:checked ~ #iee_2-5:checked ~ #spacer { padding-bottom: 3600px; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))    
f.write("#i%s__3-1:checked ~ #i%s__3-2:checked ~ #i%s__3-3:checked ~ #i%s__3-4:checked ~ #iee_3-5:checked ~ #spacer { padding-bottom: 3600px; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))
f.write("#i%s__4-1:checked ~ #i%s__4-2:checked ~ #i%s__4-3:checked ~ #i%s__4-4:checked ~ #iee_4-5:checked ~ #spacer { padding-bottom: 3600px; }\n" % (puzzle[0], puzzle[1], puzzle[2], puzzle[3] ))

f.write("\n")

f.write("#i%s__4-1:not(:checked) ~ #iee_4-5:checked ~ #p___l { animation-name: timer; animation-duration: 8s; }\n" % ( puzzle[0] ))
f.write("#i%s__4-2:not(:checked) ~ #iee_4-5:checked ~ #p___l { animation-name: timer; animation-duration: 8s; }\n" % ( puzzle[1] ))
f.write("#i%s__4-3:not(:checked) ~ #iee_4-5:checked ~ #p___l { animation-name: timer; animation-duration: 8s; }\n" % ( puzzle[2] ))
f.write("#i%s__4-4:not(:checked) ~ #iee_4-5:checked ~ #p___l { animation-name: timer; animation-duration: 8s; }\n" % ( puzzle[3] ))

f.write("\n")

f.close()