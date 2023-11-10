#!/usr/bin/python3
"""Console module for the command line app."""
import cmd
from models import storage
import config


class HBNBCommand(cmd.Cmd):
    """
    The AirBNB clone cli entry point.
    """
    prompt = "(hbnb)"

    def emptyline(self):
        return

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, _):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        """Creates a new class.\nUsage:
        create <class_name>"""
        argv = args.split()
        if len(argv) != 1:
            print("** class name missing **")
            return
        if argv[0] not in config.ACCEPTED_CLASSES.keys():
            print("** class doesn't exist **")
            return

        cls_name = argv[0]
        new_model = None
        if cls_name in list(config.ACCEPTED_CLASSES.keys()):
            new_model = config.ACCEPTED_CLASSES[cls_name]()
        if new_model:
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """Prints out a stored class.\nUsage:
        show <class_name>"""
        argv = args.split()
        argc = len(argv)
        if argc < 1:
            print("** class name missing **")
            return
        cls_name = argv[0]
        if cls_name not in config.ACCEPTED_CLASSES.keys():
            print("** class doesn't exist **")
            return
        if argc < 2:
            print("** instance id missing **")
            return
        id = argv[1]
        saved_model = storage.all().get("{}.{}".format(cls_name, id))

        if not saved_model:
            print("** no instance found **")
            return

<<<<<<< HEAD
    def do_destroy(self, args):
        pass
=======
        print(saved_model)

    def do_destroy(self, args):
        """Deletes an existing class.\nUsage:
        destroy <class_name> [existing_object_id]"""
        argv = args.split()
        argc = len(argv)
        if argc < 1:
            print("** class name missing **")
            return
        if argv[0] not in config.ACCEPTED_CLASSES.keys():
            print("** class doesn't exist **")
            return
        cls_name = argv[0]
        if argc < 2:
            print("** instance id missing **")
            return
        id = argv[1]
        try:
            del storage.all()["{}.{}".format(cls_name, id)]
            storage.save()
        except KeyError:
            print("** no instance found **")

        return
>>>>>>> 1fb53ec83f4fb381383649fde7fd010fd34af9f5

    def do_all(self, args):
        """Prints out all stored class.\nUsage:
        all
        all <class_name>"""
        argv = args.split()
        argc = len(argv)
        if argc > 0 and argv[0] not in config.ACCEPTED_CLASSES.keys():
            print("** class doesn't exist **")
            return
        if argc == 0:
            saved_models = [str(model) for model in storage.all().values()]
        else:
            saved_models = [
                str(model)
                for model in storage.all().values()
                if model.__class__.__name__ == argv[0]
            ]
        print(saved_models)

    def do_update(self, args: str):
        """Updates a stored class with new attributes.\nUsage:
        update <class_name> <existing_id> <argument_name> <argument_value>"""
        argv = args.split(maxsplit=3)
        argc = len(argv)
        if argc < 1:
            print("** class name missing **")
            return
        cls_name = argv[0]
        if cls_name not in config.ACCEPTED_CLASSES.keys():
            print("** class doesn't exist **")
            return
        if argc < 2:
            print("** instance id missing **")
            return
        id = argv[1]
        saved_model = storage.all().get(cls_name + "." + id)
        if not saved_model:
            print("** no instance found **")
            return
        if argc < 3:
            print("** attribute name missing **")
            return
        if argc < 4:
            print("** value missing **")
            return
        attr_name = argv[2]
        attr_value = argv[3].strip("\"")

        setattr(saved_model, attr_name, attr_value)
        saved_model.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
