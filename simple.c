#include <stdio.h>

void checkPass(int x){
    // Print success msg if secret code entered
    if(x == 7857){
        printf("Access Granted!\n");
    }else{
        printf("Access Denied!\n");
    }
}

int main(int argc, char *argv[]){
    int x = 0;
    printf("Enter the password: ");
    // Read input
    scanf("%d", &x);
    // Validate input
    checkPass(x);
}