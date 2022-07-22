import shutil
import os
import sys
import random
from util.termy import solve, key_dict, key_coords


# get all argument passed when script was ran
WORD = None
LENGTH = 4
GUESSES = 4
try:
    WORD = sys.argv[1]
    LENGTH = int(sys.argv[2])
    GUESSES = int(sys.argv[3])
except:
    pass


STATS = [0] * LENGTH
ITERATION = 0

STYLES = {
    'keyboard-initializer': ( GUESSES * 60 ) + ( 2 * 100 ) + 80,
}

# Get all words from 4 Letter Word File
text_file = open("constants/%sLW.txt" % (LENGTH), "r")
data = text_file.read()
words = data.split()

print(len(words))

# If a word wasn't supplied select a random word
if not WORD:
    WORD = random.choice(words).lower()
PUZZLE = [char for char in WORD]

# Termy algorithms
word_characters = []

for word in words:
    c = [char.lower() for char in word]
    if len(c) != LENGTH:
        print("A WORD IS NOT %s LETTERS" % (LENGTH))
        exit()
    word_characters.append(c)

def create_element(tag:str="div", contents:str="", style:str="", classes:list=[], **kwargs):
    style = ' style="%s"' % (style) if style else ""
    classes = ' class="%s"' % (" ".join(classes)) if classes else ""
    k = ""
    for key, value in kwargs.items():
        k += ' %s="%s"' % (key, value)
    contents = contents if contents else ""
    return "<%s%s%s%s>%s</%s>" % (tag, classes, style, k, contents, tag)


def generate_detail(key:str="", contents:str="", style:str="", classes:list=[], depth:int=1, completed:str=""):
    global LENGTH, ITERATION
    position = "bottom:%spx;left:%spx;" % (key_coords[key][0] * 60, (key_coords[key][1] * 20) + -200)
    summary = create_element(tag="summary", contents=key_dict[key], style=position+style, classes=classes)
    choice = ""
    result = ""
    if key != "ee" and key != "dd":
        bottom = int((GUESSES * 60) - (60 * ITERATION) + 204)
        left = int((LENGTH*-60/2)+((depth-1)*60))
        pos_bottom = "bottom:%spx;" % (bottom)
        pos_left = "left:%spx;" % (left)
        choice = create_element(tag="div", contents=key_dict[key], classes=['r__%s-%s' % (ITERATION, depth), 'choice'], style=pos_left+pos_bottom)
        if completed:
            status = solve(PUZZLE, completed)
            bottom = int(bottom+(GUESSES*60))
            pos_bottom = "bottom:%spx;" % (bottom)
            for i in range(LENGTH):
                left = (LENGTH*-60/2)+((i)*60)
                pos_left = "left:%spx;" % (left)
                result_type = 'correct' if status[i] == 2 else 'present' if status[i] == 1 else 'absent'
                result += create_element(tag="div", contents=key_dict[completed[i]], classes=['result', result_type], style=pos_left+pos_bottom)
    margin = ""
    # if depth == LENGTH: # We take this out due to the error in previous siblings (enter must be accessible at the very start)
    #     margin = create_element(tag="div", style="margin-bottom:240px")
    contents = summary + contents + choice + result + margin
    return create_element(tag="details", contents=contents)


def generate_keyboard_details(depth:int, keys:list=[], pool:list=[]):
    global GUESSES, LENGTH
    content = ""
    if depth == 1:
        content += generate_detail(key="ee", contents=create_element(tag="div", style="margin-bottom:%spx;" % (GUESSES*60)), classes=["kb__label", "kb__ee", 'kb__%s-%s' % (ITERATION, depth)], style="z-index: %s" % (20 - ITERATION))
    for key in keys:
        new_pool = []
        for word in pool:
            if word[depth - 1].lower() == key:
                new_pool.append(word)
        detail_contents = generate_keyboard_instance(depth, pool=new_pool)
        if  depth == LENGTH:
            content += generate_detail(key=key, contents=detail_contents, classes=["kb__label", "kb__%s" % (key), 'kb__%s-%s' % (ITERATION, depth)], depth=depth, completed=new_pool[0])
        else:
            content += generate_detail(key=key, contents=detail_contents, classes=["kb__label", "kb__%s" % (key), 'kb__%s-%s' % (ITERATION, depth)], depth=depth)
    return content


def generate_keyboard_instance(depth:int=0, pool:list=[]):
    global STATS, LENGTH
    depth += 1
    contents = ""
    if depth <= LENGTH:
        accepted = []
        for word in pool: #[ 'H', 'A', 'L', 'F' ]
            if word[depth - 1].lower() not in accepted:
                accepted.append(word[depth - 1].lower())
        contents = generate_keyboard_details(depth, keys=accepted, pool=pool)
        STATS[depth-1] = STATS[depth-1] + len(accepted)
    image = ""
    # image = create_element(tag='img', src='https://raw.githubusercontent.com/slyduda/termy-keyboards/main/disabled-keyboard.png', classes=['kb__image'], style="z-index:%s" % (depth))
    image = create_element(tag='div', style="position:absolute;background:rgba(17,24,39);width:400px;height:180px;bottom:0;left:-200px;z-index:%s" % (depth))
    return image + contents


def generate_keyboard():
    global ITERATION
    ITERATION += 1
    return create_element(tag="div", contents=generate_keyboard_instance(pool=word_characters), classes=["kb__%s"% (ITERATION), "kb"])


def generate_grid():
    global GUESSES, LENGTH
    rows = ""
    for i in range(GUESSES):
        cells = ""
        for j in range(LENGTH):
            cells += create_element(tag="div", classes=["cell"])
        rows += create_element(tag="div", classes=['grid-row'], contents=cells)
    return create_element(tag="section", classes=['grid'], contents=rows)

def main():
    global GUESSES, LENGTH, STYLES
    contents = create_element(tag="div", id="footer-hider")
    for i in range(GUESSES):
        contents = generate_keyboard() + contents

    contents = create_element(tag="section", contents=contents, id="k-wrapper")
    grid = generate_grid()
    
    # Change some stuff in the inline.html file
    filedata = None
    with open('src/inline.html', 'r') as file:
        filedata = file.read()
        filedata = filedata.replace('{{ keyboard }}', contents)
        filedata = filedata.replace('{{ grid }}', grid)
        filedata = filedata.replace('inline.css', 'index.css')

    with open('dist/index.html', 'w') as file:
        file.write(filedata)

    # Change some stuff in the pre.css file
    cssdata = None
    with open('src/inline.css', 'r') as file:
        cssdata = file.read()
        cssdata = cssdata.replace('guesses: 0', 'guesses: %s' % (GUESSES))
        cssdata = cssdata.replace('length: 0', 'length: %s' % (LENGTH))
        cssdata = cssdata.replace('var(--keyboard-initializer)', '%spx' % (STYLES['keyboard-initializer']))

    with open('dist/index.css', 'w') as file:
        file.write(cssdata)

    B = os.path.getsize('dist/index.html')
    print(STATS)
    print('%skb' % (B/(1024)))

# for i in range(LENGTH + 1):
main()