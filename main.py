import copy, math
from db import crops_db


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
        return f'{self.name} {self.formation}'


class Fertilizer(Crop):  # fertilizer object - inherits form Crop
    def __init__(self, name, n=0, p=0, k=0):
        super().__init__(name, n, p, k)
        self.weight = self.N + self.P + self.K #TODO: review purpose for this attribute

    def __repr__(self):
        return f'{self.name} + {self.formation}'


def calculate_fertilizer(crop, *args):
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
            requirement_highest_kg = math.floor(getattr(crop, highest_npk_key) * (100/highest_of_ratio))

        recommendations.update({
            fertilizer.name: requirement_highest_kg,
        })

        if middle_ratio != 0:
            middle_of_ratio = getattr(fertilizer, middle_npk_key)
            added_kg_middle = (middle_of_ratio / 100) * requirement_highest_kg
            remaining_middle = math.floor(getattr(crop, middle_npk_key) - added_kg_middle)
            # print(remaining_middle)  # remaining middle value

        if lowest_ratio != 0:
            lowest_of_ratio = getattr(fertilizer, lowest_npk_key)
            added_kg_lowest = (lowest_of_ratio / 100) * requirement_highest_kg
            remaining_lowest = math.floor(getattr(crop, lowest_npk_key) - added_kg_lowest)
            # print(remaining_lowest)  # remaining lowest value

        # todo Should only be applied to the first instance

        setattr(crop, highest_npk_key, 0)
        setattr(crop, middle_npk_key, remaining_middle)
        setattr(crop, lowest_npk_key, remaining_lowest)

    return recommendations


def get_selected_crop(selected):
    crop = crops_db.crops_collections.get(selected.capitalize())
    if crop is not None:
        required_n = crop.get('N')
        required_p = crop.get('P2O5')
        required_k = crop.get('K2O')
        selected_crop = Crop(selected, required_n, required_p, required_k)
        print(selected_crop)
    else:
        print('Crop does not exist in database')
    return selected_crop


def main():
    #TODO: make a test to varify if the fertilizer is in order and switch them
    recommendations = calculate_fertilizer(
        get_selected_crop("rice"),
        Fertilizer("DAP", 18, 46, 0),
        Fertilizer("Urea", 46, 0, 0)
    )
    print(recommendations)


if __name__ == "__main__":
    main()

