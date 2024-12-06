using System.Dynamic;

namespace _20._10._2023_Binnärrechner
{
    internal class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.Write("Schreibe eine bliebige Natürliche Zahl die in Binär Code umgewanelt werden soll:");
                string input =null;
                do
                {
                    input = Console.ReadLine();
                    if (input == "" )
                    {
                        Console.WriteLine("Versuche es Nocheinmal:");
                    }
                    
                }while (input == "");

                string zahlBinär = "";
                try
                {
                    int dezimalZahl;
                    dezimalZahl = Convert.ToInt32(input);
                    zahlBinär = Codierer(dezimalZahl);
                }
                catch (Exception e) 
                {
                    Console.WriteLine(e.Message);
                }
                
                
                Console.WriteLine($"Die Zahl {input} schreibt man in Binär Code: {zahlBinär}");
                Console.ReadLine();
            }while (true);

        }
        static string Codierer(int input)
        {
            string antwort = null;
            int rest = 0;
            do
            {
                input = input / 2;
                rest = input % 2;
                antwort = antwort + rest ;
            } while (input != 0);

            return antwort;
        }
    }
}