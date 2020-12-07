/*
Validate if a password meets the following requirements:
1. be at least 8 characters,
   - no more than 2 numbers
   - at least an uppercase letter
   - at least a special character (one of @, #, _, and / only)
2. cannot contain spaces,
3. cannot include the username
*/

// TODO: stop counting after finding 2 numbers
function howManyNumbers(string) {
  let numberOfDigits = 0;
  const stringToArray = string.split('');
  for (char of stringToArray) {
    if (!isNaN(char)) {
      numberOfDigits += 1;
    }
  }
  return numberOfDigits;
}

// TODO: stop counting after finding an uppercase letter
function howManyUpperCase(string) {
  let numberOfUpperCase = 0;
  const stringToArray = string.split('');
  for (char of stringToArray) {
    if (isNaN(char) && char === char.toUpperCase()) {
      numberOfUpperCase += 1;
    }
  }
  return numberOfUpperCase;
}

// TODO: Return when the first special character is found
function containsSpecialCharacter(string) {
const validSpecialCharacters = [ '@', '#', '_', '/' ];
  for (char of string) {
    if (validSpecialCharacters.includes(char)) {
      return true;
    }
  }
  return false;
}

// TODO: Update condition after modifying the other functions
function isValidPassword(password, userName) {
  const numberOfDigits = howManyNumbers(password);
  const numberOfUpperCase = howManyUpperCase(password);
  const hasSpecialCharacter = containsSpecialCharacter(password);
  if (password.length < 8 
  || password.includes(' ')
  || password.toLowerCase().includes(userName.toLowerCase())
  || numberOfDigits > 2
  || numberOfUpperCase < 1
  || !hasSpecialCharacter) {
    return false;
  }
  return true;
}
