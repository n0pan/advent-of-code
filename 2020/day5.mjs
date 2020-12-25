import { input } from "./inputs/day5.mjs";

const FRONT = "F";
const BACK = "B";
const LEFT = "L";
const RIGHT = "R";
const INITIAL_ROWS_RANGE = {
  start: 0,
  end: 127
};

let currentRange = INITIAL_ROWS_RANGE;
const boardingPassesRows = [];

function getRow(char, range) {
  if (char === FRONT) {
    currentRange = { start: range.start, end: Math.floor(range.end / 2) };
  } else if (char === BACK) {
    currentRange = { start: Math.ceil(range.start / 2), end: range.end };
  } else {
    throw Error(`invalid case ${char}`);
  }
}

const boardingPasses = input.split("\n");

boardingPasses.forEach(pass => {
  const formattedPass = pass.split("");
  boardingPassesRows.push(getRow(formattedPass, INITIAL_ROWS_RANGE));
});
