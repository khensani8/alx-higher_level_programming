#!/usr/bin/node

// Your addMeMaybe function
function addMeMaybe(number, theFunction) {
  number++; // Increment the number
  theFunction(number); // Call the provided function with the updated number
}

// Export the addMeMaybe function
module.exports = {
  addMeMaybe,
};

