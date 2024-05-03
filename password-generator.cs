using System;
using System.Linq;
using System.Collections.Generic;

namespace Password_Generator
{
    public class Password
    {
        public Password(int length, bool uppercaseLetters, bool digits, bool specialCharacters)
        {
            Length = length;
            UppercaseLetters = uppercaseLetters;
            Digits = digits;
            SpecialCharacters = specialCharacters;
        }

        public int Length { get; set; }
        public bool UppercaseLetters { get; set; }
        public bool Digits { get; set; }
        public bool SpecialCharacters { get; set; }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Password currPassword = new Password(8, false, false, false);
            string password = "";
            while (true)
            {
                Console.Clear();
                Console.WriteLine("---\tPassword Generator\t---");
                Console.WriteLine();
                Console.WriteLine("[0] <- Exit");
                Console.WriteLine();
                Console.WriteLine("[1] Generator Settings");
                Console.WriteLine("[2] Generate Password");

                Console.WriteLine();
                Console.Write("Choose an option: ");

                string[] validInputs = { "0", "1", "2" };
                string input;

                do
                {
                    input = Console.ReadLine();
                } while (!validInputs.Contains(input));

                var Menu = new Program();
                switch (Convert.ToInt32(input))
                {
                    case 0:
                        {
                            return;
                        }
                    case 1:
                        {
                            currPassword = Menu.Settings(currPassword);
                            break;
                        }
                    case 2:
                        {
                            password = Menu.Generator(currPassword);
                            Console.WriteLine($"Your password is: {password}");
                            Console.ReadLine();
                            break;
                        }
                }
            }
        }

        public Password Settings(Password currPassword)
        {
            Console.Clear();
            Console.WriteLine("---\tSettings\t---");
            Console.WriteLine();
            Console.WriteLine("[0] <- Back");
            Console.WriteLine();
            Console.WriteLine("[1] Change Password Length\t\t\t" + "Status: " + currPassword.Length);
            Console.WriteLine("[2] Enable Uppercase Letters\t\t" + "Status: " + currPassword.UppercaseLetters);
            Console.WriteLine("[3] Enable Digits\t\t\t" + "Status: " + currPassword.Digits);
            Console.WriteLine("[4] Enable Special Characters\t\t" + "Status: " + currPassword.SpecialCharacters);
            Console.WriteLine();

            string[] validInputs = { "0", "1", "2", "3", "4" };
            string input = "";
            while (!validInputs.Contains(input))
            {
                input = Console.ReadLine();
            }

            switch (Convert.ToInt32(input))
            {
                case 0:
                    {
                        return currPassword;
                    }
                case 1:
                    {
                        int newLength;
                        bool validInput;

                        do
                        {
                            Console.Write("The new password length is: ");

                            // Read user input and attempt to convert it to a number
                            string userInput = Console.ReadLine();
                            validInput = int.TryParse(userInput, out newLength);

                            if (!validInput || newLength <= 0)
                            {
                                Console.WriteLine("Invalid input. Please enter a positive number.");
                            }
                        } while (!validInput || newLength <= 0);

                        Console.WriteLine($"The new password length is {newLength}.");
                        // You can use newLength here to set or save the password length
                        currPassword.Length = newLength;
                        Console.ReadLine();
                        break;
                    }

                case 2:
                    {
                        currPassword.UppercaseLetters = !currPassword.UppercaseLetters;
                        break;
                    }
                case 3:
                    {
                        currPassword.Digits = !currPassword.Digits;
                        break;
                    }
                case 4:
                    {
                        currPassword.SpecialCharacters = !currPassword.SpecialCharacters;
                        break;
                    }
            }
            Settings(currPassword);
            return currPassword;
        }

        public string Generator(Password currPassword)
        {
            List<char> characters = new List<char>() { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
            List<char> uppercaseLetters = new List<char>() { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
            List<char> digits = new List<char>() { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            List<char> specialCharacters = new List<char>() { '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', '"', ',', '.', '<', '>', '/', '?' };

            if (currPassword.UppercaseLetters)
                characters.AddRange(uppercaseLetters);

            if (currPassword.Digits)
                characters.AddRange(digits);

            if (currPassword.SpecialCharacters)
                characters.AddRange(specialCharacters);

            Random random = new Random();
            string result = "";

            for (int i = 0; i < currPassword.Length; i++)
            {
                result += characters[random.Next(characters.Count)];
            }
            return result;
        }
    }
}