namespace Exponent_Methode
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string num1;
            string num2;
            
            double basis = 0;
            double exponent = 0;
            
            do 
            {
                Console.Write("Gebe eine Basis ein: ");
                num1 = Console.ReadLine();
                Console.Write("Gebe eine Exponent ein: ");
                num2 = Console.ReadLine();

                try
                {
                    basis = Convert.ToDouble(num1);
                    exponent = Convert.ToDouble(num2);
                }catch (Exception ex)
                {
                    Console.WriteLine("Gebe eine Zahl ein und keine Zeichen.");
                }

                double result = GetExponent(basis, exponent);
                if (result != -1)
                {
                    Console.WriteLine("Die Antwort ist "+result +"\n");
                }
            }while (num1 != null || num2 == null);
        }

        static double GetExponent(double basis, double exponent)
        {
            if (exponent== 1)
            {
                return basis;
            }else if (exponent == 0)
            {
                return 0;
            }
            else if (basis != 0)
            {
                double result = 0;
                for (double i = 0; i <= exponent; i++) 
                { 
                    result = basis * basis;
                }
                return result;
            }
            else
            {
                Console.WriteLine("Bitte gebe Zahlen an mit den ich rechnen kann. 0 als Basis ergibt immer 0...\n");
                return -1;
            }
        }
    }
}