import { input } from "./inputs/day3.mjs";

const map = input.map(line => line.split(""));

let numOfTrees = 0;

let currentColumn = 3;
let currentRow = 1;

while (map[currentRow][currentColumn]) {
  console.log(
    "map[currentRow][currentColumn]: ",
    map[currentRow][currentColumn]
  );
  if (map[currentRow][currentColumn] === "#") {
    numOfTrees += 1;
  }
  currentColumn += 3;
  currentRow += 1;
}

console.log("numOfTrees: ", numOfTrees);
console.log('map[0]: ', map[0]);
