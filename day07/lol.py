'''
https://adventofcode.com/2020/day/7
'''
with open("input.txt") as f:
    line = f.readline()
    inputs = {}
    while line:
        if line.split():
            # set the parent bag color as the KEY and the colors it holds (VALUE) as an array
            parentBag = ' '.join(line.split()[:3]).replace("bags", "")
            childrenBags = []
            innerBags = ' '.join(line.split()[4:])
            # we don't care HOW MANY of each bag it can hold, so we filter that out
            for i in innerBags.split(", "):
                # append the filtered result to childrenBags array
                childrenBags.append(' '.join(i.split()[1:-1]))
            inputs[parentBag.strip()] = childrenBags
        line = f.readline()
#print(json.dumps(inputs, indent=2))


def numBags(color):
    '''
    I had a tough time with this one, so after hours of trying, I decided to seek help online
    THIS CODE LOGIC CAME FROM https://www.youtube.com/watch?v=7IOd7wvxDX0
    Highly recommend watching. He explains it really well :)
    '''
    containsColor = []  # keeps track of the bags that hold the specified color
    for k, v in inputs.items():
        # check to see if the colors are in the value arrays
        for el in v:
            if color == el:
                # if it is, append it to containsColor array
                containsColor.append(k)
    checkedColors = []
    if len(containsColor) == 0:
        return []
    else:
        for color in containsColor:
            checkedColors.append(color)
            checkedColors += numBags(color)
        return set(checkedColors)


print(len(numBags("shiny gold")))