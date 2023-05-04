import java.util.Random;
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
    public static String RandomJoke(){
        String[] book= new String[]{
            """
                I started a new job this week.

                On my first day it was my co-worker Frank's birthday; we gathered around his desk to sing happy birthday and share a cake.
                
                Just as we finished singing the office door slammed open.
                
                In strides a creature: upper body of a man, lower body of a horse. He screams LOOK AT ME EVERYBODY and proceeds to grab Frank's cake and gallop out of the office with it.
                
                I was dumbfounded but my new colleagues just rolled their eyes: "oh thats just Bill" they said "always the Centaur of attention."
                    """,
            """
                i started carrying a knife after a mugging attempt years ago
                Since then my mugging attempts have been a lot more successful.
                    """,
            """
                A lawyer just lost a career making/breaking case so Satan sees this as an opportunity to approach him and make him an offer.

                Satan: I will make you the most successful lawyer in history. You will never lose a case again. You will be famous. You will be wealthy beyond your wildest imagination.
                
                Lawyer: What's the catch?
                
                Satan: I want the souls of your parents, your siblings, your spouse, your children and all your future descendants for damnation in hell for all eternity.
                
                Lawyer: Okay, but what's the catch?
                    """,
            """
                I've been attempting a murder
                But I can't get more than 1 crow
                    """,
                    """
                        What’s the difference between Brazil and the USA?
                        About 1500 arrests within 48 hours of an attempted coup.
                            """,
            """
                He said he would kiss me or die in the attempt.
                Well?
                
                He has no life-insurance, and I pitied his poor old mother.
                
                    """,
            """
                Do you know the Football player whose missing 75% of his spine?
                He's the Quarterback.
                    """,
            """
                I tried to hit on an IT woman After three attempts she locked me out.
                    """,
            """
                Some construction workers are working on a high building early in the morning. Sadly, Steve slips off a ledge,
                 spirals down to the ground and is critically injured. They attempt to save him with CPR, but there is a large hole in his
                  skull that the blood keeps squirting out of, and he dies. Bill says 'Someone needs to tell Steve's wife'. Joey says 
                  'I'll do it, I'm very sensitive'. Joey goes off, then a few hours later comes back with two cases of beer. 
                  Bill asks 'Where did you get the beer?' Joey says 'Steve's wife gave it to me'. 
                  Bill says 'You told her Steve was dead and she gave you beer?' 'Not exactly. 
                  When she answered the door I said "You must be Steve's widow', she said 'I'm not a widow" and I said "I bet you two cases of beer you are".'
                    """
        };
        Random tmp = new Random();
        return book[ tmp.nextInt(book.length)];}
    
}