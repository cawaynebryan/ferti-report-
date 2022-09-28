import copy


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


def fertilizer_recommendation(crop, fertilizer):
    """" Determine quantity of fertilisers base on crop need """

    recommendation = {}

    highest_ratio, middle_ratio, lowest_ratio = fertilizer.sorted()
    highest_npk_key, highest_npk_vale = highest_ratio.popitem()
    middle_npk_key, middle_npk_value = middle_ratio.popitem()
    lowest_npk_key, lowest_npk_value = lowest_ratio.popitem()

    if highest_npk_vale != 0:
        highest_of_ratio = getattr(fertilizer, highest_npk_key)
        requirement_highest_kg = getattr(crop, highest_npk_key) * (100/highest_of_ratio)
        recommendation.update({highest_npk_key: requirement_highest_kg})  # recommendation for highest_npk_key

    if middle_ratio != 0:
        middle_of_ratio = getattr(fertilizer, middle_npk_key)
        added_kg_middle = (middle_of_ratio / 100) * requirement_highest_kg
        remaining_middle = getattr(crop, middle_npk_key) - added_kg_middle
        print(remaining_middle)  # remaining middle value  

    if lowest_ratio != 0:
        lowest_of_ratio = getattr(fertilizer, lowest_npk_key)
        added_kg_lowest = (lowest_of_ratio / 100) * requirement_highest_kg
        remaining_lowest = getattr(crop, lowest_npk_key) - added_kg_lowest
        print(remaining_lowest)  # remaining lowest value

    setattr(crop, highest_npk_key, 0)
    setattr(crop, middle_npk_key, remaining_middle)
    setattr(crop, lowest_npk_key, remaining_lowest)


def main():

    crop = Crop("Corn", 120, 60, 40)
    fertilizer_one = Fertilizer("DAP", 18, 46, 12)
    fertilizer_recommendation(crop, fertilizer_one)


if __name__ == "__main__":
    main()

