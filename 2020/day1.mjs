import { input } from "./inputs/day1.mjs";

function multiply(x, y, z) {
  return x * y * z;
}

function sumTo2020(inputList) {
  inputList.forEach(input => {
    inputList.forEach(comparativeInput => {
      inputList.forEach(secondComparativeInput => {
        if (input + comparativeInput + secondComparativeInput === 2020) {
          console.log(
            "multiply(input, comparativeInput, secondComparativeInput): ",
            multiply(input, comparativeInput, secondComparativeInput)
          );
          return multiply(input, comparativeInput, secondComparativeInput);
        }
      });
    });
  });
}

sumTo2020(input);
