public class Animal {
    public String name;

    public Animal(String name) {
        this.name = name;
    }
    
    public void MakeNoise() {};
}

class Dog extends Animal
{
    public Dog(String name)
    {
        super(name);
    }

    @Override
    public void MakeNoise()
    {
        System.out.println(this.name + "울음소리");
    }
}

class Cat extends Animal
{
    public Cat(String name)
    {
        super(name);
    }
    
    @Override
    public void MakeNoise()
    {
        System.out.println(this.name + "울음소리");
    }
}

class Wolf extends Animal
{
    public Wolf(String name)
    {
        super(name);
    }
    
    @Override
    public void MakeNoise()
    {
        System.out.println(this.name + "울음소리");
    }
}

class Lion extends Animal
{
    public Lion(String name)
    {
        super(name);
    }
    
    @Override
    public void MakeNoise()
    {
        System.out.println(this.name + "울음소리");
    }
}

class Hipo extends Animal
{
    public Hipo(String name)
    {
        super(name);
    }
    
    @Override
    public void MakeNoise()
    {
        System.out.println(this.name + "울음소리");
    }
}
