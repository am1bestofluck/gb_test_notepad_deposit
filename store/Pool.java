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
        System.out.println("");
        throw new UnsupportedOperationException("Unimplemented method 'roll'");
    }

    @Override
    public HashMap<Item, Integer> giveaway() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'giveaway'");
    }

    @Override
    public HashMap<Item, Integer> prize() {
        return this.pool;
    }

    public static void main(String[] args) {
        Pool a = new Pool();
        Item asd = new Item(23,0.56);
        a.add(asd,20);
        a.add(asd,40);
        System.out.println(a.prize());


    }

}