public class Vet {
    public void Jusa(Animal animal)
    {
        System.out.print("수의사가 " + animal.name + "에게 주사를 놓음 ");
        animal.MakeNoise();
    }
}
