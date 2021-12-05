#!/usr/bin/env python3

is_testing = True
file_name = "test_input" if is_testing else "input"
report = open(file_name).read().strip().split("\n")


class ReportParser:
    gamma_rate = ""
    epsilon_rate = ""
    power_consumption_rating = ""
    oxygen_generator_rating = ""
    co2_scrubber_rating = ""
    life_support_rating = ""
    report = []

    def __init__(self, report):
        self.report = report

    def get_power_consumption_rating(self):
        self.power_consumption_rating = self.gamma_rate * self.epsilon_rate
        return self.power_consumption_rating

    def get_life_support_rating(self):
        self.life_support_rating = (
            self.oxygen_generator_rating * self.co2_scrubber_rating
        )
        return self.life_support_rating

    def get_decimal_from_binary(self, binary):
        return int(binary, 2)

    def parse_rates(self):
        binary_gamma_rate = ""
        binary_epsilon_rate = ""

        for bit_index in range(0, len(self.report[0])):
            zero_count = 0
            one_count = 0
            for index, number in enumerate(report):
                bit_to_compare = number[bit_index]

                if bit_to_compare == "0":
                    zero_count += 1
                elif bit_to_compare == "1":
                    one_count += 1

            if zero_count > one_count:
                binary_gamma_rate += "0"
                binary_epsilon_rate += "1"
            else:
                binary_gamma_rate += "1"
                binary_epsilon_rate += "0"

        print(binary_epsilon_rate)
        print(binary_gamma_rate)

        self.gamma_rate = self.get_decimal_from_binary(binary_gamma_rate)
        self.epsilon_rate = self.get_decimal_from_binary(binary_epsilon_rate)

    def get_oxygen_generator_rating(self):
        potential_ratings = self.report

        while len(potential_ratings) > 1:
            for bit_index in range(0, len(self.report[0])):
                zero_count = 0
                one_count = 0
                numbers_with_0_at_position = []
                numbers_with_1_at_position = []
                for index, number in enumerate(potential_ratings):
                    bit_to_compare = number[bit_index]

                    if (bit_to_compare) == "0":
                        zero_count += 1
                        numbers_with_0_at_position.append(number)
                    else:
                        one_count += 1
                        numbers_with_1_at_position.append(number)

                if zero_count > one_count:
                    potential_ratings = numbers_with_0_at_position
                elif zero_count == one_count:
                    potential_ratings = numbers_with_1_at_position
                else:
                    potential_ratings = numbers_with_1_at_position

        self.oxygen_generator_rating = self.get_decimal_from_binary(
            potential_ratings[0]
        )

    def get_co2_scrubber_rating(self):
        potential_ratings = self.report

        while len(potential_ratings) > 1:
            for bit_index in range(0, len(self.report[0])):
                zero_count = 0
                one_count = 0
                numbers_with_0_at_position = []
                numbers_with_1_at_position = []
                for index, number in enumerate(potential_ratings):
                    bit_to_compare = number[bit_index]

                    if (bit_to_compare) == "0":
                        zero_count += 1
                        numbers_with_0_at_position.append(number)
                    else:
                        one_count += 1
                        numbers_with_1_at_position.append(number)

                if zero_count < one_count:
                    potential_ratings = numbers_with_0_at_position
                elif zero_count == one_count:
                    potential_ratings = numbers_with_0_at_position
                else:
                    potential_ratings = numbers_with_1_at_position

                if len(potential_ratings) == 1:
                    break

        self.co2_scrubber_rating = self.get_decimal_from_binary(potential_ratings[0])

    def part_one(self):
        self.parse_rates()
        self.get_power_consumption_rating()

    def part_two(self):
        self.get_oxygen_generator_rating()
        self.get_co2_scrubber_rating()
        self.get_life_support_rating()

    def display(self):
        print("The gamma rate is: ", self.gamma_rate)
        print("The epsilon rate is: ", self.epsilon_rate)
        print("The power consumption rating is: ", self.power_consumption_rating)
        print("------------------------------------------------------------------")
        print("The CO2 scrubber rating is: ", self.co2_scrubber_rating)
        print("The oxygen generator rating is: ", self.oxygen_generator_rating)
        print("The life support rating is: ", self.life_support_rating)


if __name__ == "__main__":
    generated_report = ReportParser(report)

    generated_report.part_one()
    generated_report.part_two()

    generated_report.display()
