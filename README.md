![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/98336206/177213884-58390904-70c0-42b2-9e90-fdc51163761f.png)
## AirBnB clone - The console
What we did in this project, it's a Class that's in charge of the initialization, serealization and deserealization of our future instances.

## Our Console

> **Remember**: to give permissions (if you don't already have them) to the file to make it executable.

```
$ chmod u+x console.py
```

## How to use the console:

It is executed with the following command `./console.py`

These are the commands that are used in our console and what they are for:

- **Create**: Create a new instance of BaseModel.
- **Update**: Updates an instance based on the class name and id by adding or updating attribute.
- **Show**: Prints the string representation of an instance based on the class name.
- **All**: Prints all string representation of all instances based or not on the class name.
- **Destroy**: Deletes an instance based on the class name and id.
- **Help**: Provides information about the command.
- **Quit**: Quits the console.

|**Objects**             |HTML|
|-----------|-----------------------------|
|User|      |Name and other iformation about the user|
|City|      |City in where the place is in|
|State|     |State where the City is located|
|Place|     |Information about, in this case the hotel|
|Review|    |What people think of the place they stayed at|
|Amenity|   |What features the place has|
|-----------|-----------------------------|

We created a simple flow of serealization/deserealization: Instance <-> Dictionary <-> JSON chain <-> archive.
We created all of the classes utilyzed for AirBnB (User, State, City, Place...) that inherit the BaseModel.
We created the first abstract storage motor of the project: archive storage.
We created every unit test to validate all of our classes and the storage motor.
