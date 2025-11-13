public class AnimalTestDrive{
    public static void main(String[] args) {
        MyAnimalList list = new MyAnimalList();
        Dog d = new Dog("Dog");
        Cat c = new Cat("Cat");
        Wolf w = new Wolf("Wolf");
        Lion l = new Lion("Lion");
        Hipo h = new Hipo("Hipo");

        list.add(d);
        list.add(c);
        list.add(w);
        list.add(l);
        list.add(h);

        System.err.println("");


        list.showThem();

        list.doThem();
    }
    
}