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
        attr_value = argv[3].strip('"')

        setattr(saved_model, attr_name, attr_value)
        saved_model.save()

    def default(self, line):
        if not line.strip().startswith(tuple(config.ACCEPTED_CLASSES.keys())):
            return super().default(line)
        _cmd = line.split(".")
        _cmd_name = _cmd[0]
        _cmd_method = _cmd[1]

        _accepted_cmds = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        _cmd_args = _cmd_method.split("(")

        if _cmd_args[0] not in _accepted_cmds:
            return super().default(line)

        if _cmd_method in list(_accepted_cmds.keys())[0:2]:
            _accepted_cmds[_cmd_args[0]](_cmd_name)
        elif _cmd_args[0].strip() == "update":
            parameters = _cmd_args[1].strip(")").split(",")

            if parameters[1].strip().startswith("{") and len(parameters) == 2:
                arg_str = parameters[1].strip().strip("}").strip("{")
                update_args = arg_str.split(":")
                arg_str = "{} {} {}".format(
                    _cmd_name,
                    parameters[0],
                    " ".join(update_args),
                )
            else:
                arg_str = "{} {}".format(_cmd_name, " ".join(parameters))
            _accepted_cmds[_cmd_args[0]](arg_str)

        else:
            parameters = _cmd_args[1].strip(")")
            arg_str = "{} {}".format(_cmd_name, parameters)
            _accepted_cmds[_cmd_args[0]](arg_str)

    def count(self, line):
        print(
            len(
                [
                    k
                    for k in storage.all().keys()
                    if k.startswith(
                        line.strip(),
                    )
                ],
            ),
        )


if __name__ == "__main__":
    HBNBCommand().cmdloop()
