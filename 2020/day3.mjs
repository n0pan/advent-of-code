import { input } from "./inputs/day3.mjs";

const TREE = "#";
const STARTING_COLUMN = 3;
const STARTING_ROW = 1;
let currentMap = input;

function duplicateMap(input) {
  input.forEach((row, index) => {
    input[index] = row.concat(input[index]);
  });
}

let numberOfTrees = 0;
let currentColumn = STARTING_COLUMN;
let currentRow = STARTING_ROW;

while (currentRow <= currentMap.length - 1) {
  if (currentColumn >= currentMap[currentRow].length) {
    duplicateMap(currentMap);
  }
  if (currentMap[currentRow].charAt(currentColumn) === TREE) {
    ++numberOfTrees;
  }
  currentColumn += STARTING_COLUMN;
  currentRow += STARTING_ROW;
}

console.log("numberOfTrees: ", numberOfTrees);
