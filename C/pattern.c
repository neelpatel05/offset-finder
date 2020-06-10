#include<stdio.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>

char UPPERCASE[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
char LOWERCASE[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char NUMBERS[] = {'0','1','2','3','4','5','6','7','8','9'};

void argment_check(int number_of_argument) {
    if (number_of_argument != 2) {
        puts("Usage ./pattern <length>");
        exit(0);
    }
}

void create_string(int length) {

    char pattern[length];

    for(int  i=0; i<26; i++) {
        strncat(pattern, &UPPERCASE[i], 1);
        
        for (int j=0; j<26; j++) {
            strncat(pattern, &LOWERCASE[j], 1);

            for (int k=0; k<10; k++) {
                strncat(pattern, &NUMBERS[k], 1);
                
                if ((strlen(pattern)-1) == length) {
                    pattern[strlen(pattern)] = '\0';
                    printf("%s\n",pattern);
                    exit(0);
                } else if ((length - (strlen(pattern)-1)) == 1) {
                    strncat(pattern, &UPPERCASE[i], 1);
                    pattern[strlen(pattern)] = '\0';
                    printf("%s\n",pattern);
                    exit(0);
                } else if ((length - (strlen(pattern)-1)) == 2) {
                    strncat(pattern, &LOWERCASE[j], 1);
                    pattern[strlen(pattern)] = '\0';
                    printf("%s\n",pattern);
                    exit(0);
                } else {
                    strncat(pattern, &UPPERCASE[i],1);
                    strncat(pattern, &LOWERCASE[j],1);
                }
            }
        }
    }
}

int main(int argc, char** argv) {
    argment_check(argc);

    int length = atoi(argv[1]);
    create_string(length);

    return 0;
}