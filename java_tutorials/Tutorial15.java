// http://xahlee.org/java-a-day/read_file.html
// Example of Reading and Writing a File

import java.io.*;

public class Tutorial15
{
    public static void main(String[] args)  throws IOException {
        File inputFile = new File("t_in.txt");
        File outputFile = new File("t_out.txt");
            
        FileReader in = new FileReader(inputFile);
        FileWriter out = new FileWriter(outputFile);
        int c;

        while((c = in.read()) != -1)
            out.write(c);
        in.close();
        out.close();
    }
}
    
            
            
            