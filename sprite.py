import copy


def _clone(r):
    return copy.deepcopy(r)


# 从大到小
def sortByHeight(r):
    print(r)
    result = []
    r = _clone(r)
    result = sorted(r, key=lambda x: x['h'])

    return result


# end sortByHeight

def createSprite(r):
    r2 = []
    length = len(r)

    def create():
        for i, v in enumerate(r):
            w, h = v[0], v[1]
            r2.append({'w': w, 'h': h, 'p': i})

    sampleArr = sortByHeight(r)
    MaxHeightReact = sampleArr[0]['h']
    MaxWeightReact = sampleArr[0]['w']

    return None
