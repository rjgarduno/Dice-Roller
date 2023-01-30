const numDiceInput = document.getElementById("num-dice");
const numSidesInput = document.getElementById("num-sides");
const rollDiceBtn = document.getElementById("roll-dice");
const diceArea = document.getElementById("dice-area");
const totalP = document.getElementById("total");

rollDiceBtn.addEventListener("click", function() {
  const numDice = numDiceInput.value;
  const numSides = numSidesInput.value;
  diceArea.innerHTML = "";
  let total = 0;
  for (let i = 0; i < numDice; i++) {
    const diceValue = Math.floor(Math.random() * numSides) + 1;
    total += diceValue;
    const dice = document.createElement("div");
    dice.classList.add("dice");
    dice.textContent = diceValue;
    diceArea.appendChild(dice);
  }
  totalP.textContent = "Total: " + total;
});
