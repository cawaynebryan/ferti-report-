if case == '111':  # TODO: Add functionality for this case
    if combo == 'NPK':
        lbs_fertilizer_one = math.ceil(crop.P / (fertilizer_one.P / 100))
        lbs_remaining = math.ceil(lbs_fertilizer_one * (fertilizer_one.N / 100))
        lbs_fertilizer_two = math.ceil((crop.N - lbs_remaining) / (fertilizer_two.N / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one, fertilizer_two.name: lbs_fertilizer_two}
        print(recommendation)

    if combo == 'NKP':
        pass
    if combo == 'PNK':
        pass
    if combo == 'PKN':
        pass
    if combo == 'KPN':
        pass
    if combo == 'KNP':
        pass

if case == '110':
    if fertilizer_one.P or fertilizer_two.N != 0:
        lbs_fertilizer_one = math.ceil(crop.P / (fertilizer_one.P / 100))
        lbs_remaining = math.ceil(lbs_fertilizer_one * (fertilizer_one.N / 100))
        lbs_fertilizer_two = math.ceil((crop.N - lbs_remaining) / (fertilizer_two.N / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one, fertilizer_two.name: lbs_fertilizer_two}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')

if case == '101':
    if (fertilizer_one.K or fertilizer_two.N) != 0:
        lbs_fertilizer_one = (math.ceil(crop.K / (fertilizer_one.K / 100)))
        lbs_remaining = math.ceil(lbs_fertilizer_one * (fertilizer_one.N / 100)) * 1  # Redundant 1 :)
        lbs_fertilizer_two = math.ceil((crop.N - lbs_remaining) / (fertilizer_two.N / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one, fertilizer_two.name: lbs_fertilizer_two}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')

if case == '011':
    if fertilizer_one.P or fertilizer_two.K != 0:
        lbs_fertilizer_one = (math.ceil(crop.P / (fertilizer_one.P / 100)))
        lbs_remaining = (math.ceil(lbs_fertilizer_one * (fertilizer_one.N / 100)))
        lbs_fertilizer_two = math.ceil((crop.K - lbs_remaining) / (fertilizer_two.K / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one, fertilizer_two.name: lbs_fertilizer_two}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')

if case == '100':
    if fertilizer_one.N != 0:
        lbs_fertilizer_one = math.ceil(crop.N / (fertilizer_one.N / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')

if case == '010':
    if fertilizer_one.P != 0:
        lbs_fertilizer_one = math.ceil(crop.P / (fertilizer_one.P / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')

if case == '001':
    if fertilizer_one.K != 0:
        lbs_fertilizer_one = math.ceil(crop.K / (fertilizer_one.K / 100))
        recommendation = {fertilizer_one.name: lbs_fertilizer_one}
        print(recommendation)
    else:
        print('Try a different combination of fertilizers')