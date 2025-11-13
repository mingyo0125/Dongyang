public class MyAnimalList {
    private Animal[] animals = new Animal[5];
    private int nextIndex = 0;

    public void add (Animal a)
    {
        if(nextIndex < animals.length)
        {
            animals[nextIndex] = a;
            System.out.println(a.name + "이 " + nextIndex + "에 추가됨");
            nextIndex++;
        }
    }

    public void showThem()
    {
        int i = 0;
        for (Animal animal : animals) {
            System.out.println(i + "번째 인덱스에는 " + animal.name + "이 저장되어 있음");
            i++;
        }

        System.err.println("\n");
    }

    public void doThem()
    {
        Vet v = new Vet();

        System.out.println("주사놓기시작");

        for (Animal animal : animals)
        {
            v.Jusa(animal);
        }
    }
}
