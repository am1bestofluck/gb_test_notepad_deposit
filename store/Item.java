import java.util.Scanner;

/**
 * Item
 */
public class Item {

    Integer id;
    public Integer getId() {
        return id;
    }
    Double chance;

    public Double getChance() {
        return chance;
    }

    public Item() {
        Scanner read = new Scanner(System.in);
        System.out.println("id?");
        this.id= read.nextInt();
        System.out.println("drop chance?");
        this.chance = read.nextDouble();
        // read.close();
    }

    public Item( int id, Double chance){
        this.id = id;
        this.chance = chance;
    }
    @Override
    public String toString() {
        return String.format("Item with id %d and drop chance %f", this.getId(),this.getChance());
    }
    @Override
    public boolean equals(Object obj) {
        return this.getId()==((Item)obj).getId();
    }
    public static void main(String[] args) {
        Item a = new Item(1,2.0);
        System.out.println(a);
        Item b = new Item();
        System.out.println(b);

    }
    }