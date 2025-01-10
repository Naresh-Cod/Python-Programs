#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LEN 128

// Function to generate a random character
char getRandomChar() {
    char chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int index = rand() % strlen(chars);
    return chars[index];
}

// Function to generate a random password of the same length
void generatePassword(char *guess, int length) {
    for (int i = 0; i < length; i++) {
        guess[i] = getRandomChar();
    }
    guess[length] = '\0'; // Null-terminate the string
}

int main() {
    char password[MAX_LEN], guess[MAX_LEN];
    int attempts = 0;

    printf("Enter the password to guess: ");
    scanf("%s", password);

    int passwordLength = strlen(password);

    // Seed the random number generator
    srand(time(0));

    do {
        generatePassword(guess, passwordLength);
        attempts++;

        printf("Attempt %d: Trying password: %s\n", attempts, guess);
    } while (strcmp(guess, password) != 0);

    printf("\nPassword guessed successfully after %d attempts!\n", attempts);
    printf("The password is: %s\n", guess);

    return 0;
}
