import copy


def _clone(r):
    return copy.deepcopy(r)


# 从大到小
def sortByHeight(r):
    result = []
    r = _clone(r)
    result = sorted(r, key=lambda x: x['h'])

    return result


# end sortByHeight

def createSprite(r):
    r2 = []
    sprite = []
    length = len(r)

    def create():
        for i, v in enumerate(r):
            w, h = v[0], v[1]
            r2.append({'w': w, 'h': h, 'p': i})

        sample_arr = sortByHeight(r2)
        # 最大画布高度
        max_height_react = sample_arr[0]['h']
        # 最大画布宽度
        max_weight_react = sample_arr[0]['w']

        for value in r2:
            x, y = reckon(value['p'])
            sprite.append({'p': value['p'], 'x': x, 'y': y})

        return {
            'w': max_weight_react,
            'h': max_height_react,
            'r': sprite
        }

    # end create
    def reckon(n):
        if n < 10:
            x = n * 108
            y = 0
        elif n == 10:
            x = 0
            y = 72
        elif n % 10 == 0:
            i = n // 10
            x = 972
            y = (i + 1) * 72
        else:
            i = n % 10
            x = i * 108
            y = n // 10 * 72

        return x, y

    # end reckon

    return create()
