#include <stdio.h>

int main() {
    int rot;
    int length;
    printf("ROT? > ");
    scanf("%d", &rot);
    printf("length > ");
    scanf("%d", &length);
    char str[length];
    printf("string & $ > ");
    scanf("%[^$}", &str);
    for (int i = 0; i < length; i++) {
        if ((str[i] >= 65 && str[i] <= 90 - rot) || (str[i] >= 97 && str[i] <= 122 - rot)) str[i] += rot;
        else if ((str[i] > 90 - rot && str[i] <= 90) || (str[i] > 122 - rot && str[i] <= 122)) str[i] -= rot;
    }
    printf("%s", str);
    return 0;
}
