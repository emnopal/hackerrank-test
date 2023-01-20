def PigLatin(s):
    return " ".join(list(map(lambda x: f"{x[-1]}" if x[-1] in ['!', '?'] else f"{x[1:]}{x[0]}ay", s.split(" "))))

print(PigLatin('Pig latin is cool'))
print(PigLatin('This is my string'))
print(PigLatin('O tempora o mores !'))
