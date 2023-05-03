import java.util.HashMap;

interface PoolCanvas{
    
    public void add();

    public void add(Item item, Integer quantity);

    public Item roll();

    public HashMap<Item,Integer> giveaway();

    public HashMap<Item,Integer> prize();
}