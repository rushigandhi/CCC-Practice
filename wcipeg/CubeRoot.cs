using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    class Program
    {
        static void Main(string[] args)
        {

            int total = int.Parse(Console.ReadLine());
            int k = int.Parse(Console.ReadLine());

            while (total > 0)
            {

                while ((k % 10) != 2)
                {

                    k = k + 1;

                }

                while (((k * k * k) % 1000) != 888)
                {
                    k = k + 10;

                }

                Console.WriteLine(k);

                total--;

            }
            Console.ReadLine();

        }
    }
