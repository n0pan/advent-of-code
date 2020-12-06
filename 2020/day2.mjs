import { passwords } from "./inputs/day2.mjs";

function splitPassword(password) {
  const splitPassword = password.split(" ");
  const policy = getPolicy(splitPassword[0], splitPassword[1]);
  return { ...policy, password: splitPassword[2] };
}

function getPolicy(limit, policyLetter) {
  const letterLimit = limit.split("-");
  const affectedLetter = policyLetter.charAt(0);

  return {
    letter: affectedLetter,
    firstIndex: parseInt(letterLimit[0]),
    secondIndex: parseInt(letterLimit[1])
  };
}

function getNumberOfValidPasswords(passwords) {
  let validCount = 0;
  passwords.forEach(pw => {
    const password = splitPassword(pw);
    const pass = password.password;
    const { firstIndex, secondIndex, letter } = password;
    if (
      (pass[firstIndex - 1] === letter && pass[secondIndex - 1] !== letter) ||
      (pass[firstIndex - 1] !== letter && pass[secondIndex - 1] === letter)
    ) {
      validCount += 1;
    }
  });
  console.log("validCount: ", validCount);
  return validCount;
}

getNumberOfValidPasswords(passwords);
