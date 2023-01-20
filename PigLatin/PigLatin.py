def PigLatin(s):
    return " ".join(map(lambda x: x[-1] if not x[-1].isalnum() else f"{x[1:]}{x[0]}ay", s.split(" ")))

print(PigLatin('Pig latin is cool'))
print(PigLatin('This is my string'))
print(PigLatin('O tempora o mores !'))
