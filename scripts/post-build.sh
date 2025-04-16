#!/bin/bash
echo '# import custom MoneiClient' >>./Monei/__init__.py
echo 'from Monei.monei_client import MoneiClient' >>./Monei/__init__.py
echo 'from Monei.models import *' >>./Monei/__init__.py
echo 'from Monei.apis import *' >>./Monei/__init__.py
echo 'from Monei.exceptions import *' >>./Monei/__init__.py
