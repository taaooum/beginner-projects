using System;
using System.Diagnostics.Contracts;
using System.IO;
using System.Linq.Expressions;
using System.Numerics;
using System.Reflection.Metadata;
using System.Security.Principal;
using System.Collections;

namespace Tic_Tac_Toe
{
    internal class Program
    {
        static List<int> playerPosition = new List<int>();
        static List<int> cpuPosition = new List<int>();

        static void Main(string[] args)
        {
            char[,] gameBoard = {
                {' ' ,'│' ,' ' ,'│' ,' ' },
                {'─','┼','─','┼','─' },
                { ' ', '│', ' ', '│', ' ' },
                {'─','┼','─','┼','─' },
                { ' ', '│', ' ', '│', ' ' } };

            PrintGameBoard(gameBoard);

            Console.WriteLine();

            int position;
            string input;
            string winner;
            do
            {
                do
                {
                    Console.Write("Welche Position willst du deinen Marker setzen(1-9)? ");
                    input = Console.ReadLine();

                    position = Convert.ToInt16(input);
                    
                    if (cpuPosition.Contains(position))
                    {
                        Console.WriteLine("Diese Position ist schon besetzt, versuche eine andere.");
                    }
                } while (string.IsNullOrEmpty(input) || cpuPosition.Contains(position));
                
                PrintPiece(gameBoard, position, "player");
                
                int cpuInput;
                do
                {
                    Random random = new Random();
                    cpuInput = random.Next(10);
                
                } while (playerPosition.Contains(cpuInput));
                
                
                PrintPiece(gameBoard, cpuInput, "cpu");

                winner = CheckWinner(playerPosition, cpuPosition);

                PrintGameBoard(gameBoard);

                for (int i = 0; i < playerPosition.Count; i++)
                {
                    Console.Write( playerPosition[i]);

                }
                Console.WriteLine();
                for (int i = 0; i < cpuPosition.Count; i++)
                {
                    Console.Write( cpuPosition[i]);
                }
                Console.WriteLine();

            
            } while (winner == "none");

            if (winner == "player")
            {
                Console.WriteLine("Du hast gewonnen!");
            }else if (winner == "cpu") {
                Console.WriteLine("Du hast verloren.");
            }
        }

        static void PrintGameBoard(char[,] gameBoard)
        {
            for (int i = 0; i < gameBoard.GetLength(0); i++)
            {
                for(int j = 0; j < gameBoard.GetLength(1); j++)
                {
                    Console.Write(gameBoard[i,j]);
                }
                Console.WriteLine();
            }
        }

        static void PrintPiece(char[,] gameBoard, int position, string currentPlayer) 
        {
            char symbol = ' ';
            //currentPlayer auswählen
            if (currentPlayer == "player")
            {
                symbol = 'X';
                playerPosition.Add(position);
            }else if(currentPlayer == "cpu")
            {
                symbol = 'O';
                cpuPosition.Add(position);
            }

            //position Umwandeln für Spalte und Reihe
            switch (position)
            {
                case 9:
                    gameBoard[0, 4] = symbol;
                    break;
                case 8:
                    gameBoard[0, 2] = symbol;
                    break;
                case 7:
                    gameBoard[0, 0] = symbol;
                    break;
                case 6:
                    gameBoard[2, 4] = symbol;
                    break;
                case 5:
                    gameBoard[2, 2] = symbol;
                    break;
                case 4:
                    gameBoard[2, 0] = symbol;
                    break;
                case 3:
                    gameBoard[4, 4] = symbol;
                    break;
                case 2:
                    gameBoard[4, 2] = symbol;
                    break;
                case 1:
                    gameBoard[4, 0] = symbol;
                    break;
                default:
                    break;
            }
            Console.WriteLine();
        }
        
        static string CheckWinner(List<int> playerPosition, List<int> cpuPosition)
        {
            string winner = "none";
            
            List<int> topRow        = new List<int> { 1, 2, 3 };
            List<int> middleRow     = new List<int> { 4, 5, 6 };
            List<int> bottomRow     = new List<int> { 7, 8, 9 };
            List<int> topCollum     = new List<int> { 1, 4, 7 };
            List<int> middleCollum  = new List<int> { 2, 5, 8 };
            List<int> bottomCollum  = new List<int> { 3, 6, 9 };
            List<int> crossRight    = new List<int> { 1, 5, 9 };
            List<int> crossLeft     = new List<int> { 3, 5, 7 };
                
            List<List<int>> winning = new List<List<int>>();
            winning.Add(topRow);
            winning.Add(middleRow);
            winning.Add(bottomRow);
            winning.Add(topCollum);
            winning.Add(middleCollum);
            winning.Add(bottomCollum);
            winning.Add(crossRight);
            winning.Add(crossLeft);

            // Iteration durch die verschachtelte Liste mit einer for-Schleife
            foreach (List<int> l in winning)
            {
                if (l.SequenceEqual(playerPosition))
                {
                    winner = "player";
                    break;
                }
                else if (l.SequenceEqual(cpuPosition))
                {
                    winner = "cpu";
                    break;
                }
                
            }
            return winner;
        }
    }
}