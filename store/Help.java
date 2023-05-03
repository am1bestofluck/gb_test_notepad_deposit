import java.util.Scanner;
import java.io.EOFException;
import java.io.File;
import java.io.FileNotFoundException;
/**
 * Help
 */
public class Help {

    public static void main(String[] args) {
        try{
        File helpFile = new File("help.json");
        Scanner sc = new Scanner(helpFile);
        while (sc.hasNextLine()){
            System.out.println(sc.nextLine());
        }
        sc.close();
    }
        catch (FileNotFoundException e){
            e.printStackTrace();
        }
    }
}