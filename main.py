import copy, math


class Crop:
    def __init__(self, name, n=0, p=0, k=0):
        self.N = n
        self.P = p
        self.K = k
        self.name = name
        self.ratio = [{"N": self.N}, {"P": self.P}, {"K": self.K}]
        self.formation = f"{self.N}-{self.P}-{self.K}"

    def sorted(self):
        ratio = copy.deepcopy(self.ratio)
        for J in range(len(ratio) - 1, 0, -1):  # Bubble sort
            for i in range(J):
                if list(ratio[i].values())[0] < list(ratio[i + 1].values())[0]:
                    ratio[i], ratio[i + 1] = ratio[i + 1], ratio[i]
        return ratio

    def __repr__(self):
        return f'{self.crop} {self.formation}'


class Fertilizer(Crop):  # fertilizer object - inherits form Crop
    def __init__(self, name, n=0, p=0, k=0):
        super().__init__(name, n, p, k)
        self.weight = self.N + self.P + self.K

    def __repr__(self):
        return f'{self.name} + {self.formation}'


def fertilizer_recommendation(crop, *args):
    """" Determine quantity of fertilisers base on crop need """

    recommendations = {}
    for idx, fertilizer in enumerate(args):
        highest_ratio, middle_ratio, lowest_ratio = fertilizer.sorted()
        highest_npk_key, highest_npk_vale = highest_ratio.popitem()
        middle_npk_key, middle_npk_value = middle_ratio.popitem()
        lowest_npk_key, lowest_npk_value = lowest_ratio.popitem()

        #TODO: if max of fertilizer one is grater than middle of fertilizer 2

        if highest_npk_vale != 0:  # Todo: make sure that only fertilizer one is assigned
            highest_of_ratio = getattr(fertilizer, highest_npk_key)
            requirement_highest_kg = math.ceil(getattr(crop, highest_npk_key) * (100/highest_of_ratio))

        recommendations.update({
            fertilizer.name: requirement_highest_kg,
        })

        if middle_ratio != 0:
            middle_of_ratio = getattr(fertilizer, middle_npk_key)
            added_kg_middle = (middle_of_ratio / 100) * requirement_highest_kg
            remaining_middle = math.ceil(getattr(crop, middle_npk_key) - added_kg_middle)
            # print(remaining_middle)  # remaining middle value

        if lowest_ratio != 0:
            lowest_of_ratio = getattr(fertilizer, lowest_npk_key)
            added_kg_lowest = (lowest_of_ratio / 100) * requirement_highest_kg
            remaining_lowest = math.ceil(getattr(crop, lowest_npk_key) - added_kg_lowest)
            # print(remaining_lowest)  # remaining lowest value

        # todo Should only be applied to the first instance

        setattr(crop, highest_npk_key, 0)
        setattr(crop, middle_npk_key, remaining_middle)
        setattr(crop, lowest_npk_key, remaining_lowest)

    return recommendations


def main():

    crop = Crop("Corn", 120, 60, 40)
    recommendations = fertilizer_recommendation(crop, Fertilizer("DAP", 18, 46, 0), Fertilizer("MOP", 22, 8, 7))
    print(recommendations)


if __name__ == "__main__":
    main()

