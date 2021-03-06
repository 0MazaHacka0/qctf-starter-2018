﻿using System;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;

namespace Level2
{
    static class Win32
    {
        [DllImport("kernel32.dll")]
        public static extern IntPtr LoadLibrary(string dllToLoad);

        [DllImport("kernel32.dll")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procedureName);

        [DllImport("kernel32.dll")]
        public static extern bool FreeLibrary(IntPtr hModule);
    }
    
    internal class Program
    {
        public static void Main(string[] args)
        {
            if (Authorize())
            {
                Console.WriteLine("Security check complete. Starting application...");
            }
            else
            {
                Console.WriteLine("Security check failed. Exiting...");
                return;
            }
            var fileName = Path.GetTempFileName();
            var assembly = Assembly.GetExecutingAssembly();
            var resourceStream = assembly.GetManifestResourceStream(nameof(Level2) + ".level3.dll");
            using (var fileStream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
            {
                while (resourceStream.Position < resourceStream.Length)
                {
                    fileStream.WriteByte(Deobfuscate((byte)resourceStream.ReadByte()));
                }
            }
            var library = Win32.LoadLibrary(fileName);
            var checkPtr = Win32.GetProcAddress(library, "check");
            var check = (Action)Marshal.GetDelegateForFunctionPointer(checkPtr, typeof(Action));
            check();
            Win32.FreeLibrary(library);
            File.Delete(fileName);
        }

        private static bool Authorize()
        {
            Console.WriteLine("Please, complete security check to run this application.");
            Console.Write("Enter PIN: ");
            var input = Console.ReadLine();
            long pin;
            return long.TryParse(input, out pin) && pin == $PIN;
        }

        private static byte Deobfuscate(byte obfuscated)
        {
            return (byte)(255 - obfuscated);
        }
    }
}