import sys

fn = sys.argv[1]

new_lines = []
for line in open(fn):
    words = line.split()
    if len(words) > 0: 
        first_word = words[0]
        if len(first_word) > 1:
            if first_word[1] == '.' and len(first_word) == 2:
                words[0] = first_word[0] + '\.'
                line = ' '.join(words)
    if line[-1] != '\n':
        line += '\n'
    new_lines.append(line)


f = open(fn, 'w')
f.write(''.join(new_lines))
f.close()
    
