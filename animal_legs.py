import json


class AnimalsCounter:

    LEGS_COUNT_BY_ANIMAL = {"pigs": 4, "chickens": 2, "cows": 4}
    ANIMALS_INFO_FILE_PATH = "animals.json"

    def load_animals_count(self):
        try:
            with open(self.ANIMALS_INFO_FILE_PATH) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"There is no similar file in the directory: {self.ANIMALS_INFO_FILE_PATH}")
        except json.JSONDecodeError:
            print("JSON file contains invalid content")

    def get_legs_count(self, animals_count):
        count_of_legs = 0
        for animal, count in animals_count.items():
            count_of_legs += self.LEGS_COUNT_BY_ANIMAL[animal] * count
        return count_of_legs

    def get_total_number_of_animals_legs(self):
        animals_count_dict = self.load_animals_count()
        return self.get_legs_count(animals_count_dict)


if __name__ == "__main__":
    animals_counter = AnimalsCounter()
    print("The total number of legs in animals is:", animals_counter.get_total_number_of_animals_legs())
