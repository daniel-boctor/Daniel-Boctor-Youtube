// PSET1: write a program that accepts a password from the user
// if the password matches the string 'super secret', let the user in

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int length = strlen(argv[1]);
    char password[length];
    memcpy(password, argv[1], length);

    if (strcmp(password, "super secret") == 0) {
        printf("PASSWORDS MATCH! Access granted...\n");
    } else {
        printf("INCORRECT PASSWORD!\n");
    }

    return 0;
}