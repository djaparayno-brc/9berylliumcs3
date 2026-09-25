# Advanced Class Relationships
## Previous Activities
- [classAttrib](classAttributesMethods.md)
- [classRel](classRelationships.md)
## Existing System Description:
- There are two connected classes: Musician and MusicalInstrument. MusicalInstrument stores information about instruments, while Musician stores information about musicians and their assigned instruments. Musician can have and play many musical instruments.
## Inheritance Relationship
- Parent: MusicalInstrument
- Child: Guitar
- Explanation: Guitar is a child class of MusicalInstrument because it inherits the common attributes and methods from it, while also adding a specific data only for guitar, such as the number of strings.
## Inheritance UML
![Inheritance](im/inheritanceDiagram.png)
## Composition/Aggregation
- Relationship: Aggregation
- Explanation: A musician can have a musical instrument, but the musical instrument can still exist independently from the musician. For me, the instrument is created first and then assigned to the musician.
## Advanced UML Diagram
![Advanced UML](im/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](im/advancedTestRun.png)
## Object Diagram
![Objects](im/advancedObjectDiagram.png)

## Reflection
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
- I chose this inheritance relationship because I figured that the child class of MusicalInstrument should be a type of a musical instrument, commonly a guitar. The child class, Guitar, is a type of my parent class, MusicalInstrument. "Why is a guitar considered a musical instrument?" That is because a guitar can create melodic tunes and musical sounds that establish the fundamental components of being a musical instrument. 

2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- Guitar reuses the attributes that were already defined in MusicalInstrument. This implies that inheritance reduces code duplication. Features such as name, type, primary_material, play(), and get_details() are already inherited, needing not to be declared again.

3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
- My HAS-A relationship is aggregation because a musical instrument can still independently exist from a musician, as the musician can own/have a musical instrument. The two are created separately; musical instrument is made first, then assigned to the musician. Therefore, when you remove the musician, the musical instrument won't also be removed due to the HAS-A relationship being aggregation, which means that two objects has a weak HAS-A relationship.
  
4. What is the difference between Association from Part III and the advanced relationship you
implemented?
- Association in Part III establishes a general connection between Musician and MusicalInstrument without specifying a whole-part ownership relationship. Aggregation is more specific due to the fact that it represents Musician as the whole and MusicalInstrument as a part that can exist independently. Therefore, I can say that the aggregation relationship provides additional information about the lifecycle and independence of the related objects.
  
5. How does your design follow the DRY principle?
- My design follows the DRY principle because the common attributes and methods of the MusicalInstrument class were also placed into the Guitar class. The Guitar class then inherits these existing features instead of redefining the same code. This reduces the needless code repetition and makes the program easier to modify and become more efficient.
