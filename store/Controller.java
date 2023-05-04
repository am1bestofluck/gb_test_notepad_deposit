
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
        Pool prizesPool= new Pool();
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
                    Item test = prizesPool.roll();
                    if (test != null){
                        System.out.println(String.format("Got a prize! %s", test.toString()));}
                    else {
                        System.out.println("Tough luck...:). Have an uplifting joke!");
                        System.out.println(Help.RandomJoke());}
                    
                    break;
                case "add":
                    System.out.println("add positions to prize pool");
                    Item newItem = new Item();
                    System.out.println("How much items to add?");
                    Integer qua = loop.nextInt();
                    prizesPool.add(newItem,qua);
                    break;
                case "giveaway":
                    System.out.println("report on lots already out");
                    System.out.println(prizesPool.giveaway());
                    break;
                case "prize":
                    System.out.println("report on lots in pool yet");
                    System.out.println(prizesPool.prize());
                    break;
                default:
                    break;
                    }
                }
            }
    }