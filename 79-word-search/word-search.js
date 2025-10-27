/**
 * Word Search - Backtracking (DFS)
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
    const rows = board.length;
    const cols = board[0].length;

    // Helper DFS function
    const dfs = (i, j, index) => {
        // ✅ Base case: found the entire word
        if (index === word.length) return true;

        // ❌ Out of bounds or mismatch
        if (
            i < 0 || i >= rows ||
            j < 0 || j >= cols ||
            board[i][j] !== word[index]
        ) {
            return false;
        }

        // Temporarily mark the cell as visited
        const temp = board[i][j];
        board[i][j] = '#';

        // Explore all 4 directions
        const found =
            dfs(i + 1, j, index + 1) ||
            dfs(i - 1, j, index + 1) ||
            dfs(i, j + 1, index + 1) ||
            dfs(i, j - 1, index + 1);

        // Backtrack: restore the cell
        board[i][j] = temp;

        return found;
    };

    // Iterate over each cell as potential starting point
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            // Optional pruning: only start if first letter matches
            if (board[i][j] === word[0] && dfs(i, j, 0)) {
                return true;
            }
        }
    }

    return false;
};