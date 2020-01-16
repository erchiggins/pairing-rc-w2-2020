window.onload = function() {
    createBoard();
}

let board = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
];

function printBoard() {
    console.log(board.map((row) => row.join("")).join("\n"));
}

function iterate() {
    let container = document.getElementById('board');
    // create a copy with which to replace the existing board
    let newBoard = [];
    board.forEach((row) => {newBoard.push(row.slice())});
    // for each element NOT IN THE BUFFER, update copy according to its status and living neighbors
    for( let r = 1; r < board.length -1; r++){
        for (let c = 1; c < board[0].length -1; c++) {
            let liveNeighbors = countLiveNeighbors(r,c);
            if (board[r][c]) {
                // current cell is alive
                if (liveNeighbors <= 1 || liveNeighbors >= 4) {
                    // loneliness or overpopulation
                    newBoard[r][c] = 0;
                    container.childNodes[r-1].childNodes[c-1].className='';
                }
            } else {
                // current cell is dead
                if (liveNeighbors === 3) {
                    newBoard[r][c] = 1;
                    container.childNodes[r-1].childNodes[c-1].className='alive';
                }
            }
        }
    }
    // set board to the copy instead 
    board = newBoard;
    // print the board
    printBoard();
}

function countLiveNeighbors(row, col) {
    let livingNeighbors = 0;
    for (r = row - 1; r <= row + 1; r++) {
        for (c = col - 1; c <= col + 1; c++) {
            if (r === row && c === col) {
                continue;
            }
            if (board[r][c]) {
                livingNeighbors++;
            }
        }
    }
    return livingNeighbors;
}

function createBoard() {
    let container = document.getElementById('board');
    for( let r = 1; r < board.length -1; r++){
        let row = document.createElement('div');
        container.appendChild(row);
        for (let c =1; c < board[0].length -1; c++) {
            let cell = document.createElement('span');
            if (board[r][c]) {
                cell.className='alive';
            }
            row.appendChild(cell);
        }
    }
}