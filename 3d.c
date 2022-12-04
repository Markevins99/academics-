#include<stdio.h>
void main()
{
    int i,j,k,cube[30][30][30],a,b,c,sid;
    printf("enter the no of attributes for sleeping habbit\n");
    scanf("%d",&a);
    printf("enter the no of attributes for names and student id\n");
    scanf("%d",&b);
    printf("enter the no of attributes for semester\n");
    scanf("%d",&c);
    printf("enter the values\n");
    for(i=0;i<c;i++)
    {
        for(j=0;j<b;j++)
        {
            for(k=0;k<a;k++)
            {
                scanf("%d",&cube[i][j][k]);
            }
        }
    }
    printf("the cube is\n");
    for(i=0;i<c;i++)
    {
        for(j=0;j<b;j++)
        {
            for(k=0;k<a;k++)
            {
                printf("%d\t",cube[i][j][k]);

            }
            printf("\n");
        }
        printf("\n");
    }
    printf("\n the attributes for sleeping habbits are: \n ");
    for(k=0;k<a;k++)
            {
                printf("%d\t",cube[0][0][k]);
            }
    printf("\n the attributes for names and student id are \n");
    for(j=1;j<b;j++)
        for(k=0;k<2;k++)
            {
                printf("%d\t",cube[0][j][k]);
            }
    printf("\n the attributes for semester are \n");

    for(i=1;i<c;i++)
    {
        for(j=0;j<2;j++)
        {

        for(k=0;k<2;k++)
            {
                printf("%d\t",cube[i][j][k]);
            }
        }
}

printf("\n find  the sleeping habbit of the student by std id:\n");
scanf("%d",&sid);



if(cube[0][1][0]==sid)
{
  printf("early sleeper");


}

else{
    printf("late sleeper");

}

}


