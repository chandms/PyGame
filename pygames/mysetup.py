import cx_Freeze

executables = [cx_Freeze.Executable('snake.py')]

cx_Freeze.setup(name="OldSnake",

                options ={

                    "build_exe":{

                        "packages" : ["pygame"],
                        "include_files" : ['apple.png','snakehead.png','snakebody.png','icon.png']

                    }
                },

                description = "Old Snake Game ",
                executables = executables

                )