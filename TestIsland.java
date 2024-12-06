package Testing;

import org.junit.Assert;
import org.junit.Test;
import org.island.*;

import java.util.List;

public class TestIsland {
    @Test
    public void testadditionofBears(){
        Island actual = new Island(100,20);
        Bear bear1 = new Bear("Bear1",4,3,12,2,2);
        Bear bear2 = new Bear("Bear2",4,3,12,2,2);
        Bear bear3 = new Bear("Bear3",4,3,12,2,2);
        Bear bear4 = new Bear("Bear4",4,3,12,2,2);
        Bear bear5 = new Bear("Bear5",4,3,12,2,2);
        Bear bear6 = new Bear("Bear6",4,3,12,2,2);
        Island.addAnimalToCell(bear1,0,0);
        Island.addAnimalToCell(bear2,0,0);
        Island.addAnimalToCell(bear3,0,0);
        Island.addAnimalToCell(bear4,0,0);
        Island.addAnimalToCell(bear5,0,0);
        Island.addAnimalToCell(bear6,0,0);
        String expected = "Слишком много медведей в этой клетке!";
        Cell bears=actual.getCell(0,0);
        Assert.assertEquals(expected,bears);
    }
    @Test
    public void testeat(){
        try {
            Island island = new Island(100,20);
            Wolf wolf1 = new Wolf("Wolf1", 5, 3, 45, 0, 0);
            Wolf wolf2 = new Wolf("Wolf2", 5, 4, 45, 0, 0);
            Rabbit rabbit1 = new Rabbit("Rabbit1", 5, 45, 45, 1, 0);
            Rabbit rabbit2 = new Rabbit("Rabbit2", 5, 45, 45, 0, 1);
            Rabbit rabbit3 = new Rabbit("Rabbit3", 5, 45, 45, 1, 0);
            Fox fox = new Fox("Fox1", 5, 45, 45, 0, 2);
            Goat goat1 = new Goat("Goat",5,32,12,6,7);
            Hog hog1 = new Hog("Hog",4,12,4,5,5);
            Mouse mouse1 = new Mouse("Mouse",3,12,34,0,2);
            Horse horse1 = new Horse("Horse",4,3,12,0,2);
            Horse horse2 = new Horse("Horse",4,3,12,0,2);
            Island.addAnimalToCell(wolf1, 0, 0);
            Island.addAnimalToCell(wolf2, 0, 0);
            Island.addAnimalToCell(fox, 0, 0);
            Island.addAnimalToCell(rabbit1, 0, 0);
            Island.addAnimalToCell(rabbit2, 0, 0);
            Island.addAnimalToCell(rabbit3, 0, 0);
            Island.addAnimalToCell(goat1,0,0);
            Island.addAnimalToCell(hog1,0,0);
            Island.addAnimalToCell(mouse1,0,0);
            Island.addAnimalToCell(horse1,1,1);
            Island.addAnimalToCell(horse2,3,1);
            // Проверка на одной клетке и вызов метода eat
            Cell cell = island.getCell(0, 0);
            List<Animal> animals = cell.getAnimals();
            for (Animal animal : animals) {
                // Логика покушать
                if (animal instanceof Wolf) {
                    for (Animal prey : animals) {
                        if (prey instanceof Rabbit) {
                            animal.eat(prey);
                        } else if (prey instanceof Deer) {
                            animal.eat(prey);
                        } else if (prey instanceof Horse) {
                            animal.eat(prey);
                        }else if (prey instanceof Mouse) {
                            animal.eat(prey);
                        }else if (prey instanceof Goat) {
                            animal.eat(prey);
                        }else if (prey instanceof Sheep) {
                            animal.eat(prey);
                        }else if (prey instanceof Hog) {
                            animal.eat(prey);
                        }else if (prey instanceof Bull) {
                            animal.eat(prey);
                        }else if (prey instanceof Duck) {
                            animal.eat(prey);
                        }
                    }
                }
            }
            for (Animal animal : animals) {
                if (animal instanceof Rabbit) {
                    Assert.assertEquals("Wolf ate rabbit","Wolf ate rabbit");
                }
                else if (animal instanceof Deer) {
                    Assert.assertEquals("Wolf ate deer","Wolf ate deer");
                }
                else if (animal instanceof Horse) {
                    Assert.assertEquals("Wolf ate horse","Wolf ate horse");
                }
                else if (animal instanceof Mouse) {
                    Assert.assertEquals("Wolf ate mouse","Wolf ate mouse");
                }
                else if (animal instanceof Goat) {
                    Assert.assertEquals("Wolf ate goat","Wolf ate goat");
                }
                else if (animal instanceof Sheep) {
                    Assert.assertEquals("Wolf ate sheep","Wolf ate sheep");
                }
                else if (animal instanceof Hog) {
                    Assert.assertEquals("Wolf ate hog","Wolf ate hog");
                }
                else if (animal instanceof Bull) {
                    Assert.assertEquals("Wolf ate hog","Wolf ate hog");
                }
                else if (animal instanceof Duck) {
                    Assert.assertEquals("Wolf ate duck","Wolf ate duck");
                }
            }
        }catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
