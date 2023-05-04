import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Random;

/**
 * Pool
 */
public class Pool implements PoolCanvas {

    private HashMap<Item, Integer> pool;
    private HashMap<Item, Integer> log;

    public Pool() {
        this.pool = new HashMap<>();
        this.log = new HashMap<>();
    }

    public void add() {
        Scanner readSys = new Scanner(System.in);
        Item newItem = new Item();
        System.out.println("quantity?");
        int qua = readSys.nextInt();
        this.__add(newItem, qua);

    }

    public void add(Item item, Integer quantity) {
        this.__add(item, quantity);
    }

    private void __add(Item item, Integer quantity) {
        if (this.pool.containsKey(item)) {
            this.pool.put(item, this.pool.get(item) + quantity);
        } else {
            this.pool.put(item, quantity);
        }
    }

    @Override
    public Item roll() {
        // по очереди подбрасываем монетку, по каждой позиции;
        // в зачёт идёт самый дорогой приз
        ArrayList<Item> winners = new ArrayList<>();
        for (Item  roll_it: this.pool.keySet()) {
            if (this.pool.get(roll_it) > 0){
                Integer toss_coin = new Random().nextInt(roll_it.getChance());
                if (toss_coin == 0){ // 0 - попадение
                    winners.add(roll_it);
                }
                }
        }
            if (winners.size() == 0){
                return null;
            }
        Item out = winners.get(0);
        for (int i = 0; i < winners.size(); i++) {
                if( winners.get(i).getPrice() > out.getPrice()){
                    out = winners.get(i);
                }
            }
        this.pool.put(out, this.pool.get(out)-1);
        if (this.log.containsKey(out)){
            this.log.put(out, this.log.get(out)+1);
        }
        else this.log.put(out, 1);
        return out;
        
    }

    @Override
    public HashMap<Item, Integer> giveaway() {
        System.out.println("Prizes which have been already thrown");
        return this.log;
    }

    @Override
    public HashMap<Item, Integer> prize() {
        System.out.println("Prizes yet in pool");
        return this.pool;
    }

    public static void main(String[] args) {
        Pool a = new Pool();
        Item asd = new Item(23,4,23.0);
        Item qwe = new Item(34,1000,2300);
        Item jackpot = new Item(45,100000,1000000);
        a.add(asd,20);
        a.add(asd,40);
        a.add(qwe,140);
        a.add(jackpot,7);
        
        // System.out.println(a.prize());
        for (int i = 0; i < 2000; i++) {
            a.roll();
        }
        System.out.println("asd");
        System.out.println(a.giveaway());
        System.out.println(a.prize());


    }

}