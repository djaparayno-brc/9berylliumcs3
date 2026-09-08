# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | str | public | The instrument's name can be viewed by anyone. |
| type | str | private | The type should only be changed through class methods. |
| primary material | str | private | The material is an internal property that should be protected. |
| price | int | public | The price can be viewed directly by users. |
## Updated UML Class Diagram
![Class Diagram](ClassDiagramSG5(2).png)
## Python Implementation
[View Python Source](classImplementation.py)
## Test Run
![Test Run](classTestRun.png)
## Object Diagram
![Object Diagram](objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
