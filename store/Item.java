import java.util.Scanner;
/**
 * Item
 */
public class Item {

    Integer id;
    public Integer getId() {
        return id;
    }
    Integer chance;
    Double price;

    public void setPrice(Double price) {
        this.price = price;
    }

    public Double getPrice() {
        return price;
    }

    public Integer getChance() {
        return chance;
    }

    public Item() {
        Scanner read = new Scanner(System.in);
        System.out.println("id?");
        this.id= read.nextInt();
        System.out.println("drop chance?");
        this.chance = read.nextInt();
        System.out.println("Price?");
        this.price = read.nextDouble();
        // read.close();
    }

    public Item( Integer id, Integer chance){
        this.id = id;
        this.chance = chance;
        this.price = 0.0;
    }

    public Item( Integer id, Integer chance, double price ){
        this.id = id;
        this.chance = chance;
        this.price = price;
    }

    @Override
    public String toString() {
        return String.format("Item with id %d, price %.2f and drop chance %f", this.getId(), this.getPrice(), 1/Double.valueOf(this.getChance()));
    }
    @Override
    public boolean equals(Object obj) {
        return this.getId()==((Item)obj).getId();
    }
    public static void main(String[] args) {
        Item a = new Item(1,2);
        System.out.println(a);
        // Item b = new Item();
        // System.out.println(b);
        Item c = new Item(5,50,23.0);
        Item d = new Item(5,40,33.0);
        System.out.println(c);
        System.out.println(d);
        System.out.println(a);
        System.out.println(c.equals(d));

    }
    }