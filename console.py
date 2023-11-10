#!/usr/bin/python3
import cmd
from models import storage
import config


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self):
        return

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, _):
        return True

    def do_create(self, args):
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

        print(saved_model)

    def do_destroy(self, args):
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

    def do_all(self, args):
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
