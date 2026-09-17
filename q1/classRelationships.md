# Class Relationships: Association and Multiplicity
## Previous Work
- [Part I - Classes and Objects](classObjectUML.md)
- [Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
- Class: MusicalInstruments
- Description: All musical instruments have their own names, types, and the way they are played.
## New Related Class
- Class: Musicians
- Description: Every musician has a typical instrument they use a lot in their songs and music.
## Association
- Relationship: Musicians HAS-A MusicalInstruments.
- Explanation: These two are interconnected, for every musician has at least one instrument.
## Multiplicity
- Multiplicity: many-to-many
- Explanation: A musician can play many instruments, and instrument can be played by many musicians.

## UML Class Relationship Diagram
![Class Relationship Diagram](im/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](im/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](im/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
- A musician can have multiple musical instruments, and a musical instrument can be played by many musicians.
### What multiplicity did you choose and why?
- The multiplicity I chose is many to many because a musician can play multiple musical instruments, and also a musical instrument can be played by many musicians.
### How did you implement the relationship in Python?
- I just used assign_instrument() to store Musical_Instrument object inside of Musician object.
### Why did you store an object reference instead of copying its data?
- It actually connects the two objects together which is better than just copying data.
### If your relationship uses many, why is a list appropriate?
- Because for each musician, it can store multiple MusicalInstrument objects together for each musician.
### LLM prompts used
- An LLM was used, source: GoogleAI <img width="904" height="713" alt="image" src="https://github.com/user-attachments/assets/24498c1c-8050-4711-81ee-2973d1d6eca0" />
