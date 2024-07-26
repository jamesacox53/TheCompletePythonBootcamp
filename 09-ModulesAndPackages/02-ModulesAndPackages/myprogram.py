# The __init__.py file tells Python that the directory is
# a Package/Subpackage. It allows you to run what we see
# here.

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript
from mymodule import my_func

some_main_script.report_main()

mysubscript.sub_report()

my_func()