let coins = 1000;

const symbols = ['🍒', '🍋', '🍉', '⭐'];

function spin() {
    let bet = parseInt(document.getElementById('bet').value);
    let result = document.getElementById('result');
    
    if (isNaN(bet) || bet <= 0) {
        result.textContent = "Veuillez entrer une mise valide.";
        return;
    }
    
    if (bet > coins) {
        result.textContent = "Vous n'avez pas assez de pièces pour cette mise.";
        return;
    }

    coins -= bet;
    document.getElementById('coins').textContent = coins;

    // Spin the reels and show results
    let symbol1 = spinReel('reel1', bet);
    let symbol2 = spinReel('reel2', bet);
    let symbol3 = spinReel('reel3', bet);

    checkWin(bet, symbol1, symbol2, symbol3);
}

function spinReel(reelId, bet) {
    let reel = document.getElementById(reelId);
    reel.innerHTML = '';
    let chance = Math.random();
    let winProbability = Math.min(0.1 + (bet / 1000), 0.5); // Increase chance of winning with higher bets

    let symbol;
    if (chance < winProbability) {
        // Higher chance to get a winning symbol
        symbol = symbols[Math.floor(Math.random() * 2)]; // 🍒 or ⭐
    } else {
        // Normal chance to get any symbol
        symbol = symbols[Math.floor(Math.random() * symbols.length)];
    }

    let symbolDiv = document.createElement('div');
    symbolDiv.className = 'symbol';
    symbolDiv.textContent = symbol;
    reel.appendChild(symbolDiv);

    return symbol;
}

function checkWin(bet, symbol1, symbol2, symbol3) {
    if (symbol1 === symbol2 && symbol2 === symbol3) {
        let winnings = bet * 2;
        coins += winnings;
        document.getElementById('coins').textContent = coins;
        document.getElementById('result').textContent = `Félicitations ! Vous avez gagné ${winnings} pièces avec ${symbol1} ${symbol2} ${symbol3} !`;
    } else {
        document.getElementById('result').textContent = `Dommage, vous avez perdu avec ${symbol1} ${symbol2} ${symbol3}.`;
    }
}

function getCoin() {
    coins++;
    document.getElementById('coins').textContent = coins;
}
