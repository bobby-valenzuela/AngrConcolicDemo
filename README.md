# AngrConcolicDemo
Concolic (Dynamic Symbolic Execution) with Angr demo on a simple binary.

Static Code Analysis usually involves one pouring over code to visualize any potential paths that a program might take.
Symbolic execution (SE), takes this one step further as it evaluates a binary itself making it programming-language-agnostic.
SE usually requires some sort of a "Theorem Prover" (such as the very powerful Z3 theorem prover developed by Microsoft).
Though SE is amazing - it does suffer some potential scalability issues with potentially larger programs.

This is where Dynamic Symbolic Execution (DSE) comes in (also called "concolic") and Angr is one of the best implementations of DSE.

Using Angr, we can test a binary file and see all the possible paths it might take.
Further, if we know some bits of the expected output of a given path, we can run Angr to try and find that path for us.

In this case, I have a sample script in C which returns a success message if a certain number is entered upon running the program.
We don't need to know the number, but just how the successful (or otherwise) state would look like then feed that state into Angr and Angr will tell us what we need to do to get to that state. For this example. this means we just need to tell Angr what the successful message might look like and Angr will process the binary (though not executing it) and look at every possible outcome, it will eventually find the successful state, and finally it will tell us what we need to do to get to that state.I.E. which number we need to enter to find the success state.

All this happens while  we have no idea the secret number might be - but only what the successful state looks like.

__Note__: Basic code/setup taken as a template from "Ethical Hacking: A Hands-on Introduction to Breaking in" 2021 | No Startch Press.


# Creating the binary
I have the basic program saved in simple.c and it has been compiled into a binary using 
```bash
$ gcc simple.c -o simple
``` 
and saved as 'simple'.

# Installing/Running Angr

Install Python's Virtual Environment & Dependencies (this prevents any potential lib conflicts)

```bash
$ sudo apt install python3-dev libffi-dev build-essential virtualenvwrapper -y
```

Configure/Activate Virtual Envinronment Wrapper (source it)

```bash
$ . /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```


Create new Virtual Environment

```bash
$mkvirtualenv --python=$(which python3) angrEnv
```

Install Angr in this newly created environment

```bash
python3 -m pip install angr
``` 
or 
```bash
$ pip3 install angr
```  
(I prefer the former)

You should see the __angrEnv__ label in ther terminal prompt.

Docs for using angr: https://docs.angr.io/core-concepts/toplevel


Finally, run Angr against our binary to find the password (7857)

```bash
$ python3 angrSim.py
```

If all went well, Angr should find the password and output `Found Solution: 7857`.     
<br />
<br />
  
The "simple2.c" program is a tiny bit more complex and accepts two inputs: 7857 and 123.
If you want to test with this program you can compile this one instead: 

```bash
$ gcc simple2.c -o simple
```

Then run Angr on the "simple" binary that was just created

```bash
$ python3 angrSim.py
```

You should see: `Found Solution: 78570000000123`

Not really a "useful" program here - but it served as a great demo for me to depper understand Symbolic Execution and how it all works.  
  
![Alt text](./demo-001.gif?raw=true "Demo 1")
