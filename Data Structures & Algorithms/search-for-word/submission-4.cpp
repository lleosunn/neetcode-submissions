class Solution {
public:

    int ROWS, COLS;
    bool exist(vector<vector<char>>& board, string word) {
        ROWS = board.size();
        COLS = board[0].size();
        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (board[r][c] == word[0]) {
                    if (dfs(board, word, r, c, 0)) return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(vector<vector<char>>& board, string& word, int r, int c, int i) {
        // takes in a board, word, and cell and checks if
        // you can form the word starting at the cell

        if (i == word.size()) return true;

        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || 
            board[r][c] != word[i] || board[r][c] == '#') {
                return false;
        } // return false if r, c out of bounds, letter doesnt match desired
        // or r, c has already been used

        // mark this cell as used 
        board[r][c] = '#';
        bool out = dfs(board, word, r - 1, c, i + 1) ||
                    dfs(board, word, r + 1, c, i + 1) ||
                    dfs(board, word, r, c - 1, i + 1) ||
                    dfs(board, word, r, c + 1, i + 1);
        board[r][c] = word[i];
        return out;
    } 

};
