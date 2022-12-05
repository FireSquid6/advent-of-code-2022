const fs = require("fs");
const clamp = (num, min, max) => Math.min(Math.max(num, min), max);

let total = 0;

const allFileContents = fs.readFileSync("./day-2/input.txt", "utf-8");
allFileContents.split(/\r?\n/).forEach((line) => {
  let score = 0;

  let opponent = line.charAt(0);
  let player = line.charAt(2);

  // convert away from characters
  let opponent_int = 0;
  switch (opponent) {
    case "A":
      opponent_int = 1;
      break;
    case "B":
      opponent_int = 2;
      break;
    case "C":
      opponent_int = 3;
      break;
  }

  let player_int = 0;
  switch (player) {
    case "X":
      // lose
      player_int = opponent_int - 1;
      if (player_int == 0) {
        player_int = 3;
      }
      break;
    case "Y":
      // draw
      player_int = opponent_int;
      break;
    case "Z":
      // win
      player_int = opponent_int + 1;
      if (player_int == 4) {
        player_int = 1;
      }
      break;
  }

  console.log(`Player int: ${player_int}`);
  console.log(`Opponent int: ${opponent_int}`);

  // if a tie, add 3
  if (opponent_int == player_int) {
    score += 3;
    console.log("Tie");
  } else {
    let winner = 0;
    switch (opponent_int + player_int) {
      case 3:
        winner = 2;
        break;
      case 4:
        winner = 1;
        break;
      case 5:
        winner = 3;
        break;
    }

    if (player_int == winner) {
      score += 6;
      console.log("I win!");
    } else {
      console.log("I lose :(");
    }
  }

  console.log(player);

  score += player_int;
  total += score;
});

console.log(`\nTotal: ${total}`);
