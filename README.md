noti.py
=======
simple script to show system notifications on Linux

this project is inspired by [noti](https://github.com/variadico/noti), which does similar thing, but is written in Go

installation
------------

with **wget**:
```
sh -c "$(wget https://raw.githubusercontent.com/pwittchen/noti.py/master/install.sh -O -)"
```

with **curl**:
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/pwittchen/noti.py/master/install.sh)"
```

usage
-----

```
noti.py -t <title> -m <message>
```

screenshot
----------

after making the following call from terminal:

```
noti.py -t "noti.py" -m "hello"
```

we should see the following notification in the upper-right corner of the screen:

![Screenshot](https://raw.githubusercontent.com/pwittchen/noti.py/master/screenshot.png)

if you are using Gnome 3, you will see the following notification in the top of the screen:

![Screenshot](https://raw.githubusercontent.com/pwittchen/noti.py/master/screenshot-gnome3.png)


