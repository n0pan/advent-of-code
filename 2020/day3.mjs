import { input } from "./inputs/day3.mjs";

const TREE = "#";
const SLOPES = [
  { right: 1, down: 1, numberOfTrees: 0 },
  { right: 3, down: 1, numberOfTrees: 0 },
  { right: 5, down: 1, numberOfTrees: 0 },
  { right: 7, down: 1, numberOfTrees: 0 },
  { right: 1, down: 2, numberOfTrees: 0 }
];
let currentMap = input;

function duplicateMap(input) {
  input.forEach((row, index) => {
    input[index] = row.concat(input[index]);
  });
}

function getTotalNumberOfTrees(slopes) {
  const numberOfTrees = slopes.map(slope => slope.numberOfTrees);
  return numberOfTrees.reduce((x, y) => x * y);
}

let numberOfTrees = 0;

SLOPES.forEach(slope => {
  let currentColumn = slope.right;
  let currentRow = slope.down;
  while (currentRow <= currentMap.length - 1) {
    if (currentColumn >= currentMap[currentRow].length) {
      duplicateMap(currentMap);
    }
    if (currentMap[currentRow].charAt(currentColumn) === TREE) {
      slope.numberOfTrees++;
    }
    currentColumn += slope.right;
    currentRow += slope.down;
  }
});

console.log("numberOfTrees: ", getTotalNumberOfTrees(SLOPES));
