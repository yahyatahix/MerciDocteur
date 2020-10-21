#include <stdio.h>
int main(int argc, char* argv[], char* arge[]){
	int i=0;
   	printf("Content-type: text/plain\n\n");
   	while (arge[i])
		printf("%s\n",arge[i++]);
}
