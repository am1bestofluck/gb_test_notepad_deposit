
import java.util.Scanner;
class Controller{

    enum lines{
        roll, 
        add, 
        giveaway, 
        prize,
        qqq
    }
    public static void main(String[] args) {
        Help.main(new String[] {}); // может позже распарсю; вообще странно
        // что нужно что-то докачивать
        Boolean exitCondition=false;
        while (!exitCondition) { 
            
            System.out.print("listening...");
            Scanner loop = new Scanner(System.in);
            String tmp = loop.nextLine().toLowerCase();
            Boolean match = false;
            Controller.lines[] valid = Controller.lines.values();
            for (int i = 0; i < valid.length; i++) {
                if (tmp.equals(valid[i].toString())){
                    match=true;
                }
            }
            if (!match){
                System.out.println("no match");
                Help.main(new String[] {});
                continue;}
            switch (tmp.toLowerCase()) {
                case "qqq":
                    System.out.println("got it!");
                    exitCondition=true;
                    break;
                case "roll":
                    System.out.println("randomize reward");
                    // TODO
                    break;
                case "add":
                    System.out.println("add positions to prize pool");
                    // TODO
                    break;
                case "giveaway":
                    System.out.println("report on lots already out");
                    // TODO
                    break;
                case "prize":
                    System.out.println("report on lots in pool yet");
                    // TODO
                    break;
                default:
                    break;
            }}}
}