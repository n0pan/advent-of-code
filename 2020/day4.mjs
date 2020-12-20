import { input } from "./inputs/day4.mjs";

const REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

function formatPassports(input) {
  const groupedPassports = input.split("\n\n");
  const tempPassports = groupedPassports.map(p => {
    return p.split(/[\n\r\s]+/);
  });
  const cleanedPassports = tempPassports.map(pp => {
    return pp.map(p => {
      const splitPassport = p.split(":");
      return { [splitPassport[0]]: splitPassport[1] };
    });
  });
  return cleanedPassports;
}

// function validatePassports(passports) {
//   const cleanedPassports = passports.map(p => {
//     const passportFields = p.split(" ");
//     console.log('passportFields: ', passportFields);
//   });
// }

const passports = formatPassports(input);
// validatePassports(passports);
