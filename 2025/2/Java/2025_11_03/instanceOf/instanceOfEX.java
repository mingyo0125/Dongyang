class Person {}
class Student extends Person{}
class Researcher extends Person{}
class Professor extends Researcher{}

public class instanceOfEX
{
    static void print(Person p)
    {
        if (p instanceof Person) {System.err.println("Person");}
        if (p instanceof Student) {System.err.println("Student");}
        if (p instanceof Researcher) {System.err.println("Researcher");}
        if (p instanceof Professor) {System.err.println("Professor");}
    }

    public static void main(String[] args) {
        System.err.print("Student()-> \t");
        print(new Student());
        System.err.print("Researcher()-> \t");
        print(new Researcher());
        System.err.print("Professor()-> \t");
        print(new Professor());

    }
}
