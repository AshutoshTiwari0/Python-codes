exception=ExceptionGroup("can not divide by zero",
                         [FileNotFoundError("file nhi hai"),
                          FileNotFoundError("kaha na nhi hai")])


try:
    raise exception
#except ExceptionGroup as E:
 #   print(E.exceptions)
except* FileNotFoundError as E:
    print(E.exceptions)