#include <stdio.h>
#include <string.h>

int main() {
    char stored_sapid[] = "500121943";
    char user_sapid[50];

    while (1) {
        printf("Enter your SAP ID: ");
        scanf("%s", user_sapid);

        if (strcmp(user_sapid, stored_sapid) == 0) {
            printf("Matched\n");
        } else {
            printf("Not Matched\n");
        }
    }

    return 0;
}