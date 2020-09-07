# **Collie** v1.2 - an expansion of [Dog](https://esolangs.org/wiki/DOG)

Collie is a programming language created by Reese Jacobson, based on Jeremy Ruten’s Dog. The purpose of this language is to expand the capabilities of Dog and turn it into a more “useful” programming language. The most notable features, among many, are `teach`, a way to define routines, and the removal of `jump` and `label` for better control structures. Some minor changes from Dog include calling values “treats” instead of “cookies”, the omission of plates since there are an unlimited number of dishes, and renaming a few other commands.

## Variables
Just like with Dog, you have a selection of dishes, the floor, and the mouth to store treats in. The difference here is that Collie allows an unlimited number of dishes, and unlimited floor and mouth space. This is because Collies are a smart breed and know how to keep track of things better than most dogs.

## Commands
Where **X** appears, you can replace it with dishX, floor, or a number. Where **V** appears, you can replace it with dishX or floor, but NOT a number. If **X** or **V** appears in square brackets, it's optional.
* **fetch X** - Place X treats into dog's mouth, adding on to whatever number is already there.
* **drop V** - Move all treats from dog's mouth into V, adding onto whatever number is already there.
* **pickup V** - Move treats from V into dog's mouth, adding on to whatever number is already there.
* **eat [X]** - Subtract X amount of treats from dog's mouth. If X isn't provided, dog eats all the treats.
* **take** - Waits for user to input a number and adds that number to the dog's mouth.
* **show** - Prints the number that is in the dog's mouth.
* **give** - Prints the number that is in the dog's mouth and resets dog's mouth to 0.
* **bark "string"** - Prints whatever is in the quotes to the screen. Newlines are NOT added to the end.
* **sit X** - Pause program execution for X seconds.
* **bed** - Ends the program. Dog goes to bed.
* **teach *trick*** - Define a routine, or trick. Anything indented inside it is considered part of the trick. Any time the dog does a trick, all values remain the same.
* **heel** - Marks the end of a trick, like a return. It’s possible to use this conditionally inside a function by putting a number or value before it.
* ***trick*** - Call a routine.
* **X *cmd*** - Execute a command X amount of times.

## Use
I've provided an interpreter written in Python, as well as a sample program in `test.col`.

```sh
./main.py test.col
```

## To do / Goals
* A real-time interpreter to directly type into
* Bring back plates (and possibly allow for backwards compatibility)
* Make a little more like assembly to turn it into a teaching tool??
