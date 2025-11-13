public class Overriding
{
    public static void main(String[] args)
    {
        Weapon weapon = new Weapon();
        weapon.fire();
        weapon = new Cannon();
        weapon.fire();
    }
}

class Weapon
{
    protected int getDamage()
    {
        return 1;
    }

    protected void fire()
    {
        System.out.println(getDamage());
    }
}

class Cannon extends  Weapon
{
    @Override
    protected int getDamage()
    {
        return 10;
    }
}
