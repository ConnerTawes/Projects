// Yeah I tried in cpp but I really hated learning something new so I started again in python.
// Uncomment the file when your ready to tackle this beast

// // This file will be the first solution made where the program will solve with brute force

// #include <iostream>
// #include <fstream>
// #include <vector>
// #include <string>
// #include <sstream>
// using namespace std;

// const int depth = 1000;
// const int rows = 9;
// const int cols = 9;
// int allBoards[depth][rows][cols];

// std::vector<std::vector<int>> stringTo2DIntArray(const std::string& input, int rows, int cols) {
//     std::vector<std::vector<int>> result(rows, std::vector<int>(cols));
//     std::stringstream ss(input);
//     std::string token;
//     char delimiter = ','; 
//     int row = 0;
//     int col = 0;

//     while (std::getline(ss, token, delimiter)) {
//         result[row][col] = std::stoi(token);
//         col++;
//         if (col == cols) {
//             col = 0;
//             row++;
//         }
//         if (row == rows) break;
//     }
//     return result;
// }

// int main () {

//   // Create a text string, which is used to output the text file
//   char strBoard[164];
//   int boardNum = 0;

//   // Read from the text file
//   ifstream MyReadFile("../boards/boards.txt");

//   // Use a while loop together with the getline() function to read the file line by line
//   while (MyReadFile.read(strBoard, 163)) {
//     // Output the text from the file
//     strBoard[164] = '\0';

//     // switch from string to 2d int array
//     char rowDelimiter = '\n';
//     char colDelimiter = ' ';
//     std::vector<std::vector<int>> arrayBoard = stringTo2DIntArray(strBoard, rows, cols);

//     for (int i = 0; i < rows; ++i) {
//         for (int j = 0; j < cols; ++j) {
//             std::cout << arrayBoard[i][j] << " ";
//         }
//         std::cout << std::endl;
//     }
//     // std::copy(std::begin(a1), std::end(a1), std::begin(a2));
//     // allBoards[boardNum] = arrayBoard;

//   }

//   // Close the file
//   MyReadFile.close();
//   cout << "Finished";
//   return 0;
// }