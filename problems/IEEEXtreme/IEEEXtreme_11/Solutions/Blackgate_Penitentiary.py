# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

num_crew = get_number()
# print("Number of crew members:", num_crew)
names = []
heights = []
# heights = {}
while 1:
    try:
        name = get_word()
        h = get_number()
        # heights[name] = h
        names.append(name)
        heights.append(h)
    except:
        break

# print(names)
# print(heights)

z = list(zip(heights, names))
z.sort()
# print(z)
names_sorted = [name for _, name in z]
heights_sorted = [height for height, _ in z]
# print(names_sorted)
# print(heights_sorted)


uniq_heights = numpy.unique(heights_sorted)
# print(uniq_heights)
for i in uniq_heights:
    w = numpy.where(heights_sorted == i)[0]
    # print(w)
    s = [names_sorted[o] for o in w]
    # print(s)
    print(' '.join(s), min(w)+1, max(w)+1)
