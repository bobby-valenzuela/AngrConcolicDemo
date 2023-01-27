# AngrConcolicDemo
Concolic (Dynamic Symbolic Execution) with Angr demo on a simple binary.

Statuc Code Analysis usually involves one ouring over code to visualize any potential paths that a program might take.
Symbolic execution (SE), takes this one step further as it evaluates a binary itself making it programming-language-agnostic.
SE usually requires some sort of a "Theorem Prover" (such as the very powerful Z3 theorem prover developed by Microsoft).
Though SE is amazing - it does suffer some potential scalability issues with potentially larger programs.

This is where Dynamic Symbolic Execution (DSE) comes in (also called "concolic") and Angr is one of the best implementations of DSE.

Using Angr, we can test a binary file and see all the possible paths it might take.
Further, if we know some bits of the expected output of a given path, we can run Angr to try and find that path for us.

In this case, I have a sample script in C which returns a success message if a certain number is entered upon running the program.
We don't need to know the number, but just how the successful (or otherwise) state would look like then feed that state into Angr and Angr will tell us what we need to do to get to that state. For this example. this means we just need to tell Angr what the successful message might look like and Angr will process the binary (though not executing it) and look at every possible outcome, it will eventually find the successful state, and finally it will tell us what we need to do to get to that state.I.E. which number we need to enter to find the success state.

All this happens while  we have no idea the secret number might be - but only what the successful state looks like.

__Note__: Basic code/setup taken as a template from "Ethical Hackin: A Hands-on Introduction to Breaking in" 2021 | No Startch Press.


# Creating the binary
I have the basic program saved in simple.c and it has been compiled into a binary using `gcc simple.c -o simple` and saved as `simple`.

# Installing/Running Angr