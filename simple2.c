#include <stdio.h>


void level2_checkPass(int val){

    if(val==123){
        printf("Access Granted!\n");
    }
}

int level2_check(){

    printf("Enter second secret pass: ");
    int y = 0;
    scanf("%d",&y);
    int* y_Ptr = &y;
    int y_val = *y_Ptr;
    level2_checkPass(y_val);
}

void checkPass(int x){
    // Print success msg if secret code entered
    if(x == 7857){
        // printf("Access Granted!\n");

        int response = level2_check();

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
