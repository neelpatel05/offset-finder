#include<stdio.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>

char UPPERCASE[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
char LOWERCASE[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char NUMBERS[] = {'0','1','2','3','4','5','6','7','8','9'};

void argment_check(int number_of_argument) {
    if (number_of_argument != 3) {
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

void find_offset(char *query) {

    char string[50];
    int len = strlen(query);

    for (int i = 0, j = 0; j < len; ++i, j+=2) {
        int val[1];
        sscanf(query + j, "%2x", val);
        string[i] = val[0];
        string[i + 1] = '\0';
    }
    string[strlen(string)] = '\0';
    printf("%s",string);
}

int main(int argc, char** argv) {
    argment_check(argc);

    if (strcmp(argv[1],"length") == 0) {
        int length = atoi(argv[2]);
        create_string(length);
    } else if (strcmp(argv[1],"query") == 0) {
        create_string(21000);
        find_offset(argv[2]);
    }

    return 0;
}