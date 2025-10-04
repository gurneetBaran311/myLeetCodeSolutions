/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
    let result = [];
    let board = [];
    for (let i = 0; i < n; i++) {
        board[i] = [];
        for (let j = 0; j < n; j++) {
            board[i][j] = '.';
        }
    }
    let backTracking = (board, colSet, diagonalSet, antiDiagonalSet, row) => {
        if (row === n) {
            result.push(transform(board));
        }
        for (let column = 0; column < n; column++) {
            if (colSet.has(column) || diagonalSet.has(row - column) || antiDiagonalSet.has(row + column)) continue;
            board[row][column] = 'Q';
            colSet.add(column);
            diagonalSet.add(row - column);
            antiDiagonalSet.add(row + column);
            backTracking(board, colSet, diagonalSet, antiDiagonalSet, row + 1);
            board[row][column] = '.';
            colSet.delete(column);
            diagonalSet.delete(row - column);
            antiDiagonalSet.delete(row + column);
        }
    };
    backTracking(board, new Set(), new Set(), new Set(), 0);
    return result;
};
function transform(borad) {
    return borad.map(i => i.join(''));
}