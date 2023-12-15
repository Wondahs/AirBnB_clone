![hbnb_logo](https://user-images.githubusercontent.com/111706856/218246185-8578fd32-ae95-434d-beff-91a772aa2142.png)


ALXBnB is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB. The goal of the
 project is to deploy on our server a simple copy of the AirBnB website.


## Console :computer:
The Console is the command line interpreter. The console provides an 
interface between the user and the kernel and executes programs called commands.
For example, if a user enters the "less" command, the shell executes the command.
It can be used to handle and manipulate all classes utilized by
the application
It is also capable of executing other programs such as applications,
scripts and as well other user programs.

### Using the Console

The console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

Alternatively, to use the console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create BaseModel
8ff582e2-c587-4d13-bf47-289f438c4097
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.973410a2-7096-41f4-a4e9-01cb219bc229": {"updated_at": "2023-12-04T07:16:54.204720", "created_at": "2023-12-04T07:16:54.204650", "__class__": "Base
Model", "id": "973410a2-7096-41f4-a4e9-01cb219bc229"}}
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
614e71d1-f359-465d-8f84-359a5eb841b5
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (614e71d1-f359-465d-8f84-359a5eb841b5) {'id': '614e71d1-f359-465d-8f84-359a5eb841b5', 'created_at': datetime.datetime(2023, 12, 4, 10, 33, 16, 667262), 
'updated_at': datetime.datetime(2023, 12, 4, 10, 33, 16, 667302)}
(hbnb) 
(hbnb) User.show(614e71d1-f359-465d-8f84-359a5eb841b5)
[User] (614e71d1-f359-465d-8f84-359a5eb841b5) {'id': '614e71d1-f359-465d-8f84-359a5eb841b5', 'created_at': datetime.datetime(2023, 12, 4, 10, 33, 16, 667262), 
'updated_at': datetime.datetime(2023, 12, 4, 10, 33, 16, 667302)}
(hbnb) 
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

```
$ ./console.py
(hbnb) create State
49a13545-e611-4951-9d73-f976fe6ada6e
(hbnb) create Place
8b304cae-974a-4a87-a61b-88e26ae978cf
(hbnb)
(hbnb) destroy State 49a13545-e611-4951-9d73-f976fe6ada6e
(hbnb) Place.destroy(8b304cae-974a-4a87-a61b-88e26ae978cf)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no 
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
28221803-5b84-4a36-81af-c8778d664291
(hbnb) create BaseModel
32d9358d-a9d3-4f8b-9006-a0dc0aae00b3
(hbnb) create User
e50379f2-2851-43e1-91c1-ca6eee32df46
(hbnb) create User
ad0c37eb-5f2a-4805-91b2-14e879560488
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (973410a2-7096-41f4-a4e9-01cb219bc229) {'updated_at': datetime.da
tetime(2023, 12, 4, 7, 16, 54, 204720), 'created_at': datetime.datetime(2023, 12, 4, 7, 16, 54, 204650), 'id': '973410a2-7096-41f4-a4e9-01cb219bc229'}", "[Bas
eModel] (1b2d6bce-9be8-4f44-8747-2ad75ede890f) {'updated_at': datetime.datetime
(2023, 12, 4, 8, 23, 41, 499064), 'created_at': datetime.datetime(2023, 12, 4, 8, 23, 41, 499036), 'id': '1b2d6bce-9be8-4f44-8747-2ad75ede890f'}"]
(hbnb)
(hbnb) User.all()
["[User] (be12df3a-e8c2-46f3-ae47-3d6bc6c51400) {'updated_at': datetime.datetim
e(2023, 12, 4, 8, 23, 41, 599824), 'created_at': datetime.datetime(2023, 12, 4, 8, 23, 41, 599804), 'id': 'be12df3a-e8c2-46f3-ae47-3d6bc6c51400'}", "[User] 
(c4368d4b-fdb1-45c3-a816-07c68d313c2d) {'updated_at': datetime.datetime(2023, 12, 4, 8, 24, 26, 606222), 'created_at': datetime.datetime(2023, 12, 4, 8, 24, 26, 606206), 'id': 'c4368d4b-fdb1-45c3-a816-07c68d313c2d'}"]
(hbnb) 
(hbnb) all
["[User] (be12df3a-e8c2-46f3-ae47-3d6bc6c51400) {'updated_at': datetime.datetim
e(2023, 12, 4, 8, 23, 41, 599824), 'created_at': datetime.datetime(2023, 12, 4, 8, 23, 41, 599804), 'id': 'be12df3a-e8c2-46f3-ae47-3d6bc6c51400'}", "[BaseMo
del] (973410a2-7096-41f4-a4e9-01cb219bc229) {'updated_at': datetime.datetime(2023, 12, 4, 7, 16, 54, 204720), 'created_at': datetime.datetime(2023, 12, 4, 7, 16, 54, 204650), 'id': '973410a2-7096-41f4-a4e9-01cb219bc229'}", "[User] (c4368d4b-fdb1-45c3-a816-07c68d313c2d) {'updated_at': datetime.datetime(2023, 12, 4, 8, 24, 26, 606222), 'created_at': datetime.datetime(2023, 12, 4, 8, 24, 26, 606206), 'id': 'c4368d4b-fdb1-45c3-a816-07c68d313c2d'}", "[BaseModel] (1b2d6bce-9be8-4f44-8747-2ad75ede890f) {'updated_at': datetime.datetime(2023, 12, 4, 8, 23, 41, 499064), 'created_at': datetime.datetime(2023, 12, 4, 8, 23, 41, 499036), 'id': '1b2d6bce-9be8-4f44-8747-2ad75ede890f'}"]
(hbnb)


```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Place
0d0887c2-3892-44a7-9df9-cc44d4576b3a
(hbnb) create Place
d4a3db78-2389-4cfd-b55f-519cf3eb439c
(hbnb) create City
e52ff3a7-9d4e-46d7-b7eb-6e21cfa87310
(hbnb) 
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb) 
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.

