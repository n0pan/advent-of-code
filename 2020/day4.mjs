import { input } from "./inputs/day4.mjs";

const REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
const VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];

function parsePassports(input) {
  const cleanedPassports = input
    .split("\n\n")
    .map(p => p.split(/[\n\r\s]+/))
    .map(pp => {
      let passport = {};
      pp.forEach(p => {
        const splitPassport = p.split(":");
        passport = { ...passport, [splitPassport[0]]: splitPassport[1] };
      });
      return passport;
    });
  return cleanedPassports;
}

function validatePassport(passport) {
  const passportKeys = Object.keys(passport);
  return REQUIRED_FIELDS.every(field => {
    if (passportKeys.includes(field)) {
      return validateField({ key: field, value: passport[field] });
    }
    return false;
  });
}

function validateField({ key, value }) {
  switch (key) {
    case "byr":
      if (value.length === 4) {
        if (Number(value) >= 1920 && Number(value) <= 2002) {
          return true;
        }
        return false;
      }
      return false;
    case "iyr":
      if (value.length === 4) {
        if (Number(value) >= 2010 && Number(value) <= 2020) {
          return true;
        }
        return false;
      }
      return false;
    case "eyr":
      if (value.length === 4) {
        if (Number(value) >= 2020 && Number(value) <= 2030) {
          return true;
        }
        return false;
      }
      return false;
    case "hgt":
      if (value.includes("cm")) {
        const height = value.split("cm")[0];
        if (Number(height) >= 150 && Number(height) <= 193) {
          return true;
        }
        return false;
      } else if (value.includes("in")) {
        const height = value.split("in")[0];
        if (Number(height) >= 59 && Number(height) <= 76) {
          return true;
        }
        return false;
      }
      return false;
    case "hcl":
      if (RegExp(/^#[0-9a-f]{6}$/).test(value)) {
        return true;
      }
      return false;
    case "ecl":
      if (VALID_EYE_COLORS.includes(value)) {
        return true;
      }
      return false;
    case "pid":
      if (value.length === 9) {
        return true;
      }
      return false;
    case "cid":
      return true;
    default:
      return false;
  }
}

const passports = parsePassports(input);
let validPassports = 0;

passports.forEach(passport => {
  if (validatePassport(passport)) validPassports++;
});

console.log("validPassports: ", validPassports);