```
$ ./console.py
(hbnb) create User
af42ea06-1b32-46f1-b5a0-3c8e446c1b44
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Gabriel"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (af42ea06-1b32-46f1-b5a0-3c8e446c1b44) {'created_at': datetime.datetime(
2023, 12, 7, 0, 6, 19, 894392), 'first_name': 'Gabriel', 'updated_at': date
time.datetime(2023, 12, 7, 0, 6, 19, 894434), 'id': 'af42ea06-1b32-46f1-b5a0-3c8e446c1b44'}
(hbnb)
(hbnb) User.update(af42ea06-1b32-46f1-b5a0-3c8e446c1b44, address, "98 Mission S
t")
(hbnb) User.show(af42ea06-1b32-46f1-b5a0-3c8e446c1b44)
[User] (af42ea06-1b32-46f1-b5a0-3c8e446c1b44) {'created_at': datetime.datetime(
2023, 12, 7, 0, 6, 19, 894392), 'address': '98 Mission St', 'first_name': 
'Gabriel','updated_at': datetime.datetime(2023, 12, 7, 0, 6, 19, 894434), 'id
': 'af42ea06-1b32-46f1-b5a0-3c8e446c1b44'}
(hbnb)
(hbnb) User.update(af42ea06-1b32-46f1-b5a0-3c8e446c1b44, {'email': 
'bengabrielisek@gmail.com', 'last_name': 'Ben'})
[User] (af42ea06-1b32-46f1-b5a0-3c8e446c1b44) {'email': 'bengabrielisek@gmail.co
m', 'first_name': 'Gabriel', 'updated_at': datetime.datetime(2023, 12, 7, 0, 6, 19, 894434), 'address': '98 Mission St', 'last_name': 'Ben', 'id': 'af42ea06-1b32-46f1-b5a0-3c8e446c1b44', 'created_at': datetime.datetime(2023, 12, 7, 0, 6, 19, 894392)}
(hbnb) 
```

## Testing :straight_ruler:

Unittests for the AirBnB project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run each  time:

```
$ python3 unittest -m tests/test_console.py
``` 
